from django.db import models

class Audio(models.Model):

	idiomas = [('de', 'Alemão'),
				('ca', 'Catalão'),
				('zn-cn', 'Chinês'),
				('ko', 'Coreano'),
				('es-es', 'Espanhol'),
				('fr-fr', 'Francês'),
				('en-ca', 'Inglês (Canadá)'),
			    ('en-us', 'Inglês (EUA)'),
			    ('en-uk', 'Inglês (Reino Unido)'),
			    ('ja', 'Japonês'),
			    ('la', 'Latim'),
				('pt-br', 'Português (BR)'), 
				('pt-pt', 'Português (PT)'),
				('ru', 'Russo')]

	nome_do_arquivo = models.CharField(max_length = 255, 
							help_text = 'Não utilize acento no nome do arquivo.')

	texto = models.TextField()

	idioma = models.CharField(
		max_length = 255,
		choices = idiomas,
		default = ('pt-br', 'Português')
		)

	def __str__(self):
		return self.nome_do_arquivo

