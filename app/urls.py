from django.urls import path

from . import admin
from .views import home_view,products_view,contact_view,cart_view,testimonial_view,chackout_view,category_view,shop_view
urlpatterns = [
    path('',home_view,name='index'),
    path('product/',products_view,name='products'),
    path('contact/',contact_view,name='contact'),
    path('testimonial/',testimonial_view,name='testimonial'),
    path('cart/',cart_view,name='cart'),
    path('chackout/',chackout_view,name='chackout'),
    path('category/',category_view,name='category'),
    path('shop_view/',shop_view,name='shop'),

]