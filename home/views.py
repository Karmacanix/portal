from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User


from .forms import  NewUserForm


UserModel = get_user_model()


# Create your views here.
def home(request):
    sitename = 'karma-base'
    context = {'sitename': sitename}
    return render( request, 'home/home.html', context)



@login_required
def account_settings(request):
    name = UserModel.get_full_name(request.user)
    context = {'name': name}
    return render( request, 'home/account.html', context)
    
    
def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NewUserForm(request.POST)
        # check the username is unique
        
        #check the passwords match
        
        # check whether it's valid:
        if form.is_valid():
            # save user
            if form.fields["email"]:
                em = form.cleaned_data.get("email")
                if form.clean_username(form.fields["username"]):
                    un = form.cleaned_data.get("username")
                    if form.clean_password2(form.fields["password1"], form.fields["password2"]):
                        pw = form.cleaned_data.get("password1")
                        user = User.objects.create_user(un, em, pw)
        
        return HttpResponseRedirect('home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewUserForm()

    return render(request, "home/signup.html", {"form": form})  

    