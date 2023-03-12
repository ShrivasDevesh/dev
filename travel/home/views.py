# from os import login_tty
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate, login
# Create your views here.
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/home")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request,"login.html")

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/") 
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")
def about(request):
   if request.user.is_anonymous:
       return redirect("/")
   return render(request,'About.html')
def Services(request):
    if request.user.is_anonymous:
        return redirect("/") 
    return render(request,'Services.html')
def contact(request):
    if request.user.is_anonymous:
        return redirect("/") 
    return render(request,'contact.html')
def Course(request):
    if request.user.is_anonymous:
        return redirect("/") 
    return render(request,'Course.html')
def upload(request):
    if request.user.is_anonymous:
        return redirect("/") 
    return render(request,'upload.html')
def Dbms(request):
    if request.user.is_anonymous:
        return redirect("/") 
    return render(request,'Dbms.html')
def texRec(request):
    if request.user.is_anonymous:
        return redirect("/") 
    return render(request,'texRec.html')

