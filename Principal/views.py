from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from .forms import *
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
import logging



# Crearemos nuestras vistas de cada función.
@login_required
def index(request):
    return render(request, 'Principal/index.html')

@login_required
def aboutme(request):
    return render(request, 'Principal/aboutme.html')

@login_required
def profile_view(request):
    return render(request, 'Principal/profile.html')

@login_required
def createblog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            if 'image' in request.FILES:
                image_file = request.FILES['image']
                createblog = Blog(title=form.cleaned_data['title'],
                                subtitle=form.cleaned_data['subtitle'],
                                body=form.cleaned_data['body'],
                                author=form.cleaned_data['author'],
                                image=image_file)
                createblog.save()  
                return render(request,'Principal/success.html')
    
    else:
        form = BlogForm()

    return render(request, 'Principal/createblog.html', {'form':form})

@login_required
def success(request):
    return render(request, 'Principal/success.html')

def readblog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs, 'user':request.user} 
    return render(request, 'Principal/blog.html', context)

#def __str__(self):
#       return f'Title: {self.title}\n Subtitle: {self.subtitle}\n Body: {self.body}\n Author: {self.author}\n Date: {self.date}\n Image: {self.image}'   

logger = logging.getLogger(__name__)

def is_superuser(user):
    logger.debug(f'Checking user {user} for superuser status')
    return user.is_superuser

@user_passes_test(is_superuser)
def blogDelete(request, blog_author):
    blog = get_object_or_404(Blog, author=blog_author)
    blog.delete()

    blogs = Blog.objects.all()

    context = {'blogs': blogs}

    return render(request, 'Principal/delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def blogUpdate(request, blog_author):
    blog = get_object_or_404(Blog, author=blog_author)

    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data
            
            blog.title = form_data['title']
            blog.subtitle = form_data['subtitle']
            blog.body = form_data['body']
            blog.author = form_data['author']

            blog.save()
            return render(request, 'Principal/index.html')
        
    else:
        form = BlogForm(initial={
            'title': blog.title,
            'subtitle': blog.subtitle,
            'body': blog.body,
            'author': blog.author
        })

    return render(request, 'Principal/updateblog.html', {'form': form, 'blog_author': blog_author})


class BlogDetail(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'Principal/detailblog.html'