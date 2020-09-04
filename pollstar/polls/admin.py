from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Pollstar Admin"
admin.site.site_title = "Pollstar Admin Area"
admin.site.index_title = "Welcome to Pollstar Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [("QUESTION", {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
