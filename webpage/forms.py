from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Member,Participant

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 
                'lastname', 
                'email', 
                'year', 
                'profile_pic',
                ]

class MemberRegistrationForm2(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
                'github', 
                'linkedin', 
                'facebook',
                'instagram',
                ]

class ParticipantRegistrationForm(forms.ModelForm):
    class Meta:
        model=Participant
        fields=['first_name',
        'last_name'
        'birthdate',
        'gender_p',
        'email',
        'phone']