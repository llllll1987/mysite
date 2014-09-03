from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

def hello(request):
	return HttpResponse("Hello World!")
	pass

def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html',{'current_date' : now})

def base(request):
	return render_to_response('base.html')


