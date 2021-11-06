from django.db import models

class Link(models.Model):
	Url = models.TextField()
	Url_key = models.CharField(max_length =7)