from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app2.models import *
from django.contrib.auth.decorators import login_required
from app1.models import *
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse

def uploadproduct(request):
    if request.session.get('username'):
        if request.method=='POST' and request.FILES:
            product_type=request.POST['product_type']
            image=request.FILES['image']
            productname=request.POST['productname']
            price=request.POST['price']
            description=request.POST['description']
            username=request.session.get('username')
            user=User.objects.get(username=username)
            prd=Upload_product.objects.create(username=user,product_type=product_type,productname=productname,product_price=price,product_descrition=description,product_image=image)
            prd.save()
            return HttpResponseRedirect(reverse('userproductlist'))
        return render(request,'app2/uploadproduct.html')
    else:
        return HttpResponseRedirect(reverse('log_form'))


class ProductDetail(DetailView):
    template_name='app2/product_detail.html'
    model=Upload_product
    context_object_name='prodetail'

def productorder(request):
    if request.session.get('username'):
        if request.method=='POST':
            number=request.POST['number']
            pro_id=request.POST['id']
            user=request.session.get('username')
            username=User.objects.get(username=user)
            prod=Upload_product.objects.get(product_id=pro_id)
            #prime=product_or.product_id
            RS=prod.product_price
            uk=username.username
            ck=prod.username
            num=int(number)
            tol=RS*num
            ordersave=Orderes.objects.create(username=prod.username, customer=uk,product_id=prod,how_many=num,total=tol)
            ordersave.save()
            pko=Orderes.objects.filter(username=username)
            h=0
            for x in pko:
                if h<x.pk:
                    h=x.pk
            cusorder=customorder(username=username,prime_pk=h,ordercustomer=ck,product_id=prod,how_many=num,total=tol)
            cusorder.save() 
            pid=prod.pk
            return HttpResponseRedirect(reverse('orderdetails'))

        return HttpResponse('given not proper valid') 
    else:
        return HttpResponseRedirect(reverse('log_form'))

@login_required
def get_detail(request):
    us=request.session.get('username')
    user=User.objects.get(username=us)
    OR=Orderes.objects.filter(username=user)
    l=set()
    for x in OR:
        pr=Upload_product.objects.get(product_id=str(x))
        k=pr
        l.add(k)
    d={'OR':OR,'l':l}
    return render(request,'app2/get_detail.html',d)


def customerdetail(request):
    if request.session.get('username'):
        username=request.session.get('username')
        user=User.objects.get(username=username)
        ou=Upload_product.objects.filter(username=user).order_by('-pk')
        prf=customorder.objects.filter(product_id__in=ou).order_by('-pk')
        d={'ou':ou,'prf':prf}
        return render(request,'app2/customerdetail.html',d)
    else:
        return HttpResponseRedirect(reverse('log_form'))
