from django.db import models

# Create your models here.

class Tag(models.Model):
    """
    this tag in organizer model test
    """
    name = models.CharField(max_length=64)
    slug = models.SlugField()



class Startup(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()
    description = models.TextField()
    founded_date = models.DateField()
    contact = models.EmailField()
    website = models.URLField()




class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField()
    link = models.URLField()
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, null=True)