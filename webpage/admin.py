from django.contrib import admin
from .models import Member, EventRegistration, LiftOffCRegistration,Contactus,Newsletter
# Register your models here.
admin.site.register(Member)
admin.site.register(EventRegistration)
admin.site.register(LiftOffCRegistration)
admin.site.register(Contactus)
admin.site.register(Newsletter)