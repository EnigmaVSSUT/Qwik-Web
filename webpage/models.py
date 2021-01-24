from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

YEAR_CHOICES = [
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Pre-Final'),
    ('4', 'Final'),
    ('5', 'Alumni'),
]

YEAR_CHOICES_NEW=[
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Pre-Final'),
    ('4', 'Final')
]

#BRANCH_CHOICES = [
#    ('CHEMICAL ENGINEERING', 'CHEMICAL ENGINEERING'),
#    ('CIVIL ENGINEERING', 'CIVIL ENGINEERING'),
#    ('COMPUTER SCIENCE AND ENGINEERING', 'COMPUTER SCIENCE AND ENGINEERING'),
#    ('ELECTRICAL ENGINEERING', 'ELECTRICAL ENGINEERING'),
#    ('ELECTRONICS AND TELECOMMUNICATION ENGINEERING',
#     'ELECTRONICS AND TELECOMMUNICATION ENGINEERING'),
#    ('ELECTRICAL AND ELECTRONICS ENGINEERING',
#    'ELECTRICAL AND ELECTRONICS ENGINEERING'),
#    ('INFORMATION TECHNOLOGY', 'INFORMATION TECHNOLOGY'),
#    ('MECHANICAL ENGINEERING', 'MECHANICAL ENGINEERING'),
#    ('METALLURGY AND MATERIALS ENGINEERING',
#     'METALLURGY AND MATERIALS ENGINEERING'),
#    ('PRODUCTION ENGINEERING', 'PRODUCTION ENGINEERING'),
#]

KNOWLEDGE_CHOICES=[
    ('Totally new to programming','Totally new to programming'),
    ('Have somewhat knowledge of C but want to master it','Have somewhat knowledge of C but want to master it'),
    ('Knows other language but want to learn C','Knows other language but want to learn C'),
    ('A total pro at programming','A total pro at programming')
]

DOMAIN_CHOICES = [

]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

MODE_COMMUNICATION = [
    ('WhatsApp', 'WhatsApp'),
    ('Telegram', 'Telegram'),
    ('Discord', 'Discord')
]


class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    year = models.CharField(choices=YEAR_CHOICES, max_length=6)
    github = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    others = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='member_profile_pic', default='default.jpg')
    slug = models.SlugField(unique=True, max_length=100)

# hhtps:
    def __str__(self):
        return self.firstname


class EventRegistration(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    year = models.CharField(max_length=15)
    branch = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=8)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.firstname

class LiftOffCRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    whatsapp_no = models.CharField(max_length=15)
    year = models.CharField(max_length=20)
    branch = models.CharField(max_length=100)
    knowledge=models.CharField(max_length=100)
    expectations = models.TextField(null=True, blank=True)
    mode_comm = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.name

class Contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=150)
    msg=models.TextField()
    

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,max_length=100)
    
    def __str__(self):
        return self.email