from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def blog_post_list_view(request):
    #list out objects
    #All at a same time
    qs = Post.objects.all().published()
    if request.user.is_authenticated:
        my_qs = Post.objects.filter(user = request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'posts/index.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


class IndexView(generic.TemplateView):
    template_name = 'posts/index.html'
    def get_queryset(self):
        return True

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'posts/signup.html'
# class LoginView(FormView):
#     template_name = 'posts/login.html'
#     form_class = UserLoginForm
#     success_url = '../'
#     def login_view(request):
#         next = request.GET.get('next')
#         form = UserLoginForm(request.POST or None)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             if next:
#                 return redirect(next)
#             return redirect('')
#
#         form.clean()
#         return super().form_valid(form)
#
#
#
#
# class RegisterView(FormView):
#     template_name = 'posts/signup.html'
#     form_class = UserRegisterForm
#     success_url = '../'
#     def register_view(request):
#         # next = request.GET.get('next')
#         form = UserRegisterForm(request.POST or None)
#         if form.is_valid():
#             user = form.save(commit=False)
#             password = form.cleaned_data('password')
#             password2 = form.cleaned_data('password2')
#             user.set_password(password)
#             user.save()
#             new_user = authenticate(username=user.username, password=password)
#             login(request, new_user)
#             # if next:
#             #     return redirect(next)
#             return redirect(success_url)
#
#         form.clean()
#         return super().form_valid(form)
#
# class LogoutView(generic.ListView):
#     template_name = 'posts/index.html'
#
#     def logout_view(request):
#         logout(request)
#         return redirect('')
#
#     def get_queryset(self):
#         return True
