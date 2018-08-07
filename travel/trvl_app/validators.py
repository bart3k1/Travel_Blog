from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



def validate_username(value):
    try:
        User.objects.get(username=value)
        raise ValidationError("Jest już taki użytkownik")
    except User.DoesNotExist:
        pass

