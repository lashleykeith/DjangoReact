from django.db import models
import datetime

class Band(models.Model):
	name = models.CharField(max_length=128, null=False, blank=False, unique=True)
	date_added = models.DateField(default=datetime.datetime.now())
	image = models.CharField(max_length=250, null=True, blank=True)
	bio = models.TextField(max_length=5000, null=True, blank=True)