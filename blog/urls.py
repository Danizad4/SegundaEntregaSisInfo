from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, add_comment

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', PostListView.as_view(), name='listpost'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detailpost'),
    path('post/create/', PostCreateView.as_view(), name='creatpost'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='updatepost'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='deletepost'),
    path('post/<int:pk>/comment/', add_comment, name='addcomment'),
    path('admin/', admin.site.urls), 
]
