from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("popular/", views.get_popular, name='popular'),
    path("<str:id>/", views.get, name='id'),
    path("<str:id>/like", views.like, name='like'),
]