from django.shortcuts import render, get_object_or_404 # type: ignore
from django.views import generic # type: ignore
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'blog/index.html'
    paginate_by = 6
    
def post_detail(request,  slug):
    """
    Renders the detail view of a blog post identified by its slug.
    
    **Content**
    
    ``post_detail``
        an instance of model : `blog.pot`
        
    **Template**
    
    :template:`blog/post_detail.html`
    """
    
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post}) 