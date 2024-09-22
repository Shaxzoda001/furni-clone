from decimal import Decimal

from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import CartItem, Cart, Shop


def cart(request):
    try:
        cart = Cart.objects.get(session_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        total = quantity = 0
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity
        tax = (total * 2) / 100
        gen_total = total + tax
        context = {
            'cart_items': cart_items,
            'cart_total': total,
            'quantity': quantity,
            'tax': tax,
            'gen_total': gen_total
        }
        return render(request, 'cart.html', context)
    except ObjectDoesNotExist:
        return render(request, 'cart.html', {"cart_items": [], "total": 0, "quantity": 0})


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = get_object_or_404(Shop, id=product_id)
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    cart, created = Cart.objects.get_or_create(session_id=session_id)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1, 'price': Decimal(product.price)}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.price = Decimal(product.price) * cart_item.quantity

    cart_item.save()
    return redirect('cart')


def sub_cart(request, product_id):
    cart = Cart.objects.get(session_id=_cart_id(request))
    product = get_object_or_404(Shop, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(session_id=_cart_id(request))
    product = get_object_or_404(Shop, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart')


def error(request):
    return render(request, 'error.html')


def checkout(request):
    return render(request, 'checkout.html')