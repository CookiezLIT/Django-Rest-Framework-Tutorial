from django.db import models

# Create your models here.
from django.db.models import IntegerField, CharField


class Angajat(models.Model):

    nume = CharField(max_length=250)
    prenume = CharField(max_length=250)
    varsta = IntegerField()
    oras = CharField(max_length=250)
