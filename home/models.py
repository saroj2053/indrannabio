from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields import EmailField

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=15)
    msg = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=122)
    email_address = models.CharField(max_length=122)
    service_taken = models.CharField(max_length=122)
    sub = models.TextField()
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=122)
    query_string = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
