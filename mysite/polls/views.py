from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegistrationForm
from .models import SanPham
from .models import DonHang
from .models import NhaCungCap
from django.contrib.auth import authenticate, login , logout
def index(request):
    sanpham = SanPham.objects.all()
    context = {"sanpham": sanpham }
    return render(request ,"polls/index.html",context)

def account(request):
    return render(request ,"polls/account.html",)

def contact(request):
    return render(request ,"polls/contact.html")

def NotFound(request):
    return render(request ,"polls/404.html")
def login(request):
    return render(request, "polls/login.html")

def cart(request):
    carts = DonHang.objects.all()
    context = {"cart": carts }
    return render(request ,"polls/cart.html",context)

def gifts(request):
    return render(request ,"polls/gifts.html")

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request ,"polls/register.html",{'form': form})

def store(request):
    return render(request ,"polls/store.html")

def wishlist(request):
    return render(request ,"polls/wishlist.html")
    
def single(request):
    return render(request ,"polls/single.html")
    

def logout_view(request):
    logout(request)
    return render(request, 'polls/login.html')