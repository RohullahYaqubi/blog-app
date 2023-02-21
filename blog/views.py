from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class CreatNewBlog(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['titel', 'body', 'auther']

class UpdateBlog(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['titel', 'body']

class DeletePost(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')