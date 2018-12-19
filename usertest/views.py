from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import redirect,render,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import  User
from .forms import UserForm,RegisterForm
from django.contrib.auth.hashers import make_password,check_password



def index(request):

    user = request.user.username

    return render(request,'index.html',locals())

def userlogin(request):

    if request.method =="POST":


        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username):


            user = authenticate(username=username,password=password)
            if user:

                login(request,user)
            return HttpResponseRedirect(reverse('user:index'))

        else:

            tips = '用户不存在'
    form = UserForm()
    return render(request,'login.html',locals())

def userregister(request):

    if request.method =="POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect('user:login')
        else:
            tips = form.errors
    form = RegisterForm()
    return render(request,'register.html',locals())
def usereditpassword(request):
    pass

def userlogout(request):
    logout(request)
    return redirect(reverse('user:login'))