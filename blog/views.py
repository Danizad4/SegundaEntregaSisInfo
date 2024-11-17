from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/listpost.html'
    context_object_name = 'posts'  

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detailpost.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'blog/creatpost.html'
    success_url = reverse_lazy('blog:listpost')  


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm  
    template_name = 'blog/updatepost.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:listpost')  


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/deletepost.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:listpost')
    
def index(request):
    return render(request, 'staticpages/index.html')