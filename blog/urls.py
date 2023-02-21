from django.urls import path
from .views import (
BlogListView,
BlogDetailView,
CreatNewBlog,
UpdateBlog,
DeletePost,
)

urlpatterns = [
    path('post/<int:pk>/delete/',DeletePost.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/',UpdateBlog.as_view(), name='post_edit'),
    path('post/new/', CreatNewBlog.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(),name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    ]
