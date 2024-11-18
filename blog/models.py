from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)
    categories = models.ManyToManyField(Category, related_name='posts')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    text = models.TextField()
    created_at = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'Comentario de {self.author} em {self.post.title}'