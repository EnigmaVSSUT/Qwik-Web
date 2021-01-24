from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Member, EventRegistration, LiftOffCRegistration,Contactus,Newsletter


class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname',
                  'lastname',
                  'email',
                  'year',
                  'profile_pic',
                  ]

# ------------------------------- MemberRegistrationForm2 is not required (can be deleted)-------------------------------


class MemberRegistrationForm2(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'github',
            'linkedin',
            'facebook',
            'instagram',
        ]


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = [
            'firstname',
            'lastname',
            'email',
            'year',
            'branch',
            'gender',
        ]


class LiftOffCRegistrationForm(forms.ModelForm):
    class Meta:
        model = LiftOffCRegistration
        fields = [
            'name',
            'email',
            'whatsapp_no',
            'year',
            'branch',
            'knowledge',
            'expectations',
            'mode_comm'
        ]

class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = [
            'name',
            'email',
            'subject',
            'msg'
        ]

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = [
            'email'
        ]