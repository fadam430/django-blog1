from django.shortcuts import render # type: ignore
from django.views import generic # type: ignore
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/post_list.html"