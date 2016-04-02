from django.db import models

class GameReservation(models.Model):
	"""docstring for GameReservation"""
	player = models.ForeignKey(Player)
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

class Player(models.Model):
	tokenId = models.CharField(max_length=10,  primary_key=True)
	creationDate = models.DateField(default=datetime.now())

class Image(models.Model):
	"""docstring for Image"""
	solution = models.CharField(max_length=12)
	rawFile = models.FileField(upload_to='rawImages/')
		
class ImageChallenge(object):
	"""docstring for ImageChallenge"""
	image = models.ForeignKey(Image)
	game = models.ForeignKey(Game)

	startTime = models.DateField(default=datetime.now())
	timeout = timedelta(seconds=20)
	endTime = models.DateField(default=Field.null)
	def isActive():
		if endTime != null:
			return false
		else if !self.game.isActive():
			self.end()
			return false
		else if datetime.now()>(self.startTime+timeout):
			self.end()
			return false
		else:
			return true
	def end()
		self.endTime = datetime.now()
		

class Game(models.Model):
	request = models.ForeignKey(GameRequest)
	reservation = models.ForeignKey(GameReservation)

	startTime = models.DateField(default=datetime.now())
	timeout = timedelta(seconds=60)
	endTime = models.DateField(default=Field.null)

	activeChallenge = models.ForeignKey(ImageChallenge)

	def isActive():
		if endTime != null:
			return false
		else if datetime.now() > (self.startTime + timeout):
			self.end()
			return false
		else:
			return true

	def end()
		self.endTime = datetime.now()
		self.activeChallenge.end()













