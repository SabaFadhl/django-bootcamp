from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import generics
from api.models import Like

from blog.models import Post

from .serializer import PostSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.response import Response

from rest_framework.views import APIView

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


class LikePostCreate(APIView):
    """
    this view for make like for post
    """
    permission_classes = [IsAuthenticated]


    def get(self, request, **kwargs):
        """
        get request for api
        """
        post_id = None
        post = None
        # post_id = request.GET['post_id']

        
        if request.GET['post_id']:
            post_id = request.GET['post_id']
        # print(post_id)
        try:
            post = Post.objects.get(id=post_id)
            like = Like.objects.filter(post=post, user=request.user)
            if like:
                return Response({'status': False})

        except Post.DoesNotExist:
            return Response({'status': False})
        
        # print(request.GET)
        if post:
            like = Like.objects.create(post=post, user=request.user)

        return Response({'status': True})


class CheckIfLikePost(APIView):
    """
    this view for make like for post
    """
    permission_classes = [IsAuthenticated]


    def get(self, request, **kwargs):
        """
        get request for api
        """
        # post_id = None
        # post = None
        # # post_id = request.GET['post_id']

        
        # if request.GET['post_id']:
        #     post_id = request.GET['post_id']
        # # print(post_id)
        # try:
        #     post = Post.objects.get(id=post_id)
        #     like = Like.objects.filter(post=post, user=request.user)
        #     if like:
        #         return Response({'status': False})

        # except Post.DoesNotExist:
        #     return Response({'status': False})
        
        # # print(request.GET)
        # if post:
        #     like = Like.objects.create(post=post, user=request.user)

        # return Response({'status': True})