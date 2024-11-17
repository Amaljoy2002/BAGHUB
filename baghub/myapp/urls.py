from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('' , views.index,name="index"),
    path('about',views.about,name = "about"),
    path('home',views.home,name = "home"),
    path('login1',views.login1,name = "login1"),
    path('login2',views.login2,name = "login2"),  
    path('login/', views.login2, name='login'),
    path('signup_view/',views.signup_view,name = "signup_view"),
    path('signup/', views.signup, name='signup'), 
    path('products/',views. product_listing, name='product_listing'),
    # path('products/',views. product_listing1, name='product_listing1'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('cart/', views.cart_view, name='cart_view'),  # Rename this if necessary
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('order/confirmation/', views.order_confirmation, name='order_confirmation'),
    path('order/success/', views.order_success, name='order_success'),
    

    

]