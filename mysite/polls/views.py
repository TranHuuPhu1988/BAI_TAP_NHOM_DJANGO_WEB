from django.http import HttpResponse
from django.shortcuts import render
from .models import SanPham
from .models import DonHang
from .models import NhaCungCap
from .models import Order

def index(request):
    sanpham = SanPham.objects.all()
    context = {"sanpham": sanpham }
    return render(request ,"polls/index.html",context)

def account(request):
    return render(request ,"polls/account.html")

def contact(request):
    return render(request ,"polls/contact.html")

def NotFound(request):
    return render(request ,"polls/404.html")

def cart(request):
    carts = DonHang.objects.all()
    context = {"cart": carts }
    return render(request ,"polls/cart.html",context)

def gifts(request):
    return render(request ,"polls/gifts.html")

def register(request):
    return render(request ,"polls/register.html")

def store(request):
    sanpham = SanPham.objects.all()
    context = {"sanpham": sanpham }
    return render(request ,"polls/store.html",context)

def wishlist(request):
    return render(request ,"polls/wishlist.html")
    
def single(request):
    order = Order.object().all()
    context = {"order":order}
    return render(request ,"polls/single.html",context)
    
def checkout(request):
    if request.method == "POST":
        images = request.POST.get('images','')
        GiaDaGiam = request.POST.get('GiaDaGiam','')
        Ten = request.POST.get('Ten','')
