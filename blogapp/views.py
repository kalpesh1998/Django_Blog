from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post

from .forms import *


# Create your views here.

class PostList(generic.ListView):
    #queryset = Post.objects.filter(status=1).order_by('created_on')
    queryset = Post.objects.filter(status=1).order_by('title')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'