from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from taggit.managers import  TaggableManager

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=50, verbose_name="Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created Date")
    slug = models.SlugField(unique=True,max_length=100, default=None)
    tags = TaggableManager()
    article_image = models.FileField(blank = True, null = True, verbose_name = "Upload Image")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE, verbose_name = "Article",related_name="comments")
    comment_title = models.CharField(max_length=30, verbose_name = "Title", default=None)
    comment_author = models.ForeignKey(User,on_delete= models.CASCADE, verbose_name='User')
    comment_content = models.CharField(max_length=200,verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.comment_content
    
    class Meta:
        ordering = ['-comment_date']
    
