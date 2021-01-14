from django.urls import path
from .views import home, user_profile, team,register

urlpatterns = [
    path('', home, name='home'),
    path('user-profile/', user_profile, name='user-profile'),
    path('team/', team, name='team'),
    path('register/',register,name='register')
]