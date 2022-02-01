from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from blog.models import Post

from .serializer import PostSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.response import Response

class PostApiList(generics.ListCreateAPIView):
    """
    this view for return post as api list 

    data:
    title, slug
    """
    queryset = Post.objects.filter(slug='post')
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = Post.objects.all()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data)

