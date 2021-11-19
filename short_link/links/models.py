from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
	Url = models.TextField()
	Url_key = models.CharField(max_length =7)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	redirect_count = models.IntegerField(null=True) 	