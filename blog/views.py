from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def index(request):
    return render(request, 'staticpages/index.html')

def homepage (request):
    posts = Post.objects.all()
    return render (request, 'blog/base.html', {'posts': posts})

def detail_post(request, pk):
    post = get_object_or_404(Post, id = pk)
    return render(request, 'blog/detailpost.html', {'post': post})

def search_post(request):
    query = request.GET.get('q', '')
    print(f"Buscando por: {query}")
    posts = Post.objects.filter(title__icontains=query) if query else []
    return render(request, 'blog/searchpost.html', {'posts': posts, 'query': query})

def list_post(request):
    posts = Post.objects.all()
    return render(request, 'blog/listpost.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title') 
        content = request.POST.get('content')  
        if title and content:  
            Post.objects.create(title=title, content=content)   
            return redirect('blog:listpost')  
    return render(request, 'blog/creatpost.html') 

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:  
            post.title = title
            post.content = content
            post.save()
            return redirect('blog:listpost')
    return render(request, 'blog/updatepost.html', {'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:listpost')
    return render(request, 'blog/deletepost.html', {'post': post})




# Create your views here.
