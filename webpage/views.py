from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'webpages/home.html')

@login_required
def user_profile(request):
    return render(request, 'webpages/user_profile.html')

def team(request):
    context = {
        'title': team
    }
    return render(request, 'webpages/team-page.html', context)