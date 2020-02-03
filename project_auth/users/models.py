from django.db import models

# Create your models here.
class HabUsers(models.Model):
	username = models.CharField(max_length=100)
	email = models.EmailField()
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	institution = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)