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

DOMAIN_CHOICES = [

]

GENDER_CHOICES= [
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
]

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    year = models.CharField(choices=YEAR_CHOICES, max_length=6)
    github = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    others = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(upload_to='member_profile_pic', default='default.jpg')
    slug = models.SlugField(unique=True, max_length=100)

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