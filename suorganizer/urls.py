"""suorganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import list_blog, post_details, create_post, PostList, LoginView, user_profile, logout_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post-list/', PostList.as_view(), name='post-list'),

    path('list-blog/', list_blog, name='list-blog'),
    path('post/<int:id>', post_details, name="post-details"),
    path('create-post/', create_post, name='create-post'),
    path('update-post/<int:id>', create_post, name='update-post'),
    path('delete-post/<int:id>', create_post, name='delete-post'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-info/', user_profile, name='user-info'),
    path('logout/', logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls'))
    # path('account/', include("account.urls")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
