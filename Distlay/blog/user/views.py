from django.contrib.auth.backends import UserModel
from django.shortcuts import render,redirect,reverse
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm,ProfileUpdateForm
from django.core.mail import EmailMessage 
from django.template.loader import get_template



# Create your views here.


def register(request):
    
    form = RegisterForm(request.POST or None)
    if form.is_valid():
            
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            
            newUser = User(username = username,last_name = last_name,first_name = first_name,email = email)
            newUser.set_password(password)

            email_subject = 'Happy to see you in our community!'
            email = EmailMessage(
                email_subject,
                'Test Mail for Now!',
                'noreply@fosoftwareblog.com',
                [email], 
            )

            newUser.save()
            email.send(fail_silently=False)
            login(request,newUser)
            messages.success(request,"Register successfully!")

            return redirect("index")
        
    context = {
        "form" : form
        }
    return render(request,"register.html",context)



def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username = username, password = password)

        if user is None : 
            messages.info(request,"Username or password is wrong!")
            return render (request,"login.html",context)
        
        messages.success(request,"Login Successfully")
        login(request,user)
        return redirect("index")
    
    return render(request,"login.html",context)

@login_required(login_url="user:login")
def logoutUser(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("index")

@login_required(login_url="user:login")
def profileUser(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request,"Profile Updated successfully!")
            return redirect(reverse("user:profile"))

    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request,"profile.html",context)

    