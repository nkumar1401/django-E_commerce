from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm


from .models import Product
# Create your views here.

@login_required
def admin_product_list(request):
    if not request.user.is_admin:
        return redirect("product_list")
    products = Product.objects.all()
    return render(request, "admin_panel/admin_products.html", {"products": products})

@login_required
def admin_product_create(request):
    if not request.user.is_admin:
        return redirect("product_list")
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect("admin_products")
    else:
        form = ProductForm()
    return render(request, "admin_panel/admin_product_form.html", {"form": form})







def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})

@login_required
def product_create(request):
    if not request.user.is_admin:
        return redirect("product_list")
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "products/product_form.html", {"form": form})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not (request.user.is_admin or request.user == product.created_by):
        return redirect("product_list")

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail", pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, "products/product_form.html", {"form": form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.is_admin or request.user == product.created_by:
        product.delete()
    return redirect("product_list")
