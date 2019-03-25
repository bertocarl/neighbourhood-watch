from django.contrib import admin
from .models import Neighbourhood,Notifications,Business,Blog,Profile


class HealthAdmin(admin.ModelAdmin):
    filter_horizontal =['healthservices']

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(Notifications)
