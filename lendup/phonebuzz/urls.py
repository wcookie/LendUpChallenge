from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^gather$', views.gather_digits),
]

