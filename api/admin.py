from django.contrib import admin

# Register your models here.
from .models import Like, Comments


admin.site.register(Like)
admin.site.register(Comments)
