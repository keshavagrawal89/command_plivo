from django.db import models

# Create your models here.

class CommandMappings(models.Model):
	command = models.CharField(max_length=150)
	api_request = models.URLField(max_length=500)


