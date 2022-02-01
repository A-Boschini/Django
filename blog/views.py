from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import View
from .forms import PostCreateForm

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context={
          }
        return render(request, 'blog_list.html', context)
    
    class BlogCreateView(View):
        def get(self, request,*args, **kwargs):
            context={
            }
            return render(request, 'blog_create.html', context)
        
        def post(self, request, *args, **kwargs):
           context={
           }
           return render(request, 'blog_create.html', context)    