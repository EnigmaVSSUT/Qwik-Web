from django.urls import path
from .views import (home, user_profile, team, events, 
                    event_registration,lift_off_c_registration,
                    all_regs,app_dev,ar_vr,grp_des,cp,ml_ai,web_dev)

urlpatterns = [
    path('', home, name='home'),
    path('user-profile/', user_profile, name='user-profile'),
    path('team/', team, name='team'),
    path('events/', events, name='events'),
    # path('event-registration/', event_registration, name='event-registration'),
    path('form-index/',lift_off_c_registration,name='form-index'),
    path('all-registrations-liftoffc/', all_regs, name='all-registrations-liftoffc'),
    path('app_dev/',app_dev,name='app_dev'),
    path('ar_vr/',ar_vr,name='ar_vr'),
    path('grp_des/',grp_des,name='grp_des'),
    path('cp/',cp,name='cp'),
    path('ml_ai/',ml_ai,name='ml_ai'),
    path('web_dev/',web_dev,name='web_dev'),
]