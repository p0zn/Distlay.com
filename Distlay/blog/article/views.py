from django.shortcuts import redirect, render,HttpResponse,get_object_or_404,reverse
from ask.models import Questions
from .forms import ArticleForm
from django.contrib import messages
from .models import Article as Article,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from taggit.models import Tag
from django.core.paginator import Paginator


# Create your views here.

@login_required(login_url="user:login")
def articles(request):

    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles": articles})

    articles = Article.objects.all()
    paginator = Paginator(articles,2)

    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    return render(request,"articles.html",{"articles": page_obj.object_list,"page_obj":page_obj,"page_number":int(page_number)})

def index(request):
    context = {
        
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author =request.user)
    questions = Questions.objects.filter(author=request.user)
    context = {

        "articles" : articles,
        "questions" : questions

    }
    
    return render(request,"dashboard.html",context)
    
@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    common_tags = Questions.tags.most_common()[:12]

    if form.is_valid():
        article = form.save(commit = False)
        article.slug = slugify(article.title)
        article.author = request.user
        article.save()
        form.save_m2m()

        messages.success(request,"Article created successfully!")
        return redirect("article:dashboard")


    context = {
        "form" : form,
        "common_tags" : common_tags,
    }
    return render(request,"addarticle.html",context)

def tagged(request,slug):
    tag = get_object_or_404(Tag, slug=slug)
    articles = Article.objects.filter(tags=tag)

    context = {
        "tag" : tag,
        "articles" : articles,
    }

    return render(request,"articles.html",context)

def tag_detail(request,slug):
    article = get_object_or_404(Article,slug=slug)
    return render(request,"articles.html",{"article":article})
    
@login_required(login_url="user:login")
def detail(request,id):
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()
   

    return render(request,"detail.html",{"article":article,"comments":comments,})

@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()

        messages.success(request,"Article updated successfully!")
        return redirect("article:dashboard")

    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()

    messages.success(request,"Article deleted successfully!")

    return redirect("article:dashboard")


def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_title = request.POST.get('comment_title')
        comment_content = request.POST.get('comment_content')
        comment_author = request.user

        newComment = Comment(comment_title = comment_title, comment_content = comment_content, comment_author = comment_author)

        newComment.article = article

        newComment.save()

    return redirect(reverse("article:detail",kwargs={"id":str(id)}))
