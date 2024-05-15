import random
import requests
import logging

from django.db.models import Sum
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed, Http404
from simplejson import JSONDecodeError

from . import REQUEST_URL
from .models import Quote


def index(request):

    try:
        q = get_random_quote()
    except QuoteFetchError:
        q = get_random_saved_quote()

    return do_response(request, q)


def get(request, id):
    q = get_object_or_404(Quote, id=id)
    return do_response(request, q)


def like(request, id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    q = get_object_or_404(Quote, id=id)
    q.likes += 1
    q.save()
    return redirect(q)


def get_popular(request):
    q = get_popular_quote()
    return do_response(request, q)


def do_response(request, quote):
    if request.accepts('text/html'):
        return render(request, 'quote.html', {'quote': quote})
    if request.accepts('text/json'):
        return JsonResponse(quote.as_dict())
    if request.accepts('text/plain'):
        return HttpResponse(quote.text(), content_type='text/plain')
    return JsonResponse(quote.as_dict())


def get_popular_quote():
    total_count = Quote.objects.all().count()
    if total_count < 1:
        raise Http404("No quotes available")
    likes_total = Quote.objects.filter(likes__gt=0).aggregate(Sum('likes', default=0))['likes__sum']
    rand = random.randint(0, likes_total+total_count-1)

    if rand < likes_total:
        for q in Quote.objects.filter(likes__gt=0):
            rand -= q.likes
            if rand < 0:
                return q
    else:
        return Quote.objects.all()[rand-likes_total]


def get_random_saved_quote():
    count = Quote.objects.count()
    if count < 1:
        raise Http404("No quotes available")
    return Quote.objects.all()[random.randint(0, count-1)]


def get_random_quote():
    r = requests.get(REQUEST_URL)
    if r.status_code != 200:
        logging.info(f"error getting quote: status {r.status_code}")
        raise QuoteFetchError("error fetching quote")

    logging.debug("got quote, status code 200")

    try:
        json = r.json()
        id, author, quote = (json['_id'], json['author'], json['content'])
    except (KeyError, JSONDecodeError):
        logging.warning(f"error parsing quote: {r.text}")
        raise QuoteFetchError('error parsing quote')

    q, created = Quote.objects.get_or_create(id=id)
    if created:
        q.author = author
        q.quote = quote
        q.save()

    return q


class QuoteFetchError(Exception):
    pass