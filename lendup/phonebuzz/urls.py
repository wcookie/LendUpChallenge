from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^gather/$', views.gather_digits),
	url(r'^respond/$', views.handle_response),
	url(r'^call/$', views.make_call),
	url(r'^list/$', views.show_calls, name='list'),
	url(r'^progress/(?P<pk>\d+)/$', views.repeat_call, name='repeat'),
	url(r'^completerepeatcall/(?P<number>[0-9]+)/(?P<test>.*)', views.complete_repeat_call, name='callnumber'),
]


