from django import forms
from django.db.models import fields
from .models import Questions,Report

choices = [('Not researched question','Not researched question'),('Asked many times','Asked many times'),('Bad language use','Bad language use'),
('Quote question','Quote question'),('Offesinve question','Offesinve question'),

]



class QuestionsForm(forms.ModelForm):
    
    class Meta:
        model = Questions
        fields = [
            "title",
            "content",
            "tags",
            "question_image"
        
        ]

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = [
            "reason",
            "message"
        ]     

        widgets = {
            'reason' : forms.Select(choices=choices, attrs={'class':'form-control'}),
        }