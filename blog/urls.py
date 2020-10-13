from django.urls import path
from . import views

# 视图函数命名空间
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    # url: <网站域名>/posts/id/
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]