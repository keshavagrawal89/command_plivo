# Create your views here.

import os
import plivo

from plivo_annyang.models import *
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings



def main_page(request):
	variables = {'':''}
	
	return render_to_response('main_page.html', RequestContext(request, variables))


def master_server(request):
	request_type = request.POST.get('target_input')
	if (request_type == 'plivo status') or (request_type == 'plivostatus'):
		variables = {'':''}
		return render_to_response('status.html', RequestContext(request, variables))

	elif(request_type == 'total numbers'):
		plivo_api = get_plivo_api()
		status, data = plivo_api.get_numbers()

		numbers_count = data['meta']['total_count']
		variables = {'numbers_count':numbers_count}

		return render_to_response('numbers.html', RequestContext(request, variables))
	else:
		variables = {'':''}
		return render_to_response('main_page.html', RequestContext(request, variables))

def get_plivo_api():
	auth_id = settings.AUTH_ID
	auth_token = settings.AUTH_TOKEN

	return plivo.RestAPI(auth_id = auth_id, auth_token = auth_token)
