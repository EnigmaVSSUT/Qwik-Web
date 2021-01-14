from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MemberRegistrationForm, MemberRegistrationForm2
from django.template.defaultfilters import slugify

# Create your views here.

def home(request):
    return render(request, 'webpages/home.html')

@login_required
def user_profile(request):
    return render(request, 'webpages/user_profile.html')

def team(request):
    if request.method=='POST':
        m_form = MemberRegistrationForm(request.POST, request.FILES)
        m_form2 = MemberRegistrationForm2(request.POST)
        if m_form.is_valid() and m_form2.is_valid():
            new_member = m_form.save(commit=False)
            new_member = m_form2.save(commit=False)
            new_member.slug = slugify(new_member.linkedin)
            new_member.save()
            messages.success(request, 'New member was added!')
            return redirect('team')
        else:
            messages.warning(request, 'Invalid Entry!')
    else:
        m_form = MemberRegistrationForm()
        m_form2 = MemberRegistrationForm2()
        context = {
            'title': 'team',
            'm_form': m_form,
            'm_form2': m_form2
        }
        return render(request, 'webpages/team-page.html', context)