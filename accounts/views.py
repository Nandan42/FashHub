from django.shortcuts import render,redirect,reverse,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import ProfileForm,UserForm
from .models import Profile



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        birth_date = request.POST['birth_date']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username,email=email,password=password1)
        user.save()
        profile = Profile.objects.get(user=user)
        profile.phone_number=phone_number
        profile.birth_date=birth_date
        profile.save()
        print("user created")
        return redirect('/accounts/login')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print('login successful')
            return redirect('/')
        else:
            print("wrong credentials")
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    print("logged out")
    return redirect('/')