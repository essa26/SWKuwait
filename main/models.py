from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

#number_validator = RegexValidator(r'^[0-9]*$','Please type only numbers for your civil ID')



class Log(models.Model):
    bloog_sugar = models.IntegerField()
    date = models.DateTimeField()
    comment = models.TextField(null=True)

    user = models.ForeignKey(User)  # django stock user?

