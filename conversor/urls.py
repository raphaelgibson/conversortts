from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'conversor'

urlpatterns = [
	path('', views.home, name = 'homepage'),
	url('audio/', views.ttsapi.as_view(), name='audio'),
]
