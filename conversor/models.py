from django.db import models

class Audio(models.Model):

	nome = models.CharField(max_length = 255)
	texto = models.TextField()

	def __str__(self):
		return self.title

