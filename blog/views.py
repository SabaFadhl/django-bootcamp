from django.shortcuts import render

from django.http import HttpResponse

from .models import Post


from .forms import PostForm
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

    



def create_post(request):
    form = PostForm()
    context = {
        'form': form
    }
    template_name = 'blog/create_post.html'


    return render(request, template_name, context)