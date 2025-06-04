from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product, CartItem, PurchaseRecord, PurchaseItem
from django.utils import timezone
from django.db import transaction

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:product_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'shop/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, '您已成功登出')
        return redirect('shop:product_list')
    return redirect('shop:product_list')

def hello(request):
    return render(request ,'shop/hello.html')

# @login_required
def product_list(request):
    products = Product.objects.all()
    cart_items = []  # Initialize cart_items as empty list
    cart_total = 0
    shipping = 0
    total = 0

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        cart_total = sum(item.product.price * item.quantity for item in cart_items)
        shipping = 100 if cart_total < 1000 and cart_total > 0 else 0
        total = cart_total + shipping

    return render(request, 'shop/product_list.html', {
        'products': products,
        'cart_items': cart_items,
        'cart_total': cart_total,
        'shipping': shipping,
        'total': total,
    })
    
@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if created:
            cart_item.quantity = quantity # Set quantity if item is newly created
        else:
            cart_item.quantity += quantity # Add quantity if item already exists
        cart_item.save()
    return redirect('shop:product_list')

def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = CartItem.objects.get(user=request.user, product_id=product_id)
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('shop:product_list')

@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('shop:product_list')

def remove_from_cart(request, product_id):
    CartItem.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect('shop:product_list')

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    for item in cart_items:
        item.subtotal = item.product.price * item.quantity
    cart_total = sum(item.subtotal for item in cart_items)
    shipping = 100 if cart_total < 1000 and cart_total > 0 else 0
    total = cart_total + shipping
    if request.method == 'POST' and cart_items.exists():
        with transaction.atomic():
            record = PurchaseRecord.objects.create(user=request.user, total_price=total)
            for item in cart_items:
                PurchaseItem.objects.create(
                    purchase=record,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
            cart_items.delete()
        return redirect('shop:history')
    return render(request, 'shop/checkout.html', {'cart_items': cart_items, 'cart_total': cart_total, 'shipping': shipping, 'total': total})

def product_detail(request ,product_id):
    product = Product.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    return render(request, 'shop/product_detail.html', {'product': product, 'quantity': quantity})

@login_required
def history(request):
    records = PurchaseRecord.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/history.html', {'records': records})
