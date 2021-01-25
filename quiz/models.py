from django.db import models
# Create your models here.

correctChoiceOptions = [(1,'1'),(2,'2'),(3,'3'),(4,'4')]

class question_Answer(models.Model):
    quizID   = models.IntegerField(null=False,default=0)
    question = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()
    correct_choice = models.IntegerField(null=False,default=1,choices =correctChoiceOptions)

    def __str__(self):
        return self.question

