from statistics import mode
from django.db import models

# Create your models here.

from blog.models import Post
from django.contrib.auth.models import User


class Like(models.Model):
    """
    this class model for post link is connect post id with user
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['post', 'user']]


    def __str__(self):
        return self.user.username + ' ' +str(self.post.title)


class Comments(models.Model):
    """
    this class for model comments for post
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
