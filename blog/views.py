from django.shortcuts import render

from django.http import HttpResponse

from .models import Post

# Create your views here.

def list_blog(request):
    """
    this is simple view
    """
    template_name = 'blog/list.html'
    # html = "<html"
    posts = Post.objects.all()
    # print(posts)
    context = {"name": "ibrahim2",
    
    "posts": posts}

    return render(request, template_name, context)

