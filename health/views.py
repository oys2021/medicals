from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from health.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login/')
def home(request):
    return render(request,"health/index.html")

@login_required(login_url='/login/')
def about(request):
    return render(request,"health/about-us.html")

@login_required(login_url='/login/')
def contact(request):
    return render(request,"health/contact.html")

@login_required(login_url='/login/')
def doctors(request):
    return render(request,"health/doctors.html")

@login_required(login_url='/login/')
def department(request):
    return render(request,"health/department.html")

@login_required(login_url='/login/')
def signup(request):
    return render(request,"health/signup_index.html")


class CreatePatientView(View):
    template_name="health/signup_index.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self,request, *args, **kwargs):
        full_name= request.POST.get("full_name")
        username= request.POST.get("username")
        email= request.POST.get("email")
        password= request.POST.get("password")
        repeat_password= request.POST.get("repeat_password")
        # is_active = "on" in request.POST.get("is_active", "")
        
        if password != repeat_password:
            messages.add_message(request, messages.ERROR,
                                 "Passwords do not match.")
            return redirect("accounts:create_administrator")
        else:
            patient=CustomUser.objects.create(
               email=email, full_name=full_name,username=username
            )
            patient.is_patient=True
            patient.set_password(password)
            patient.save()
        return redirect("/")
    
# class LoginView(View):
#     template_name = "health/login.html"

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         email_address = request.POST.get("email")
#         password = request.POST.get("password")
#         remember_me = True if request.POST.get("remember_me") else False
        
#         user = authenticate(email_address=email_address, password=password)
            
#         if user:
#             login(request, user)
#             user.save()
#             # redirect_url = request.GET.get("next") or "dashboard:index"
#             return redirect("/")
#         else:
#             messages.add_message(request, messages.ERROR,
#                                  "Invalid credentials")
#             return render(request, self.template_name)
        
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = 'health/login.html'

    def post(self, request, *args, **kwargs):
        email= request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_patient==True:
            login(request, user)
            return redirect('/')
        else:
           messages.add_message(request, messages.ERROR,
                                 "Invalid credentials")
           return render(request, self.template_name)
       
       
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')


# from django.shortcuts import render, redirect
# from health.form import UserForm, ProfileForm

# @login_required(login_url='/login/')
# def profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             return redirect('profile')
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'health/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })



# def update_profile(request, pk):
#     user = CustomUser.objects.get(pk=pk)
#     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()
#     return render(request,"health/update_profile.html")

            

            

       