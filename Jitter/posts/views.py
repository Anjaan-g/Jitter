from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm
from django.views.generic.edit import FormView


class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    def get_queryset(self):
        return True


class LoginView(FormView):
    template_name = 'posts/login.html'
    form_class = UserLoginForm
    success_url = ''
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
            return redirect('')

        form.clean()
        return super().form_valid(form)




class RegisterView(FormView):
    template_name = 'posts/signup.html'
    form_class = UserRegisterForm
    success_url = 'posts/index.html'
    def register_view(request):
        # next = request.GET.get('next')
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            # if next:
            #     return redirect(next)
            return redirect('')

        form.clean()
        return super().form_valid(form)

class LogoutView(generic.ListView):
    template_name = 'posts/index.html'

    def logout_view(request):
        logout(request)
        return redirect('')

    def get_queryset(self):
        return True
