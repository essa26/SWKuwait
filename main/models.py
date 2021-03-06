from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

#number_validator = RegexValidator(r'^[0-9]*$','Please type only numbers for your civil ID')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    log = models.OneToOneField(Log)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    emergency1 = models.CharField(max_length=15)
    emergency2 = models.CharField(max_length=15)
    clinic = models.ForeignKey('main.Clinic')

    def __unicode__(self):
        return self.user.username


class Log(models.Model):
    blood_sugar = models.IntegerField()
    date = models.DateTimeField()
    comment = models.TextField(null=True)
    user = models.ForeignKey('main.UserProfile')

    def __unicode__(self):
        return self.user.username


class DoctorProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255)
    clinic = models.ForeignKey('main.clinic')
    mobile = models.CharField(max_length=15)

    def __unicode__(self):
        return self.user.username


class Clinic(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
