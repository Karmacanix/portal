from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User


from home.forms import  NewUserForm
from cart.models import ShoppingCart

UserModel = get_user_model()

def get_complete_name(request):
    if request.user.get_short_name():
        un = request.user.get_short_name()
        if request.user.get_full_name():
            un = request.user.get_full_name()
    
    else:
        un = request.user.username
            
    return un

def home(request):
    un = ''
    qs = None
    if request.user.is_authenticated:
        un = get_complete_name(request)
        if ShoppingCart.objects.filter(buyer=request.user):
            qs = ShoppingCart.objects.filter(buyer=request.user)
        
    sitename = 'karma-base'
    return render( request, 'home/home.html', {"sitename": sitename, "un" : un, "qs" : qs})



@login_required
def account_settings(request):
    return render( request, 'home/account.html', {'name': get_complete_name(request)})
    
    
def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data.get("username"), 
                email = form.cleaned_data.get("email"), 
                password = form.cleaned_data.get("password1")
            )
            user.save()
            messages.success(request, "New user created.")
            
        else:
            messages.error(request, "Invalid form.")
        
        return HttpResponseRedirect(' ')

    else:
        form = NewUserForm()

    return render(request, "home/signup.html", {"form": form})

    