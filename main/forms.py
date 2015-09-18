from django import forms
from django.core.validators import RegexValidator

# RegexValidator(r'^[a-zA-Z]*$','Please Type Letters')

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

alpha_numeric_validator = RegexValidator(
    '^[a-zA-Z0-9_]+$', 'only letters and numbers')

letter_validator = RegexValidator(r'^[a-zA-Z]*$', 'Please Type Letters')


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


class DoctorSearch(forms.Form):
    name = forms.CharField(required=True, validators=[alpha_numeric_validator])

    def __init__(self, *args, **kwargs):
        super(DoctorSearch, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '/doctorsearch/'
        self.helper.layout = Layout()

        self.helper.add_input(Submit('submit', 'Submit'))


class SendEmail(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    # def __init__(self, *args, **kwargs):
    #     super(SendEmail, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = '/email/(?P<pk>\w+)/'
    #     self.helper.layout = Layout()
    #
    #     self.helper.add_input(Submit('submit', 'Submit'))
