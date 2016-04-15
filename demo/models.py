from django.db import models
from datetime import timedelta

class Player(models.Model):
	token = models.CharField(max_length=10,  primary_key=True)
	creationDate = models.DateField(auto_now_add = True)

class GameReservation(models.Model):
	"""docstring for GameReservation"""
	player = models.ForeignKey(Player, null=True)
	invitationId = models.CharField(max_length=10)
	promotionId = models.BooleanField(default=True)

class GameRequest(models.Model):
	"""docstring for GameRequest"""
	validationId = models.CharField(max_length=10)
	invitaionId = models.CharField(max_length=10)

	def isEligible():
		return (self.getGame() != null and self.getGame.isActive()) or (self.getGame() == null and self.getReservation()!=null)
			
	def getGame():
		try:
			return Game.objects.get(request=self)
		except ObjectDoesNotExist:
			return null

	def getReservation():
		try:
			return GameReservation.objects.get(invitaionId = self.invitaionId)
		except ObjectDoesNotExist:
			return null



class Image(models.Model):
	"""docstring for Image"""
	solution = models.CharField(max_length=12)
	rawFile = models.ImageField(upload_to='rawImages/')

class Game(models.Model):
	"""docstring for ImageChallenge"""
	token = models.CharField(max_length=20,  primary_key=True)
	request = models.ForeignKey(GameRequest)
	reservation = models.ForeignKey(GameReservation)

	startTime = models.DateField(auto_now_add = True)
	timeout = timedelta(seconds=60)
	endTime = models.DateField()
	remainingChallenges = 1

	activeChallenge = models.ForeignKey('ImageChallenge', null=True)

	def isActive():
		if endTime != null:
			return False
		elif datetime.now() > (self.startTime + timeout):
			self.end()
			return False
		else:
			return True

	def getImage():
		if self.activeChallenge != null:
			return self.activeChallenge.getImage()
	def check():
		return True

	def end():
		self.endTime = timezone.now()
		if self.activeChallenge !=null:
			self.activeChallenge.end()

	def challengeDidEnd(challenge):
		if challenge == self.activeChallenge:
			if self.remainingChallenges > 0:
				self.activeChallenge = self.getNewChallenge()
	def getNewChallenge():
		if self.remainingChallenges == Game.remainingChallenges:
			pass
		img = Image.objects.order_by('?').first()
		self.activeChallenge=ImageChallenge(Image=img,parentGame=self)
		self.remainingChallenges -= 1


		
class ImageChallenge(models.Model):
	"""docstring for ImageChallenge"""
	image = models.ForeignKey(Image)
	parentGame = models.ForeignKey(Game)

	startTime = models.DateField(auto_now_add = True)
	timeout = timedelta(seconds=20)
	endTime = models.DateField()

	def isActive():
		if endTime != null:
			return False
		elif not self.parentGame.isActive():
			self.end()
			return False
		elif datetime.now()>(self.startTime+timeout):
			self.end()
			return False
		else:
			return True
	def getImage():
		if self.isActive():
			return self.image
		else:
			return null
	def end():
		self.endTime = timezone.now()
		self.parentGame.challengeDidEnd(self)
		















