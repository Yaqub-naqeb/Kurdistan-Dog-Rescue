from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, Http404

# Create your views here.
def posts(request):
    posts = Post.objects.all().order_by('date')
    context = {'posts': posts}
    return render(request, 'posts_app/success_stories.html', context)

def post_detail(request, slug=None):
    post_obj = None
    if slug is not None:
        try:
            post_obj = Post.objects.get(slug=slug)
        except: raise Http404
        
    context = {
        'object': post_obj,
    }
    return render(request, 'posts_app/detail.html', context)