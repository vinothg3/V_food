"""pro_hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from app1.views import *
from app2.views import *
from app1 import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('home/',home,name='home'),
    path('register_form/',register_form,name='register_form'),
    path('log_form/',log_form,name='log_form'),
    path('logout_form/',logout_form,name='logout_form'),
    path('profile_data/',profile_data,name='profile_data'),
    path('profileupdate/',profileupdate,name='profileupdate'),
    path('update_description/',update_description,name='update_description'),
    path('uploadproduct/',uploadproduct,name='uploadproduct'),
    path('product_list/',product_list,name='product_list'),
    path('productorder/',productorder,name='productorder'),
    path('orderdetails/',orderdetails,name='orderdetails'),
   
    path('customerdetail/',customerdetail,name='customerdetail'),
    path('conformorder/',conformorder,name='conformorder'),
    path('ordercancel/',ordercancel,name='ordercancel'),
    path('update_address',update_address,name='update_address'),
    path('menus/',menus,name='menus'),
    path('userproductlist/',userproductlist,name='userproductlist'),
    
    path('menus/<slug:str>/',views.menusdetail),
    
    
    #re_path('menus/(<slug>\w+)',fetch_data,name='fetch_data' ),
    re_path('orderdetails/(?P<pk>\d+)/',OrderesDetail.as_view(),name='detail'),

    re_path('(?P<pk>\d+)/',ProductDetail.as_view(),name='detail'),
    
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
