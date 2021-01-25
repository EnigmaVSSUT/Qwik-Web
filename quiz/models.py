from django.db import models

# Create your models here.

correctChoiceOptions = [('1','1'),('2',2),('3','3'),('4','4')]

class question_Answer(models.Model):
    quizID   = models.IntegerField(null=False,default=0)
    question = models.CharField(max_length=200, null=False)
    option_1 = models.CharField(max_length=100, null=False)
    option_2 = models.CharField(max_length=100, null=False)
    option_3 = models.CharField(max_length=100, null=False)
    option_4 = models.CharField(max_length=100, null=False)
    corret_choice = models.IntegerField(null=False,default=1,choices = correctChoiceOptions)

    def __str__(self):
        return self.question

