from django.contrib import admin
from .models import question_Answer

admin.site.site_header = "Enigma Admin Portal"

# Register your models here.


class questionData(admin.ModelAdmin):
    list_display = ('question','option_1','option_2','option_3','option_4','quizID','correct_choice')
    # list_filter = ('date_of_joining','completely_filled')
    list_per_page = 20
    # def complete(self, obj): 
    #     return obj.completely_filled
  
    # complete.boolean = True
admin.site.register(question_Answer,questionData)