from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from taggit.managers import  TaggableManager
from django.urls import reverse


# Create your models here.

class Questions(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE, verbose_name='Question Author')
    title = models.CharField(max_length=50, verbose_name="Question Title")
    content = RichTextField()
    asked_date = models.DateTimeField(auto_now_add=True,verbose_name="Asked Date")
    slug = models.SlugField(unique=True,max_length=100, default=None)
    tags = TaggableManager()
    question_image = models.FileField(blank=True,null=True,verbose_name="Upload Image")
 

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-asked_date']


class Answers(models.Model):
    question  = models.ForeignKey(Questions,on_delete=models.CASCADE, verbose_name = "Question", related_name = "answers")
    answer_author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="User")
    answer_content = RichTextField(max_length=200,verbose_name="Answer", null=True)
    answer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) : 
        return self.answer_content
    
    class Meta:
        ordering = ["-answer_date"]


class Report(models.Model):
    reason = models.CharField(max_length=255, verbose_name="Select reason for reporting")
    message = models.CharField(max_length=255, verbose_name="Message")

    def __str__(self):
        return self.reason

    def get_absolute_url(self):
        return reverse("questions")
    