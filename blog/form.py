from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Post, Comments


class PostForm(ModelForm):
    class Meta:
        model= Post
        fields = "__all__"
        exclude= ['author']

class CommentsForm(ModelForm):
    class Meta:
        model= Comments
        fields= '__all__'


