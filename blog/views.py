from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content'] 

def index(request):
    return render(request, 'staticpages/index.html')

def homepage(request):
    posts = Post.objects.all()
    return render(request, 'blog/base.html', {'posts': posts})


def detail_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detailpost.html', {'post': post})


def search_post(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(title__icontains=query) if query else []
    return render(request, 'blog/searchpost.html', {'posts': posts, 'query': query})


def list_post(request):
    posts = Post.objects.all()
    return render(request, 'blog/listpost.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():              
            form.save()  
            return redirect('blog:listpost')  
    else:
        form = PostForm() 

    return render(request, 'blog/creatpost.html', {'form': form})


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  
        if form.is_valid():
            form.save()
            return redirect('blog:listpost')
    else:
        form = PostForm(instance=post)  

    return render(request, 'blog/updatepost.html', {'form': form, 'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        post.delete()
        return redirect('blog:listpost')
    
    return render(request, 'blog/deletepost.html', {'post': post})




