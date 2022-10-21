import email
from email.mime import image
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    image= models.ImageField()

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title= models.CharField(max_length=200)
    body = models.TextField(null= True,unique=True)
    author= models.ForeignKey(User,on_delete= models.CASCADE, )
    image= models.ImageField(null= True)
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.body[0:200]
    
    class  Meta:
        ordering=['-updated', '-created']


class Comments(models.Model):
    post= models.ForeignKey(Post, on_delete=models.SET_NULL, null=True )
    name= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    body=models.TextField()


    def __str__(self):
            return self.body[0:50]
        

