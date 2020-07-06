from django.urls import path
from jokebotweb import views

urlpatterns = [
	path('',views.jokebot, name='jokebot'),
]
