from django.contrib import admin
from .models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('name','email','subject','message')
admin.site.register(Contact, ContactAdmin)
