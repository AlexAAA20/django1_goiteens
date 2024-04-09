from django.db import models
from django.contrib.auth.models import AbstractUser

class Tag(models.Model):
	name = models.CharField(max_length=100)

class User(AbstractUser):
	...

class Object(models.Model):
	name = models.CharField(max_length=128, null=False)
	description = models.TextField(max_length=2048)
	url = models.URLField(null=False)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag)
