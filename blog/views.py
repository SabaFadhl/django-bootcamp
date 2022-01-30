# from turtle import title
from django.forms import forms
from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Post


from .forms import PostForm
# Create your views here.

from django.views.generic import ListView, DetailView


class PostList(ListView):
    """
    this is list view for post useing genric list view
    """
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/list.html'


class PostDetails(DetailView):
    """
    this is details view for     
    """
    model = Post
    context_object_name = 'post'
    template_name = 'blog/list.html'



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




def post_details(request, id):
    """
    this is post detail page show post model
    """
    context = {}
    try:
       post = Post.objects.get(id=id)
       context['post'] = post
    except Post.DoesNotExist:
        context['error'] = "Not found"
    
    template_name = 'blog/post_details.html'

    return render(request, template_name, context)

    



def create_post(request, id=None):
    form = PostForm
    
    template_name = 'blog/create_post.html'

    post = None
    if id:
        try:

            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            # return redirect('', permanent=False)
            pass
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if not id:
                form.save()
            else:
                form.update(post)
            # return redirect('')
        print(form.errors)
        print(request.POST)
        context = {
            'form': form
        }

        return redirect('post-list', permanent=False)
        # return render(request, template_name, context)
        

    
    context = {
            'form': PostForm()
        }
    if id:
        context = {
             'form': PostForm({"title": post.title, "text": post.text})
        }
    return render(request, template_name, context)

