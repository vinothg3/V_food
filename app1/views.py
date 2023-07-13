
from django.shortcuts import render
from app1.forms import *
from app1.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from app2.models import *
from django.db.models import Q
from django.views.generic import DetailView
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def home(request):
    if request.session.get('username'):
        user=request.session.get('username')
        return HttpResponseRedirect(reverse('product_list'))
    return render(request,'app1/home.html')

def register_form(request):
    user=user_form()
    d={'user':user}

    if request.method=='POST':
        usr=user_form(request.POST)
        if usr.is_valid():
            us=usr.save(commit=False)
            us.set_password(usr.cleaned_data['password'])
            us.save()
            ''' send_mail('register_form',
                      'Your Register successfully',
                      'kerukkucreation@gmail.com',
                      [us.email],
                      fail_silently=False)'''
            return HttpResponseRedirect(reverse('log_form'))
        else:
            messages.success(request, 'username already there')
        
    return render(request,'app1/register_form.html',d)
def log_form(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        ACT=authenticate(username=username, password=password)
        if ACT and ACT.is_active:
            login(request,ACT)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request, 'username not there')

    return render(request,'app1/log_form.html')

@login_required
def logout_form(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile_data(request):
    username=request.session.get('username')
    user=User.objects.get(username=username)
    uk=profile.objects.filter(username=user)
    if uk:
        pro=profile.objects.get(username=user)
        d={'user':user,'pro':pro}
    else:
        d={'user':user}
    
    return render(request,'app1/profile_data.html',d)

@login_required
def profileupdate(request):
    if request.method=='POST' and request.FILES:
        image=request.FILES['image']
        username=request.session.get('username')
        user=User.objects.get(username=username)
        prof=profile.objects.filter(username=user)
        if prof:
            pro=profile.objects.get(username=user)
            pro.profile_pic=image
            pro.save()
            return HttpResponseRedirect(reverse('profile_data')) 
        else:
            pro=profile.objects.create(username=user,profile_pic=image)
            pro.save()
            return HttpResponseRedirect(reverse('profile_data')) 
    return render(request,'app1/profileupdate.html')

def update_description(request):
    if request.method=='POST':
        description=request.POST['description']
        username=request.session.get('username')
        user=User.objects.get(username=username)
        prof=profile.objects.filter(username=user)
        if prof:
            pro=profile.objects.get(username=user)
            pro.description=description
            pro.save()
            return HttpResponseRedirect(reverse('profile_data')) 
        else:
            pro=profile.objects.create(username=user,description=description)
            pro.save()
            return HttpResponseRedirect(reverse('profile_data')) 
    return render(request,'app1/update_description.html')
def update_address(request):
    if request.method=='POST':
        address=request.POST['address']
        pin=request.POST['pin']

        username=request.session.get('username')
        user=User.objects.get(username=username)
        prof=profile.objects.filter(username=user)
        if prof:
            pro=profile.objects.get(username=user)
            pro.Address=address
            pro.pincode=pin
            pro.save()
            return HttpResponseRedirect(reverse('profile_data')) 
        else:
            pro=profile.objects.create(username=user,Address=address,pincode=pin)
            pro.save()
            return HttpResponseRedirect(reverse('profile_data')) 
    return render(request,'app1/update_address.html')


def product_list(request):
    if request.method=='POST':
        srh=request.POST['search']
        obj=Upload_product.objects.filter(Q(product_type__startswith=srh) | Q(productname__startswith=srh))
    else:
        obj=Upload_product.objects.all()
    d={'listpro':obj}
    return render(request,'app1/product_list.html',d)


def orderdetails(request):
    if request.session.get('username'):
        username=request.session.get('username')
        user=User.objects.get(username=username)
        prf=Upload_product.objects.all().order_by('-product_id')
        prod=Orderes.objects.filter(Q(product_id__in=prf)&Q(customer=user) ).order_by('-pk')
        
        d={'prf':prf,'prod':prod}
        return render(request,'app2/orderdetails.html',d)
    else:
        return HttpResponseRedirect(reverse('log_form'))
    

class OrderesDetail(DetailView):
    template_name='app1/orderes_detail.html'
    model=Orderes
    context_object_name='del'

@login_required
def conformorder(request):
    if request.method=='POST':
        conform=request.POST['conform']
        pri=request.POST['pri']
        pki=request.POST['pki']
        
        Orderes.objects.filter(pk=pri).update(product_accepted=conform)
        customorder.objects.filter(pk=pki).update(orderconform=conform)
        return HttpResponseRedirect(reverse('customerdetail'))
    return HttpResponse('not valid')

def ordercancel(request):
    if request.method=='POST':
        cancel=request.POST['cancel']
        pri=request.POST['prk']
        orb=Orderes.objects.filter(pk=pri).update(cancel=cancel)
        return HttpResponseRedirect(reverse('orderdetails'))

def menus(request):
    upo=Upload_product.objects.all()
    l=[]
    k=[]
    for x in upo:
        if x.product_type not in l:
            l.append(x.product_type)
            k.append(x.product_image)
    d={'l':l}
    return render(request,'app1/menus.html',d)


def menusdetail(request,str):
    obj=Upload_product.objects.filter(product_type=str)
    d={'listpro':obj}
    return render(request,'app1/product_list.html',d)

@login_required
def userproductlist(request):
    user=request.session.get('username')
    username=User.objects.get(username=user)
    up=Upload_product.objects.filter(username=username)
    d={'up':up}
    return render(request,'app1/userproductlist.html',d)