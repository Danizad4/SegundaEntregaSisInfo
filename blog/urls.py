from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.list_post, name='listpost'),
    path('<int:pk>/', views.detail_post, name='detailpost'),
    path('search/', views.search_post, name='searchpost'),
    path('create/', views.create_post, name='createpost'),
    path('<int:pk>/update/', views.update_post, name='updatepost'),
    path('<int:pk>/delete/', views.delete_post, name='deletepost'),
]
