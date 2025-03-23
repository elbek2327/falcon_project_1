from urllib import request

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from django.core.mail import send_mail
from users.forms import LoginForm, RegisterForm
from users.models import CustomUser
# Create your views here.

# def login_page(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, email=cd['email'], password=cd['password'])
#             if user:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('shop:index')
#                 else:
#                     messages.error(request, 'Disabled account')
#             else:
#                 messages.error(request, 'Invalid email or password')
#
#     return render(request, 'users/simple/login.html', {'form': form})
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/simple/login.html'
    success_url = reverse_lazy('shop:index')
    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(self.request, user)
                messages.success(self.request, 'You are now logged in.')
                return super().form_valid(form)
            else:
                messages.error(self.request, 'You are not authorized to log in.')
        else:
            messages.error(self.request, 'Invalid email or password.')
        return self.form_invalid(form)




# def register_page(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = CustomUser.objects.create(
#                 email=form.cleaned_data['email'],
#                 first_name=form.cleaned_data['name'],
#                 password=form.cleaned_data['password'],
#             )
#             user.save()
#             messages.success(request, 'Registration successful. Please login.')
#             return redirect('users:login_page')
#
#     return render(request, 'users/simple/register.html', {'form': form})

class RegisterView(FormView):
    template_name = 'users/simple/register.html'
    success_url = reverse_lazy('users:login_page')
    form_class = RegisterForm

    def form_valid(self, form):
        user = CustomUser.objects.create_user(
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['name'],
            password=form.cleaned_data['password']
        )
        user.save()
        messages.success(self.request, "Registration successful. Please login.")
        send_mail(
            'Hello Dear!',
            'You Successfully registered',
            'zubaydullayev1609@gmail.com',
            [user.email],
            fail_silently=False
        )
        return super().form_valid(form)

class LogoutView(RedirectView):
    url = reverse_lazy('shop:index')

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return super().get(request, *args, **kwargs)