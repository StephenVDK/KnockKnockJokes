from django.db import models
# Create your models here.

class jokeStorage(models.Model):
	#knockKnock = models.CharField("Knock Knock")
	firstPhrase = models.CharField(max_length=256)
	fullJoke = models.CharField(max_length=256)
	#jokeCount = models.AutoField(default=0)
	def __str__(self):
		return self.fullJoke
		



