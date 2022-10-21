from tkinter import Y
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from .models import Post, Category, Comments
from .form import PostForm, CommentsForm
from django.contrib.auth.decorators import login_required




# def Cool(request):
#     category= Category.objects.all()


#     context={'category': category}
#     render(request, 'base.html', context)



def Page(request):
    # all_post =  Post.objects.get(id=pk)
    # roar = iter(all_post)
    
    # def post_loop(roar):
    #     for x in roar:
    #         y= all_post.next()
    #         return(x,y)

    q= request.GET.get('q') if request.GET.get('q') != None else ''

    post= Post.objects.filter(category__name__icontains=q)
    
    category= Category.objects.all()

    context= {'post':post, 'category':category, }
    return render(request, 'blog/home.html', context)


def postRoom(request, pk):
    
    
    room = Post.objects.get(id=pk)
    new_comments= room.comments_set.all().order_by('-created')
    form = CommentsForm()

    if request.method == 'POST':
        form= CommentsForm(request.POST)
        Comments.objects.create(
            post= room,
            name= request.POST.get('name'),
            email= request.POST.get('email'),
            body= request.POST.get('comment'),
        )
        return redirect('post-details',pk=room.id)

    context= {'room':room, 'new_comments':new_comments, 'form':form}
    return render(request, 'blog/room.html' , context)



@login_required(login_url='login')
def createRoom(request):
    form= PostForm()
    if request.method =='POST':
        form= PostForm(request.POST, request.FILES)


        if form.is_valid():
            post= form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')

    context= {'form':form}
    return render(request, 'blog/create-post.html', context)



@login_required(login_url='login')
def  editRoom(request, pk):
    post= Post.objects.get(id=pk)
    form= PostForm(instance=post)


    if request.method=='POST':
        form= PostForm(request.POST,request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form, 'post':post}
    return render(request, 'blog/create-post.html', context)



def pageLogin(request):
    if request.method== 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.error(request, 'you are not allowed to be here')
        

    context={}
    return render(request, 'blog/login.html', context)
    

def pageLogout(request):
    logout(request)
    return redirect('home')

def pageDelete(request, pk):
    post=Post.objects.get(id=pk)

    if request.method=='POST':
        post.delete()
        return redirect('post-details', pk=post.id)

    context={}
    return render(request, 'blog/delete.html', context)


    b= iter(a)
    for x in b:
        y= b.next()
        print(x,y)

    b= iter(a)
    for x,y in ((item, b.next()) for item in b):
        print(x,y)