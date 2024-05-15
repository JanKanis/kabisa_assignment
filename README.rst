Kabisa quotes api
=================

This tiny api backend allows retrieving quotes from https://quotable.io


Features
--------

- Retrieve quote
- Like quote
- get random quote weighted by popularity
- content negotiation (html, text or json)
- fallback to cached quotes if quotable.io is not available


Installation
------------

This project requires python 3 to be installed. Beyond that, it only requires `django` and `requests`. If they are not installed, run::

    pip install django requests

To run the server, run::

  python3 manage.py runserver

This will run the server on http://localhost:8000/

API endpoints
-------------

All endpoints are relative to the url root, which by default is http://localhost:8000.

`/quote/`
  Return a random quote from `quotable.io`. If fetching a quote is not possible, returns a random cached quote from the database.

`/<id>/`
  Return quote with specified id. This only works for cached quotes.

`/popular/`
  Return a random quote, weighted by likes. Conceptually, all cached quotes are added to a jar. Then, for every like, that quote is added once more to the jar. Then one quote is retrieved at random.

`/<id>/like`
  (POST only) Increment the like count for the quote by 1.


Limitations and future improvements
-----------------------------------

The api listed in the assignment (http://quotes.stormconsultancy.co.uk/api) appears to be no longer available. I found https://api.quotable.io/random as a replacement.

The dependencies of this app should be codified in a `requirements.txt` file or similar.

For future extensions it may be useful to use Django Rest Framework.

There are no automated tests yet. There is very little code that is amenable to unit testing, and I didn't have time to set up integration testing.

For production deployment it is usually beneficial to package the app into a Docker container, and to use a more powerful database such as Postgres.

Use Django Rest Framework if more quote management is to be added.

The HTML view is rather ugly, but as an api endpoint this app isn't meant to be used stand-alone, and the HTML view is intended for testing and debugging.