from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from demo.models import *


def gameReservation(request):
	tokenId=request.REQUEST.get('token','')
	invitationId=request.REQUEST.get('invitation','')
	promotionId=request.REQUEST.get('promotion','')

	response=HttpResponse()

	if (tokenId !='' and invitationId != '' and promotionId != ''):
		reservation = GameReservation(tokenId=tokenId, invitationId=invitationId, promotionId=promotionId)
		reservation.save()
		response.status_code=200
	else:
		response.status_code=400
	return response

def gameRequest(request):
	template = loader.get_template('demo.html')
	return HttpResponse(template.render(request))