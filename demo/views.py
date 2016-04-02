from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponse
from django.template import loader
from demo.models import *


def gameReservation(request):
	tokenId=request.REQUEST.get('token','')
	invitationId=request.REQUEST.get('invitation','')
	promotionId=request.REQUEST.get('promotion','')

	response=HttpResponse()

	if (tokenId !='' and invitationId != '' and promotionId != ''):
		try:
			player = Player.objects.get(tokenId=tokenId)
		except ObjectDoesNotExist:
			raise
			player = Player(tokenId=tokenId)
		storedReservation = GameReservation(player=player, invitationId=invitationId, promotionId=promotionId)
		storedReservation.save()
		response.status_code=200
	else:
		response.status_code=400
	return response

def gameRequest(request):
	validationId=request.REQUEST.get('validation','')
	invitationId=request.REQUEST.get('invitation','')

	response=HttpResponse()

	if (validationId !='' and invitationId != '' and promotionId != ''):
		storedRequest = GameReservation(validationId=validationId, invitationId=invitationId, promotionId=promotionId)
		storedRequest.save()
		response.status_code=200
	else:
		response.status_code=400
	return response