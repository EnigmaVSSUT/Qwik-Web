from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

YEAR_CHOICES = [
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Third'),
    ('4', 'Fourth'),
    ('5', 'Alumni'),
]

DOMAIN_CHOICES = [
    
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
