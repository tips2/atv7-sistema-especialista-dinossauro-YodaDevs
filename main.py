from classDiagnostico import *
from classPerguntas import *

#Inferência
se = Diagnostico()
pergunta = Pergunta()


while se.probabilidade() != 100:
	string = pergunta.texto()
	se.pergunta(string[0],string[1])
	print('probabilidade é %d' %(se.probabilidade()))
	print(se.resultado)
	if se.probabilidade() == 100:
		print('Seu dinossauro é um: ',se.resultado[0])