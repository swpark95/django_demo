from django.urls import URLPattern, path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index),
    path('post-write/', views.post_write, name="write"),
    path('blog-home/', views.blog_home, name='home'),
    path('post-detail/<int:post_id>/', views.post_detail, name='detail'),
    path('post-edit/<int:post_id>/', views.post_update, name = "edit"),
    path('post-delete/<int:post_id>/', views.post_delete, name = "delete"),
]