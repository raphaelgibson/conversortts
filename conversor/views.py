from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Audio
from .forms import AudioForm

from gtts import gTTS
from django.core.files import File

def home(request):
	if request.method == 'POST':
		form = AudioForm(request.POST)
		if form.is_valid():
			form.save()
			audios = Audio.objects.all()
			return render(request, 'conversor/audio.html', {'audios': audios})
	else:
		audios = Audio.objects.all()
		for audio in audios:
			audio.delete()

		form = AudioForm()
		return render(request, 'conversor/index.html',
		{'form': form})

def gerar(request):
	audio = audio.objects.all()
	return render(request, 'conversor/audio.html', {'audio': audio})

def download(request, id):
	audio = get_object_or_404(Audio, pk = id)
	arq = gTTS(audio.texto, lang = 'pt-br')
	arq.save('staticfiles/{}.mp3'.format(audio.nome))
	f = open('staticfiles/{}.mp3'.format(audio.nome), 'rb')
	myfile = File(f)
	response = HttpResponse(myfile, content_type = 'audio/mpeg3')
	response['Content-Disposition'] = u"attachment; filename = %s.mp3" % audio.nome
	return response