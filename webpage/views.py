from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MemberRegistrationForm, MemberRegistrationForm2, EventRegistrationForm
from django.template.defaultfilters import slugify
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Member, EventRegistration
from django.utils.html import strip_tags
SENDER_EMAIL = 'orientation@enigmavssut.tech'

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
            new_member.github = m_form2.cleaned_data.get('github')
            new_member.facebook = m_form2.cleaned_data.get('facebook')
            new_member.linkedin = m_form2.cleaned_data.get('linkedin')
            new_member.instagram = m_form2.cleaned_data.get('instagram')
            new_member.slug = slugify(new_member.linkedin)
            new_member.save()
            sm = str(new_member.profile_pic)
            smr = sm[:sm.rfind('.')] + '_300x400' + sm[sm.rfind('.'):]
            new_member.profile_pic = smr
            new_member.save()
            messages.success(request, 'New member was added!')
            return redirect('team')
        else:
            messages.warning(request, 'Invalid Entry!')
    else:
        all_members = Member.objects.all().order_by('-year', '')
        m_form = MemberRegistrationForm()
        m_form2 = MemberRegistrationForm2()
        context = {
            'all_members': all_members,
            'title': 'team',
            'm_form': m_form,
            'm_form2': m_form2
        }
        return render(request, 'webpages/team-page.html', context)

def send_mail_to_user(attendee):
    context = {
        "attendee": attendee
    }
    html_content = render_to_string("emails/reg_confirmation.html", context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        "Registered for orientation",
        text_content,
        SENDER_EMAIL,
        [attendee.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_mails(attendee):
    context = {
        "attendee": attendee
    }
    html_content = render_to_string("emails/final_mail.html", context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        "Link for orientation",
        text_content,
        SENDER_EMAIL,
        [attendee.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

def event_registration(request):
    try:
        if request.method=='POST':
            form = EventRegistrationForm(request.POST)
            if form.is_valid():
                new_registration = EventRegistration()
                new_registration.firstname = form.cleaned_data.get('firstname')
                new_registration.lastname = form.cleaned_data.get('lastname')
                new_registration.email = form.cleaned_data.get('email')
                new_registration.year = form.cleaned_data.get('year')
                new_registration.branch = form.cleaned_data.get('branch')
                new_registration.gender = form.cleaned_data.get('gender')
                new_registration.slug = slugify(new_registration.email + 'orientation_2021')
                new_registration.save()
                send_mail_to_user(new_registration)
                messages.success(request, 'You have successfully registered for the orientation! Ckeck you email for further information.')
                return redirect('events')
            else:
                messages.success(request, 'Invalid Credentials')
                return redirect('events')

        else:
            form = EventRegistrationForm()
            context = {
                'form': form
            }
            return render(request, 'webpages/event-registration.html', context)
    except:
        messages.warning(request, 'You Have already registered for the event!')
        return redirect('events')

def events(request):
    total = EventRegistration.objects.all().count()
    context = {
        'total': total
    }
    return render(request, 'webpages/events.html', context)