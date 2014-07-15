from django import forms
from blog.models import CommentWithTitle
from django.contrib.comments.forms import CommentDetailsForm 
from django.forms.forms import DeclarativeFieldsMetaclass

class CommentMetaclass(DeclarativeFieldsMetaclass):
    def __init__(cls, cls_name, cls_bases, dict):
        del dict['base_fields']['url']
        del dict['base_fields']['email']
        super(CommentMetaclass, cls).__init__(cls_name, cls_bases, dict)

class CommentFormWithTitle(CommentDetailsForm ):
    __metaclass__ = CommentMetaclass

    def get_comment_model(self):
        # Use our custom comment model instead of the built-in one.
        return CommentWithTitle
		
    def get_comment_create_data(self):
        self.cleaned_data['url'] = ''
        self.cleaned_data['email'] = ''
        return super(CommentFormWithTitle, self).get_comment_create_data()
		