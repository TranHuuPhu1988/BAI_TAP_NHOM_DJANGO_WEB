from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login , logout
urlpatterns = [
    path('', views.index ,name='index'),
    #path('logout/', views.account , name="account"),
    path('contact/', views.contact , name="contact"),
    path('store/', views.store , name="store"),
    path('404/', views.NotFound ,name='404'),
    path('gifts/', views.gifts , name="gifts"),
    path('register/', views.register , name="register"),
    path('wishlist', views.wishlist , name="wishlist"),
    path('single/', views.single , name="single"),
    path('cart/', views.cart , name="cart"),
    # path('login/', views.login , name="login"),
    path('account/',auth_views.LoginView.as_view(template_name="polls/account.html"), name="account"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),

]