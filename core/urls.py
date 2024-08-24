from django.conf.urls.static import static
from django.conf import settings
from django.urls import path #include,
from core import views
from core.views import *
from django.contrib import admin
from .views import shop_details
from .views import blog_details

# from django.conf.urls import static
# from core.urls import urlpatterns as core_urlpatterns 
# from views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', shop, name='shop'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('shop-details/<slug:slug>/', shop_details, name='shop_details' ),
    path('blog-details/<slug:slug>/', blog_details, name='blog_details'),
    path('checkout/', checkout, name='checkout'),
    path('shopping-cart/', shopping_cart, name='shopping_cart'),
    path('discount-details/<slug:slug>/', discount_details, name='discount_details'),
    path('departments/<slug:slug>', departments, name='departments')
    
   
]



urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)