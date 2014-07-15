from django.contrib import admin
from blog.models import BlogPost, BlogPostAdmin  


admin.site.register(BlogPost, BlogPostAdmin)