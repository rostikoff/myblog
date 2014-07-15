from django.db import models
from django.contrib import admin
from django.contrib.comments.models import Comment 

class BlogPost(models.Model):
    title = models.CharField(max_length=255)  	
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("-timestamp",)
	
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

class BlogPostAdmin(admin.ModelAdmin):   
    list_display = ("title", "id", "timestamp")

class CommentWithTitle(Comment):
    title = models.CharField(max_length=300)