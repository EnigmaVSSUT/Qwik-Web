from django.urls import path
from .views import home, user_profile

urlpatterns = [
    path('', home, name='home'),
    path('user-profile/', user_profile, name='user-profile'),
]