from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView, DetailView
class BlogListView(ListView):
    template_name = 'home.html'
    model = Post
class BlogDetailView(DetailView):
    model= Post
    template_name = 'post_details.html'