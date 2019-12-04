from django.urls import path

from . import views

urlpatterns = [
    path('', views.index ,name='index'),
    path('account/', views.account , name="account"),
    path('contact/', views.contact , name="contact"),
    path('store/', views.store , name="store"),
    path('404/', views.NotFound ,name='404'),
    path('gifts/', views.gifts , name="gifts"),
    path('register/', views.register , name="register"),
    path('wishlist', views.wishlist , name="wishlist"),
    path('single/', views.single , name="single"),
    path('cart/', views.cart , name="cart"),
]