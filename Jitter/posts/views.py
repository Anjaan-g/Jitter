from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm
#
# def login_view(request):
#     next = request.GET.get('next')
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect('/')
#
#     context = {
#         'form': form,
#     }
#     return render(request, "login.html",context)

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    def get_queryset(self):
        return True


class LoginView(generic.ListView):
    template_name = 'posts/login.html'

    def login_view(request):
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect('/')

        context = {
            'form': form,
        }
        return render(request, 'posts/login.html',context)


    def get_queryset(self):
        return True
