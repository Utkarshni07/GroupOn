from django.db import models

from django.contrib.auth.models import User


# Create your models here.





class Contact(models.Model):
    name = models.CharField(max_length=145)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

