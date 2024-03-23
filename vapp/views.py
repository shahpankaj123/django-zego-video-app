from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from vapp.forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def Login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        myuser = authenticate(username=username,password=password)
        if myuser is not None:
         login(request,myuser)
         return redirect('home')
        else:
          messages.warning(request,"Password or Username donot match")   
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully")
            return redirect('Login')
        else:
           error=form.errors.as_text()
           messages.warning(request,error)
           return redirect('signup')       
    return render(request,'signup.html')

def Logout(request):
   logout(request)
   return redirect('Login')

@login_required(login_url='login.html')
def home(request):
   return render(request,'home.html')

@login_required(login_url='login.html')
def videomeet(request):
   return render(request,'video.html',{'username':request.user.first_name})

@login_required(login_url='login.html')
def joinmeet(request):
   if request.method == 'POST':
      number=request.POST['number']
      print(number)
      return redirect("/join?roomID="+number)  
   return render(request,'joinvideo.html')
