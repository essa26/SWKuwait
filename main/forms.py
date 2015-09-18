from django import forms
from django.core.validators import RegexValidator

letter_validator = RegexValidator(r'^[a-zA-Z]*$','Please Type Letters')
