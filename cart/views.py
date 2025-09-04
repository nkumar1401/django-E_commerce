from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import CartItem

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, "cart/cart.html", {"cart_items": cart_items, "total": total})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get("quantity", 1))
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, product=product
    )
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    return redirect("cart")

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id, user=request.user)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect("cart")

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id, user=request.user)
    cart_item.delete()
    return redirect("cart")
