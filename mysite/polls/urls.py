from django.conf.urls import url
from .import views

urlpatterns = [

    url('^$', views.index, name ="index"),
    #127.0.0.1/polls/

]