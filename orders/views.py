from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.models import CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def admin_order_list(request):
    if not request.user.is_admin:
        return redirect("product_list")
    orders = Order.objects.all().order_by("-created_at")
    return render(request, "admin_panel/admin_orders.html", {"orders": orders})



def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)

    if request.method == "POST":
        order = Order.objects.create(user=request.user, total=total)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        cart_items.delete()
        return redirect("order_confirmation", order_id=order.id)

    return render(request, "orders/checkout.html", {"cart_items": cart_items, "total": total})

def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, "orders/order_confirmation.html", {"order": order})

def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "orders/order_history.html", {"orders": orders})
