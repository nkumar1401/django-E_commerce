from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm  

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("product_list")  # redirect after successful login
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


# Register view
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            return redirect("product_list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
