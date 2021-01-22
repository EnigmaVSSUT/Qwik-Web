from django.contrib import admin
from .models import Member, EventRegistration, LiftOffCRegistration
# Register your models here.
admin.site.register(Member)
admin.site.register(EventRegistration)
admin.site.register(LiftOffCRegistration)