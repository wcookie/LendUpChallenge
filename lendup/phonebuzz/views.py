from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from twilio.rest import TwilioRestClient
from django.conf import settings
from django.shortcuts import render
from .forms import InputForm
import time
from django.core.urlresolvers import reverse
from .models import Call
from django_twilio.request import decompose
from django.db.models import Max
# Create your views here.

#getting a call initially and getting their input
@twilio_view
def gather_digits(request):
	
	twilio_response = Response()
	try:
		with twilio_response.gather(action='/phonebuzz/respond/', numDigits=3, finish_on_key='#') as g:
			g.say('Enter your FizzBuzz Number followed by a pound')
	except:
		return HttpResponseBadRequest
	return twilio_response

#responding to input
@twilio_view
def handle_response(request):
 	
	digits = request.POST.get('Digits', '')
	twilio_response = Response()
	
	if digits:
		try:
			mypk=Call.objects.all().aggregate(Max('pk'))
			call=Call.objects.get(pk=mypk['pk__max'])
			call.number=digits
			call.save()
		except:
			call= None

		for i in range(1,int(digits)+1):
			if i%15==0:
				twilio_response.say('fizz buzz')
			elif i%3==0:
				twilio_response.say('fizz')
			elif i%5==0:
				twilio_response.say('buzz')
			else:
				twilio_response.say(str(i))

	return twilio_response

@twilio_view
def make_call(request):
	if request.method=='POST':
		form = InputForm(request.POST)
		if form.is_valid():
			phoneNumber = request.POST.get('number',False)
			delay = request.POST.get('delay',False)
			try:
				int(delay)
				time.sleep(int(delay))
			except :
				if delay!='':
					return HttpResponse("Invalid Delay")
				
			client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
			try:
				call = client.calls.create(url="http://bff93c64.ngrok.io/phonebuzz/gather/",
				from_="+18474236350",
				to=phoneNumber, 	
				)
				call = Call(
					sid=str(call.sid), 
					delay=delay,
					phoneNumber=phoneNumber,

					)
				call.save()
				
			except:
				return HttpResponseBadRequest
			
	
	else:
		form=InputForm()
	return render(request,'phonebuzz/interface.html', {'form': form})

def show_calls(request):
	calls=Call.objects.all()
	return render(request, 'phonebuzz/list.html', {'calls' :calls})

@twilio_view
def repeat_call(request,pk):
	mycall=Call.objects.get(pk=pk)
	phoneNumber=mycall.phoneNumber
	digits=mycall.number
	url_string="http://bff93c64.ngrok.io/phonebuzz/completerepeatcall/"
	url_string=url_string+digits
	url_string=url_string+"/"
	client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	try:
		call = client.calls.create(
		url=url_string,
		from_="+18474236350",
		to=phoneNumber,
		Method="GET",
		)
				
	except:
		return HttpResponseBadRequest
	return render(request, 'phonebuzz/inprogress.html', {'phoneNumber':phoneNumber})

@twilio_view
def complete_repeat_call(request, number, test):
	print("PRINT TEST")
	twilio_response=Response()
	url_string="/phonebuzz/respondwith/"
	url_string=url_string+number
	url_string=url_string+"/"
	for i in range(1,int(number)+1):
		if i%15==0:
			twilio_response.say('fizz buzz')
		elif i%5==0:
			twilio_response.say('buzz')
		elif i%3==0:
			twilio_response.say('fizz')
		else:
			twilio_response.say(str(i))	
	return twilio_response
