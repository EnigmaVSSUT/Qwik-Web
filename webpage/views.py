from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MemberRegistrationForm, MemberRegistrationForm2, EventRegistrationForm, LiftOffCRegistrationForm,ContactusForm,NewsletterForm
from django.template.defaultfilters import slugify
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Member, EventRegistration, LiftOffCRegistration,Contactus,Newsletter
from django.utils.html import strip_tags
SENDER_EMAIL = 'orientation@enigmavssut.tech'

# Create your views here.


def home(request):
    return render(request, 'webpages/home.html')


@login_required
def user_profile(request):
    return render(request, 'webpages/user_profile.html')


def team(request):
    if request.method == 'POST':
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
        all_members = Member.objects.all().order_by('-year', 'firstname')
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
        if request.method == 'POST':
            form = EventRegistrationForm(request.POST)
            if form.is_valid():
                new_registration = EventRegistration()
                new_registration.firstname = form.cleaned_data.get('firstname')
                new_registration.lastname = form.cleaned_data.get('lastname')
                new_registration.email = form.cleaned_data.get('email')
                new_registration.year = form.cleaned_data.get('year')
                new_registration.branch = form.cleaned_data.get('branch')
                new_registration.gender = form.cleaned_data.get('gender')
                new_registration.slug = slugify(
                    new_registration.email + 'orientation_2021')
                new_registration.save()
                send_mail_to_user(new_registration)
                messages.success(
                    request, 'You have successfully registered for the orientation! Ckeck you email for further information.')
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


def lift_off_c_registration(request):
    try:
        if request.method == 'POST':
            new_form = LiftOffCRegistrationForm()
            if new_form.is_valid():
                new_mentee = LiftOffCRegistration(request.POST)
                new_mentee.name = new_form.cleaned_data.get('name')
                new_mentee.email = new_form.cleaned_data.get('email')
                new_mentee.whatsapp_no = new_form.cleaned_data.get(
                    'whatsapp_no')
                new_mentee.year = new_form.cleaned_data.get('year')
                new_mentee.branch = new_form.cleaned_data.get('branch')
                new_mentee.knowledge=new_form.cleaned_data.get('knowledge')
                new_mentee.expectations = new_form.cleaned_data.get(
                    'expectations')
                new_mentee.mode_comm = new_form.cleaned_data.get('mode_comm')
                new_mentee.slug = slugify(new_mentee.email + '2021')
                new_mentee.save()
                messages.success(
                    request, 'You have successfully registered!')
                return redirect('events')
            else:
                messages.warning(
                    request, 'Oops! you could not be registred successfully.')
                return redirect('events')
        else:
            new_form=LiftOffCRegistration()
            context={
                'form':new_form
            }
            return render(request,'webpages/form-index.html',context)

    except:
        messages.warning(request, 'You Have already registered!')
        return redirect('events')


def events(request):
    try:
        if request.method == 'POST':
            new_form = LiftOffCRegistrationForm(request.POST)
            if new_form.is_valid():
                new_mentee = LiftOffCRegistration()
                new_mentee.name = new_form.cleaned_data.get('name')
                new_mentee.email = new_form.cleaned_data.get('email')
                new_mentee.whatsapp_no = new_form.cleaned_data.get(
                    'whatsapp_no')
                new_mentee.year = new_form.cleaned_data.get('year')
                new_mentee.branch = new_form.cleaned_data.get('branch')
                new_mentee.knowledge=new_form.cleaned_data.get('knowledge')
                new_mentee.expectations = new_form.cleaned_data.get(
                    'expectations')
                new_mentee.mode_comm = new_form.cleaned_data.get('mode_comm')
                new_mentee.slug = slugify(new_mentee.email + 'cc2021')
                new_mentee.save()
                messages.success(
                    request, 'You have successfully registered!')
                return redirect('events')
            else:
                print(new_form.errors)
                messages.warning(
                    request, 'Oops! you could not be registered successfully.')
                return redirect('events')
        else:
            new_form=LiftOffCRegistration()
            context={
                'form':new_form
            }
            return render(request,'webpages/events.html',context)

    except:
        messages.warning(request, 'You Have already registered!')
        return redirect('events')
    
def all_regs(request):
    all = LiftOffCRegistration.objects.all()
    all_count = LiftOffCRegistration.objects.all().count()
    context = {
        'all': all,
        'all_count': all_count
    }
    return render(request, 'webpages/all_mentee_regs.html', context)

def app_dev(request):
    return render(request,'webpages/app.html',{'title':'APP DEVELOPMENT'})

def ar_vr(request):
    return render(request,'webpages/ar_vr.html',{'title':'VIRTUAL REALITY'})

def grp_des(request):
    return render(request,'webpages/grp-des.html',{'title':'GRAPHIC DESIGN'})

def cp(request):
    return render(request,'webpages/cp.html',{'title':'COMPETITIVE PROGRAMMING'})

def ml_ai(request):
    return render(request,'webpages/ml_ai.html',{'title':'MACHINE LEARNING/ARTIFICIAL INTELLIGENCE'})

def web_dev(request):
    return render(request,'webpages/web_dev.html',{'title':'WEB DEVELOPMENT'})


def contact_us(request):
    if request.method=='POST':
        contact_form=ContactusForm(request.POST)
        if contact_form.is_valid():
            new_contact=Contactus()
            new_contact.name=contact_form.cleaned_data.get('name')
            new_contact.email=contact_form.cleaned_data.get('email')
            new_contact.subject=contact_form.cleaned_data.get('subject')
            new_contact.msg=contact_form.cleaned_data.get('message')
            new_contact.save()
            messages.success(request,'Message successfully sent!')
            return redirect('home')
        else:
            print(contact_form.errors)
            messages.warning(request,
            'Message could not be successfuly sent.Try again.')
            return redirect('home')
    else:
        contact_form=Contactus()
        context={
            'form':contact_form
        }
        return render(request,'webpages/home.html',context)


def sub_newsletter(request):
    try:
        if request.method=='POST' and 'news_sub' in request.POST:
            subs_form=NewsletterForm(request.POST)
            if subs_form.is_valid():
                new_subs=Newsletter()
                new_subs.email=subs_form.cleaned_data.get('email')
                new_subs.slug=slugify(new_subs.email + 'subsnew')
                new_subs.save()
                messages.success(request,'You have successfully subscribed!')
                return redirect('home')
            else:
                print(subs_form.errors)
                messages.warning(request,
                'Oops!you could not be subscribed successfully')
                return redirect('home')
        else:
            subs_form=Newsletter()
            context={
                'form':subs_form
            }
            return render(request,'webpages/home.html',context)
        
    except:
        messages.warning(request,'You have already subscribed')
        return redirect('home')