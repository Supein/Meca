from django.db import models

class GameReservation(models.Model):
	"""docstring for GameReservation"""
	tokenId = models.CharField(max_length=10)
	invitationId = models.CharField(max_length=10)
	promotionId = models.BooleanField(default=True)
	def __unicode__(self):
		return 'token Id: '+self.tokenId+', invitation Id: '+self.invitaionId+', promotion Id: '+self.promotionId
	def toString():
		return "token Id: "

class GameRequest(models.Model):
	"""docstring for GameRequest"""
	validationId = models.CharField(max_length=10)
	invitaionId = models.CharField(max_length=10)

class ActiveGame(models.Model):
