from django.db import models
# Create your models here.

class jokeStorage(models.Model):
	firstPhrase = models.CharField(max_length=256)
	fullJoke = models.CharField(max_length=256)
	#jokeCount = models.IntField(default=0)
	def __str__(self):
		return self.fullJoke
		



