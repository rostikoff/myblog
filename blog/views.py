from blog.models import BlogPost 
from django.views.generic import ListView, DetailView
from django.template import loader, Context 
from django.http import HttpResponse 
from django.core.context_processors import csrf
from django.contrib.comments.models import Comment

class PostsListView(ListView): 
    model = BlogPost         
    paginate_by=10
    template_name = 'blog/post_list.html'
	
class PostDetailView(DetailView): 
    model = BlogPost
    template_name = 'blog/post_detail.html'          

