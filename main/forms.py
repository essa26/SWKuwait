from django import forms
from django.core.validators import RegexValidator

# RegexValidator(r'^[a-zA-Z]*$','Please Type Letters')

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserLogin, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '/login/'
        self.helper.layout = Layout()

        self.helper.add_input(Submit('submit', 'Submit'))
