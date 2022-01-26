from django.db import models

# Create your models here.


class Post(models.Model):
    """
    test Post for b blog app
    """
    title = models.CharField(max_length=63)
    slug = models.SlugField(null=True)
    text = models.TextField(null=True)
    pub_date = models.DateField(null=True)



    def __str__(self):
        return self.title

