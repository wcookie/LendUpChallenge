from django.shortcuts import render
from django.http import HttpResponse
from twilio.twiml import Response
from django_twilio.decorators import twilio_view

# Create your views here.
@twilio_view
def gather_digits(request):

	twilio_response = Response()

	with twilio_response.gather(action='/respond', numDigits=1) as g:
		g.say('Press one or two')
		g.pause(length=1)
		g.say('Same thing all over')
	return twilio_response