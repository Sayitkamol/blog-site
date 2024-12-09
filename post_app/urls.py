from django.urls import path
from .views import getPosts,getPost, getPostsByTags, about

urlpatterns = [
    path('', getPosts, name='post_all'),
    path('detail/<pk>/', getPost, name='post_detail'),
    path('filter/<str:tagname>/', getPostsByTags, name='post_filter'),
    path('about/', about, name='about_me'),
]