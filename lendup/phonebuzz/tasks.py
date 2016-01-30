from celery import task
from django.conf import settings

@task()
def makeCall(phoneNumber):
	client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	try:
		call = client.calls.create(url="http://bff93c64.ngrok.io/phonebuzz/gather/",
		from_="+18474236350",
		to=phoneNumber,
		)
		return
	except:
		return HttpResponseBadRequest