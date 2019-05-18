from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy




class IndexView(generic.TemplateView):
    template_name = 'posts/index.html'
    def get_queryset(self):
        return True
    def blog_post_list_view(request):
        #list out objects
        #All at a same time
        qs = Post.objects.all()
        if request.user.is_authenticated:
            my_qs = Post.objects.filter(user = request.user)
            qs = (qs | my_qs).distinct()

        context = {'object_list': qs}
        return render(request, template_name, context)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'posts/signup.html'
