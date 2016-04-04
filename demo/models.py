from django.db import models

class GameReservation(models.Model):
	"""docstring for GameReservation"""
	player = models.ForeignKey(Player)
	invitationId = models.CharField(max_length=10)
	promotionId = models.BooleanField(default=True)

class GameRequest(models.Model):
	"""docstring for GameRequest"""
	validationId = models.CharField(max_length=10)
	invitaionId = models.CharField(max_length=10)

class Player(models.Model):
	token = models.CharField(max_length=10,  primary_key=True)
	creationDate = models.DateField(default=datetime.now())

class Image(models.Model):
	"""docstring for Image"""
	solution = models.CharField(max_length=12)
	rawFile = models.ImageField(upload_to='rawImages/')
		
class ImageChallenge(models.Model):
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
	def getImage():
		if self.isActive():
			return self.image
		else
			return null
	def end()
		self.endTime = datetime.now()
		

class Game(models.Model):
	"""docstring for ImageChallenge"""
	token = models.CharField(max_length=20,  primary_key=True)
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

	def getImage():
		if self.activeChallenge != null:
			return self.activeChallenge.getImage()

	def end()
		self.endTime = datetime.now()
		self.activeChallenge.end()













