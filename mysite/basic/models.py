from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	...

class Game(models.Model):
	name = models.CharField(max_length=128, null=False)
	description = models.TextField(max_length=2048)
	url = models.URLField(null=False)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
