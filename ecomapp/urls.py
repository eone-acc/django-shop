from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.base_view, name='base'),
    path('category/<str:category_slug>/', views.category_view, name='category_detail'),
    path('product/<str:product_slug>/', views.product_view, name='product_detail'),
    path('add_to_cart/<str:product_slug>', views.add_to_cart_view, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart')


]

