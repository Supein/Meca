from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponse
from django.template import loader
from demo.models import *


def gameReservation(request):
	token=request.REQUEST.get('token','')
	invitationId=request.REQUEST.get('invitation','')
	promotionId=request.REQUEST.get('promotion','')

	response=HttpResponse()

	if (token !='' and invitationId != '' and promotionId != ''):
		storedReservation = GameReservation(player=getPlayer(request), invitationId=invitationId, promotionId=promotionId)
		storedReservation.save()
		response.status_code = 200
	else:
		response.status_code = 400
	return response

def gameRequest(request):
	validationId=request.REQUEST.get('validation','')
	invitationId=request.REQUEST.get('invitation','')

	response=HttpResponse()

	if (validationId !='' and invitationId != ''):
		storedRequest = GameReservation(validationId=validationId, invitationId=invitationId)
		storedRequest.save()
		response.status_code = 200
	else:
		response.status_code = 400
	return response

def getPlayer(request):
	token=request.REQUEST.get('token','')
	try:
		player = Player.objects.get(token=token)
	except ObjectDoesNotExist:
		player = Player(tokenId=token)
	return player

def getImage():
	gameToken=request.REQUEST.get('gameToken','')
	response=HttpResponse()
	if (gameToken !=''):
		try:
			game = Game.objects.get(token=gameToken)
			if game.isActive() and game.getImage() != null:
				img = game.getImage
	    		wrapper = FileWrapper(open(img.file))
	    		content_type = mimetypes.guess_type(filename)[0]
	    		response = HttpResponse(wrapper,content_type=content_type)  
	    		response['Content-Length']      = os.path.getsize(img.file)    
	    		response['Content-Disposition'] = "attachment; filename=CurrentImage"
	    		response.status_code = 200
		except ObjectDoesNotExist:
			response.status_code = 401
	else:
		response.status_code = 401
	return response









