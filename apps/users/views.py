from django.shortcuts import render

# Create your views here.
from  django.views import View
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,reverse

from django.contrib.auth import backends
from django.db.models import Q
from .models import UserProfile,EmailVerifyRecord

from utils.email_send import send_register_eamil
from django.contrib.auth.hashers import make_password,check_password

from django.views.generic import DetailView,ListView

from .forms import  UploadImageForm
from django.http import HttpResponse





#add email authenticated

class CustomBackend(backends.ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))

            if user.check_password(password):
                return user

        except Exception as e:
            return None




class IndexView(View):

    def get(self,request):
        user=request.user
        print(user)
        return render(request,'index.html',locals())



class LoginView(View):

    def get(self,request):

        return render(request,'login.html')
    def post(self,request):

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect(reverse('index'))
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})

def userlogout(request):

    logout(request)

    return redirect(reverse('index'))

class RegisterView(View):
    '''用户注册'''
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            UserProfile.objects.create_user(username=username,password=password,email=email)
            send_register_eamil(username)
            return redirect(reverse('login'))
        except Exception as e:
            msg = e
            return  render(request,'register.html',{'msg':msg})
class ActiveUserView(View):

    def get(self,request,active_code):
        record = EmailVerifyRecord.objects.filter(code=active_code)
        if record:
            for rc in record:
                email =  rc.email
                try:
                    user = UserProfile.objects.get(email=email)

                    user.is_active = True

                    user.save()
                except Exception :

                    return redirect(reverse('login'))
        else:
            return render(request, 'active_fail.html')
        return redirect(reverse('login'))


class ForgetView(View):
    def get(self,request):
        return render(request,'forgetpwd.html')
    def post(self,request):
        email = request.POST.get('email')
        send_register_eamil(email)
        return render(request,'send_success.html')

class RestView(View):
    def get(self,request,code):
        return render(request,'password_reset.html')
    def post(self,request,code):
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password!=password2 and password!='':
            msg='密码不一致'
            return render(request,'password_reset.html',{'msg':msg})


        else:
            record = EmailVerifyRecord.objects.filter(code=code).first()
            if record:

                email = record.email
                print(email)
                password=make_password(password)
                user = UserProfile.objects.filter(email=email).first()
                print(user)
                user.password = password
                user.save()

                return redirect(reverse('login'))
            else:
                return render(request,'active_fail.html')




class UserInfo(DetailView):
    context_object_name = 'userinfo'
    model = UserProfile
    pk_url_kwarg = 'id'
    template_name = 'user-info.html'





class UploadImageView(View):



    def post(self,request):

        image_form = UploadImageForm(request.POST)

        if image_form.is_valid():

            image = image_form.cleaned_data['image']

            request.user.image= image
            request.user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')




