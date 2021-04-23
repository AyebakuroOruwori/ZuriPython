from django.conf.urls import url
from . import views

urlpatterns = [

    url('^$', views.index, name="index"),
    #127.0.0.1/polls/
    url('^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    #127.0.0.1/polls/1
    url('^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
    #127.0.0.1/polls/1/results
    url('^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
    #127.0.0.1/Polls/1/vote
]