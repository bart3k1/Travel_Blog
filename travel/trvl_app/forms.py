import requests
from django import forms
from django.core.exceptions import ValidationError

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
        if len(password) < 6:
            raise ValidationError('Za krótkie hasło - min 6 znaków')
        if password != password2:
            raise ValidationError('Hasła się różnią')
        return password


def get_my_choices():
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&lang=pl&appid=2a11288255bccc9dcaed8d0467ac0ec8'
    city = 'Warsaw'
    choices_list_2 = []
    r = requests.get(url.format(city)).json()
    for i in range(len(r['list'])):
        choices_list_2.append((str(r['list'][i]['dt_txt']), str(r['list'][i]['dt_txt'])))
    return tuple(choices_list_2)


class CityForm(forms.Form):
    name = forms.CharField(max_length=64, label="Wpisz miasto", widget=forms.TextInput(attrs={'placeholder': 'np. London'}))
    dates = forms.ChoiceField(choices=get_my_choices(), label="Wybierz datę i godzinę")
