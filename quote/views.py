from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import requests
import logging


def index(request):

    r = requests.get('https://api.quotable.io/random')
    if r.status_code != 200:
        logging.info(f"error getting quote: status {r.status_code}")
        return HttpResponse('Error, unable to fetch quote', status=500)

    logging.debug("got quote, status code 200")



    return HttpResponse(r.text)


    return HttpResponse("failed")