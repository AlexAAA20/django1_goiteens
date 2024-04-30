from django.db import models
from django.contrib.auth.models import AbstractUser

class Tag(models.Model):
	name = models.CharField(max_length=100)

class User(AbstractUser):
	email = None

class ObjectAdditionalInfo(models.Model):
	views = models.IntegerField(default=0, blank=0)
class Comment(models.Model):
	text = models.CharField(max_length=50, null=False)
	commenter = models.ForeignKey(User, on_delete=models.CASCADE)
	karma = models.IntegerField(default=0, blank=0)
	attachedToInfo = models.ForeignKey(ObjectAdditionalInfo, on_delete=models.CASCADE)


class Object(models.Model):
	description = models.TextField(max_length=256, null=False)
	name = models.CharField(max_length=128)
	url = models.URLField(null=False)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag)
	additional_info = models.ForeignKey(ObjectAdditionalInfo, on_delete=models.CASCADE)
	views = models.IntegerField(default=0, blank=0)

