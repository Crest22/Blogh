from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('',views.Page, name='home'),

    path('blog-post/<str:pk>/', views.postRoom, name= 'post-details'),

    path('create-post/', views.createRoom, name= 'create-post'),
    path('edit-post/<str:pk>/', views.editRoom, name= 'edit-post'),
    path('delete-post/<str:pk>/', views.pageDelete, name='delete-post'),

    path('login/', views.pageLogin, name='login'),
    path('logout', views.pageLogout, name='logout'),
    
]
