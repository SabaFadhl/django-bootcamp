from django.contrib import admin

# Register your models here.

from .models import Post



@admin.action(description='Print All row on console')
def make_published(modeladmin, request, queryset):
    for i in queryset:
        print(i)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'text', 'pub_date')
    # fields = ('title', 'slug')
    read_only = ('pub_date')
    actions = [make_published]

admin.site.register(Post, PostAdmin)



