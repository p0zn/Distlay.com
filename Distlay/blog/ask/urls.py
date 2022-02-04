from django.contrib import admin
from django.urls import path
from . import views


app_name = "ask"


urlpatterns = [
    path('addquestion/',views.addQuestion,name="addquestion"),
    path('question/<int:id>',views.detail,name="detail"),
    path('tag/<slug:slug>/',views.tagged,name="tagged"),
    path('update-question/<int:id>',views.updateQuestion,name="update"),
    path('delete-question/<int:id>',views.deleteQuestion,name="remove"),
    path('answer/<int:id>',views.addAnswer,name="answer"),
    path('',views.questions,name="questions"),
    path('', views.AddReport,name="add_report"),

]
