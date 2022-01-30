from django import forms

from .models import Post

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