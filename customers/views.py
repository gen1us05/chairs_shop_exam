from django.shortcuts import render, redirect
from django.views import View
from .models import Customer


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import CustomerForm
from django.contrib.auth.hashers import make_password
from products.models import Product, Blog
from .models import Comments


class LandingPageView(View):

    def get(self, request):
        products = Product.objects.all()
        blogs = Blog.objects.all()
        comments = Comments.objects.all()
        context = {
            'products': products,
            'blogs': blogs,
            'comments': comments,
        }

        return render(request, 'main/index.html', context)





class RegisterView(View):
    def get(self, request):
        return render(request, 'form/register.html')

#     def post(self, request):
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#
#         if username and email and password:
#             if Customer.objects.filter(username=username).exists():
#                 messages.error(request, 'Username already exists')
#                 return render(request, 'form/register.html')
#             if Customer.objects.filter(email=email).exists():
#                 messages.error(request, 'Email already exists')
#                 return render(request, 'form/register.html')
#
#             user = Customer(username=username, email=email, first_name=first_name, phone=phone, last_name=last_name,
#                                password=password)
#             user.save()
#             login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return redirect('landing')
#         else:
#             messages.error(request, 'Please fill out all fields')
#             return render(request, 'accounts/register.html')

        # frist_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # username = request.POST['username']
        # email = request.POST['email']
        # phone = request.POST['phone']
        # password = request.POST['password']
        #
        # customer = Customer(frist_name=frist_name, last_name=last_name, username=username, email=email, phone=phone, password=password)
        # customer.save()
        #
        # return redirect('landing')


class LoginView(View):
    def get(self, request):
        data = AuthenticationForm()
        return render(request, 'form/login.html', {'data': data})




class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login')




