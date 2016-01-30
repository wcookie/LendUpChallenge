from django.db import models

# Create your models here.
class Call(models.Model):
	sid = models.CharField( max_length=50)
	date = models.DateTimeField(auto_now_add=True)
	delay = models.CharField(null=True, max_length=50)
	number = models.CharField(null=True, max_length=50)
	phoneNumber = models.CharField(max_length=50)
	