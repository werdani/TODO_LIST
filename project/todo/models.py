from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
	title   = models.CharField(max_length = 150)
	checked = models.BooleanField(default = False)
	created = models.DateTimeField(default = timezone.now)
	
