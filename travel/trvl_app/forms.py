import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import SelectDateWidget
from trvl_app.validators import validate_username





class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, label="User ")
    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")


class AddUserForm(forms.Form):
    username = forms.CharField(max_length=64, validators=[validate_username], label="Użytkownik")
    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")
    password_c = forms.CharField(widget=forms.PasswordInput, label="Powt. hasło")
    first_name = forms.CharField(max_length=64, label="Imię")
    last_name = forms.CharField(max_length=64, label="Nazwisko")
    email = forms.EmailField(label="e-mail")

    def clean_password_c(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password_c']
        if password != password2:
            raise ValidationError('Hasła się różnią')
        return password


year = datetime.date.today().year
date_today = datetime.date.today()
date_month_plus = date_today + datetime.timedelta(days=5)
date_month_minus = date_today


class CityForm(forms.Form):
    name = forms.CharField(max_length=64, label="Wpisz miasto", widget=forms.TextInput(attrs={'placeholder': 'np. London'}))
