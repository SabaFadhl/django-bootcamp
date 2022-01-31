from django import forms

from .models import Post
from django.contrib.auth import authenticate

class PostForm(forms.Form):

    title = forms.CharField(label='Title', max_length=100)
    text = forms.CharField(label='Text')
    pub_date = forms.DateField(label="Publish Date")


    def save(self, id=None):
        """
        this function for save to model post
        """
        # if not id:
        title = self.cleaned_data['title']
        text = self.cleaned_data['text']
        pub_date = self.cleaned_data['pub_date']

        #rint("this is print of save method", title, text, pub_date)
        return Post.objects.create(title=title, text=text)
        


    def update(self, post=None):
        post.title = self.cleaned_data['title']
        post.text = self.cleaned_data['text']
        post.save()

    # def clean_title()


    # def update_vie



class LoginForm(forms.Form):

    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput())


  

    def authentication(self):

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        is_authentication = authenticate(username=username, password=password)

        if is_authentication:
            return is_authentication
        return None

        # return is_authentication

