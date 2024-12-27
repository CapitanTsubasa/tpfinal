from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Post

class HomeView(TemplateView):
    template_name = 'home.html'

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
