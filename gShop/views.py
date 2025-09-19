from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.http import JsonResponse
import requests
from .models import Gold, Wishlist
from django.utils import translation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SignUpForm
from django.contrib import messages

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      #messages.success(request, 'Account created successfully')
      login(request, form.save())
      return redirect('/product/')
  else:
    form = SignUpForm()  

  return render(request, 'signup.html', {
    'form': form
  })

def logout_view(request):
  if request.method == "POST":
    logout(request)
    return redirect("/")

def index(request):
  return render(request, 'index.html')
def profile(request):
  return render(request, 'index.html')
def blog_detail(request):
  return render(request, 'blog_detail.html')
def blog(request):
  return render(request, 'blog.html')
def cart(request):
  return render(request, 'cart.html')
def checkout(request):
  return render(request, 'checkout.html')
def contact(request):
  return render(request, 'contact.html')
def detail(request):
  return render(request, 'detail.html')
#def product(request):
 # return render(request, 'product.html')
def about(request):
  return render(request, 'about.html')

@login_required
def add_to_wishlist(request, pk):
  item = get_object_or_404(Gold, pk=pk)
  wished_item, created = Wishlist.objects.get_or_create(wished_item=item,  customer = request.user)
  
  if created:
    messages.info(request,'The item was added to your wishlist')
  else:
    messages.info(request,'This item is already in your wishlist')
  return redirect('wishlist')

@login_required
def remove_from_wishlist(request, pk):
    wish = get_object_or_404(Wishlist, pk=pk, customer=request.user)
    wish.delete()
    messages.success(request, "Item removed from your wishlist.")
    return redirect("wishlist")

def wishlist(request):
   wishes = Wishlist.objects.filter(customer=request.user)
   return render(request, 'wishlist.html', {'wishes':wishes})

from django.utils import translation

def product(request):
    # Force Persian (for testing or default)
    translation.activate('fa')  # <-- you can switch to 'en' for English

    products = Gold.objects.all()
    price = get_price()

    # Convert price to float safely
    try:
        price = float(str(price).replace(",", ""))
    except (ValueError, TypeError):
        price = 0

    # Render the template
    return render(request, "product.html", {
        "golds": products,
        "price": price
    })


def get_price(asset_key="geram18"):
    """
    Fetch live price for a given asset from tgju.org JSON API.
    asset_key examples: 'geram18', 'crypto-bitcoin', 'price_dollar_dt'
    """
    url = "https://call2.tgju.org/ajax.json?rev=s3qMTPiBCSjNnuDvXTQC9IBKHadLYBmN5iMv7ay5zysnqvHTDZqEFlXGI9EJ"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        current = data.get("current", {})
        asset = current.get(asset_key, {})
        return asset.get("p", "N/A")
    except Exception as e:
        return f"N/A ({e})"
# Render page for any asset
#def price_view(request, asset_key):
 #   price = get_price(asset_key)
  #  return render(request, "product.html", {"price": price, "asset_key": asset_key})



# API endpoint for AJAX refresh
def price_api(request, asset_key):
    price = get_price(asset_key)
    return JsonResponse({"price": price})
