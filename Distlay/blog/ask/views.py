from django.contrib.messages.api import success
from django.db.models import fields
from django.shortcuts import render
from django.utils.text import slugify
from .forms import QuestionsForm, ReportForm
from django.contrib import messages
from .models import Answers,Report, Questions as Questions
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator
from django.views.generic import CreateView


@login_required(login_url="user:login")
def questions(request):
    keyword = request.GET.get('keyword')

    if keyword:
        questions = Questions.objects.filter(title__contains = keyword)
        return render(request,"questions.html",{"questions":questions})
    
    questions = Questions.objects.all()
    paginator = Paginator(questions,4)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    

    return render(request,"questions.html",{"questions":page_obj.object_list,"page_obj":page_obj,"page_number":int(page_number)})

@login_required(login_url="user:login")
def addQuestion(request):
    form = QuestionsForm(request.POST or None, request.FILES or None)

    common_tags = Questions.tags.most_common()[:12]
    
    if form.is_valid():
        question = form.save(commit=False)
        question.slug = slugify(question.title)
        question.author = request.user
        question.save()
        form.save_m2m()

        messages.success(request,"Question Asked successfully!")
        return redirect("article:dashboard")
    
    context = {
        "form" : form,
        "common_tags" : common_tags,
    }
    return render(request,"addquestion.html",context)

@login_required(login_url="user:login")
def tagged(request,slug):
    tag = get_object_or_404(Tag, slug=slug)
    questions = Questions.objects.filter(tags=tag)
    context = {
        "tag" : tag,
        "questions" : questions,
    }
    return render(request,"questions.html",context)

@login_required(login_url="user:login")
def detail(request,id):
    question = get_object_or_404(Questions,id = id)
    answers = question.answers.all()

    return render(request,"question-detail.html",{"question":question,"answers":answers})

@login_required(login_url="user:login")
def tag_detail(request,slug):
    question = get_object_or_404(Questions,slug=slug)
    return render(request,"questions.html",{"question":question})

@login_required(login_url="user:login")
def addAnswer(request,id):
    question = get_object_or_404(Questions,id=id)

    if request.method == "POST":

        answer_content = request.POST.get("answer_content")
        answer_author = request.user 

        newAnswer = Answers(answer_content=answer_content,answer_author=answer_author)

        newAnswer.question = question

        newAnswer.save()
    return redirect(reverse("ask:detail",kwargs={"id":str(id)}))

@login_required(login_url="user:login")
def updateQuestion(request,id):
    question = get_object_or_404(Questions,id=id)
    form = QuestionsForm(request.POST or None, request.FILES or None, instance= question)

    if form.is_valid():
        question = form.save(commit=False)
        question.author = request.user
        question.save()

        messages.success(request,"Question Updated Succesfully")
        return redirect("article:dashboard")
    return render(request,"question-update.html",{"form":form})

@login_required(login_url="user:login")
def deleteQuestion(request,id):
    question = get_object_or_404(Questions,id=id)
    question.delete()

    messages.success(request,"Question Deleted Succesfully!")
    return redirect("article:dashboard")



def AddReport(request,id):
    question = get_object_or_404(Questions,id=id)
    
    if request.method == "POST":
        reason = request.POST.get("reason_area")
        message = request.POST.get("message_area")
        report = Report(reason = reason , message = message)
        report.question = question
        report.save()
        user = request.user
        messages.success(request,"Question reported successfully. Thanks" " "+ str(user) +" " "for making our community better!")
        return redirect("ask:questions")
        
    return render(request,"questions.html")
    