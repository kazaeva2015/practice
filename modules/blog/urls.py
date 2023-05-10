from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/', posts_list, name='posts_by_page'),
    path('posts/create/', PostCreateView.as_view(), name='posts_create'),
    path('posts/<str:slug>/update/', PostUpdateView.as_view(), name='posts_update'),
    path('posts/<str:slug>/delete/', PostDeleteView.as_view(), name='posts_delete'),
    path('posts/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('subject/<str:slug>', PostBySubjectListView.as_view(), name='posts_by_subject'),
]
