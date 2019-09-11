from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Audio
from .forms import AudioForm

import os
from gtts import gTTS

from rest_framework import generics
from .serializers import AudioSerializer

def home(request):
	if request.method == 'POST':
		form = AudioForm(request.POST)
		if form.is_valid():
			form.save()
			audios = Audio.objects.all()
			for audio in audios:
				arquivo = gTTS(audio.texto, lang = audio.idioma)
				arquivo.save('conversor/media/{}.mp3'.format(audio.nome_do_arquivo))			
			return render(request, 'conversor/audio.html', {'audios': audios})
	else:
		for file in os.listdir('conversor/media'):
			if file[-1:-4:-1] == '3pm':
				os.remove('conversor/media/{}'.format(file))
					
		audios = Audio.objects.all()
		for audio in audios:
			audio.delete()

		form = AudioForm()
		return render(request, 'conversor/index.html', {'form': form})

class ttsapi(generics.ListCreateAPIView):
	queryset = Audio.objects.all()
	serializer_class = AudioSerializer
	

'''def download(request, id):
	audio = get_object_or_404(Audio, pk = id)
	myfile = open('media/{}.mp3'.format(audio.nome_do_arquivo), 'rb')
	response = HttpResponse(myfile, content_type = 'audio/mpeg3')
	response['Content-Disposition'] = u"attachment; filename = %s.mp3" % audio.nome_do_arquivo
	return response'''
