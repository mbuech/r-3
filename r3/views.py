from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Template
from models import Routes
from BeautifulSoup import BeautifulSoup
import simplejson as json
import urllib
import urllib2

origin = ''
destination = ''
leave_date = ''
return_date = ''
own_car = ''
can_drive = ''

def hello(request):
	return render_to_response('index.html')

def find(request):
	if not request.is_ajax():
		return render_to_response('index.html')
	origin = request.POST['ori']
	destination = request.POST['dest']
	leave_date = request.POST['leave']
	return_date = request.POST['returnd']
	own_car = request.POST['own']
	can_drive = request.POST['can']
	#ALGO HERE YO
	#MAKE THAT SHIT JSON!!!!
	#send it back to js
	message = origin + destination + leave_date + return_date + own_car
	return HttpResponse(json.dumps({"MESSAGE":message}), mimetype="application/json")

#python functions

def getDirectionsDriving {
	api_driving = 'http://maps.googleapis.com/maps/api/directions/json?'
	origin_api = 'origin=' + urllib2.quote("32 Endicott Drive, Amherst New York")
	destination_api = 'destination=' + urllib2.quote("206 Brownshill Road, Pittsburgh Pennsylvania")
	final_drive = api_driving + origin_api + '&' + destination_api + '&sensor=false'
	response = urllib2.urlopen(final_drive)
	directions_drive = simplejson.loads(response.read())
	
}
