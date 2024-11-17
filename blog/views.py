from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, CommentForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/listpost.html'
    context_object_name = 'posts'  

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detailpost.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context


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

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user 
            comment.save()
            return redirect('blog:detailpost', pk=post.pk)
    return redirect('blog:detailpost', pk=post.pk)