from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('audio', views.gerar),
	path('audio/<int:id>/download', views.download)

]