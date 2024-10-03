from django.db import models
from hashlib import sha256


# Create your models here.


def make_password(string):
    return sha256(str(string).encode()).hexdigest()


class Account(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
