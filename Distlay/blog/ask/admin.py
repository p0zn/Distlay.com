from django.contrib import admin

# Register your models here.

from .models import Questions,Answers,Report

admin.site.register(Report)

admin.site.register(Answers)

@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):

    list_display = ["title","author","asked_date"]
    list_display_links = ["title","asked_date"]
    search_fields = ["title"]
    list_filter = ["asked_date"]

    class Meta:
        model = Questions

