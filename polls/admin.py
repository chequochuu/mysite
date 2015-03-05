from django.contrib import admin
from polls.models import Question, Choice, Aaa

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class heo(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date','was_published_recently')
    inlines = [ChoiceInline]

admin.site.register(Choice)	
admin.site.register(Question,heo)	
admin.site.register(Aaa)	

# Register your models here.


