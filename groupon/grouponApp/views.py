from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, "index.html")
def portfolio(request):
    return render(request, "portfolio.html")
def innerpage(request):
    return render(request, "innerpage.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact(name=name, email=email, subject=subject, message=message)
        data.save()
    send_mail(
        'Contact',
        'Details of the sender',
        'groupon.yrdu@gmail.com',
        ['groupon.yrdu@gmail.com'],
        fail_silently=False,
    )
    return render(request, 'index.html')
    