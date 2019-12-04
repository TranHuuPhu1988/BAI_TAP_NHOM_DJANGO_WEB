from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request ,"polls/index.html")

def account(request):
    return render(request ,"polls/account.html")

def contact(request):
    return render(request ,"polls/contact.html")

def NotFound(request):
    return render(request ,"polls/404.html")

def cart(request):
    return render(request ,"polls/cart.html")

def gifts(request):
    return render(request ,"polls/gifts.html")

def register(request):
    return render(request ,"polls/register.html")

def store(request):
    return render(request ,"polls/store.html")

def wishlist(request):
    return render(request ,"polls/wishlist.html")
    
def single(request):
    return render(request ,"polls/single.html")
    
