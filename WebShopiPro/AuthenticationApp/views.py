from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse,get_object_or_404
from django.contrib.auth import login, logout
from .import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from .import models
from WebShopiApp.models import ProductsOfWebShopi


import requests


def webshopi_registerpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            return render(
                request,
                "AuthenticationApp/register.html",
                {"error": "Password does not match"},
            )
        filteruser= User.objects.filter(username=username)
        if filteruser.exists():
            messages.info(request, "Username already registered!")
            return redirect('/register/')

        if (
            username
            and email
            and first_name
            and last_name
            and password
        ):
        
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            messages.info(request,"Welcome to WebShopi! Account created succesfully")
            login(request, user)
            return redirect("index")

    return render(request, "AuthenticationApp/register.html")




class UserCustomLogin(LoginView):
    template_name='AuthenticationApp/login.html'



@login_required
def profile(request):
    # response = requests.get("https://fakestoreapi.com/products?limit=5")  
    # products = []
    # if response.status_code == 200:
    #     products = response.json()

    fetch_user_data= models.Profile.objects.all()

    context = {
        "user": request.user,
    }
    return render(request, "AuthenticationApp/profile.html", context)   



def logoutview(request):
    logout(request)

    return HttpResponse(f"ThankYou {{request.user}}")

    return redirect ('AuthenticationApp/login.html')  




def profile_view(request):
    # Get product IDs from session
    product_ids = request.session.get('recently_viewed', [])
    # Fetch products from DB
    products = ProductsOfWebShopi.objects.filter(pk__in=product_ids)

    # Keep order same as session
    products = sorted(products, key=lambda x: product_ids.index(x.pk))

    # You can also pass other user info for your profile
    context = {
        'products': products,
        'user': request.user
    }
    return render(request, "AuthenticationApp/profile.html", context)

  




def change_password(request):
    if request.method == 'POST':
        form = forms.CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,'Your password are successfully changed you can go know for the new password')
            return redirect('profile')
        
        else:
            messages.error(request, 'Password not changed corrrect the error firts!')
    else:
        form = forms.CustomPasswordChangeForm(request.user)

    return render (request, 'AuthenticationApp/changepass.html',{
        'form': form
    })            

            





def webshopicart(request):
    pass