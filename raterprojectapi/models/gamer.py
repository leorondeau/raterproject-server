from django.db import models
from django.contrib.auth.models import User

class Gamer(models.Model):

    user = models.OneToOneField, on_delete=models.CASCADE
    