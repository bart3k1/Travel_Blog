from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Travel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='travels', verbose_name='Autor')
    topic = models.CharField(max_length=100, verbose_name='Tytuł')
    content = models.TextField(max_length=400, null=True, verbose_name='Opis')

    def __str__(self):
            return "{}".format(self.topic)

    class Meta:
        verbose_name = "Podróż"
        verbose_name_plural = "Podróże"


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return "{}".format(self.name)

    class Meta:
        verbose_name = "Miasto"
        verbose_name_plural = "Miasta"