from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
class BlogListView(ListView):
    template_name = 'home.html'
    model = Post
class BlogDetailView(DetailView):
    model= Post
    template_name = 'post_details.html'
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
class BlogUpdateView(UpdateView):
    template_name = 'post_edit.html'
    model = Post
    fields =['title', 'body']
class BlogDeleteView(DeleteView):
    template_name= 'post_delete.html'
    model = Post
    success_url = reverse_lazy('home')