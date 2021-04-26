from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['\n-------------------------------\nSistema Especialista Dinossauro\n-------------------------------\n\n---Descubra seu Dino!---\n\nSeu Dinossauro é Hérbivoro?\nResponda com s ou n\n','herbivoro'],
		['Possui algum adorno na face?','adorno'],
		['É grande?','grande'],		
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
