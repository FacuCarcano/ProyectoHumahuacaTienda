from django.shortcuts import render, HttpResponse
from BlogApp.models import Post, Categoria
# Create your views here.

def blog(request):
    variable_posts = Post.objects.all()
    return render(request, "blog/blog.html", {"variable_posts" : variable_posts})