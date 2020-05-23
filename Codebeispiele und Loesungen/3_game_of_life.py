


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python


import time
import random


def erzeuge_naechsten_schritt(spielfeld):
	neues_spielfeld = []
	for y, zeile in enumerate(spielfeld):
		neue_zeile = []
		for x, feld in enumerate(zeile):
			nachbarn = zaehle_nachbarn((x,y), spielfeld)
			if feld and nachbarn == 2:
				feld = True
			elif nachbarn == 3:
				feld = True
			else:
				feld = False
			neue_zeile.append(feld)
		neues_spielfeld.append(neue_zeile)
	return neues_spielfeld


def game_of_life(runden):
	spielfeld = [
		[random.random() < 0.10 for x in range(50)]
		for y in range(18)
	]
	for i in range(runden):
		zeichne_feld(spielfeld)
		spielfeld = erzeuge_naechsten_schritt(spielfeld)
		time.sleep(0.6)
		
		
def zaehle_nachbarn(position, spielfeld):
	nachbarn = 0
	for x in (-1, 0, 1):
		for y in (-1, 0, 1):
			if x == y == 0:
				continue
			xpos, ypos = position[0] + x, position[1] + y
			if 0 <= xpos < len(spielfeld[0]) and 0 <= ypos < len(spielfeld):
				nachbarn += spielfeld[ypos][xpos]
	return nachbarn
	

def zeichne_feld(spielfeld):
	for zeile in spielfeld:
		print("".join("#" if zelle else " " for zelle in zeile))
	print("#" * len(zeile))

	
	
# ~ game_of_life(30)



########################################################################
### Aufgabe 1 ###
########################################################################
#https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens#Raumschiffe_und_Gleiter
"""Hier wollen wir nun eine Funktion erstellen, die an einer Stelle im
Spielfeld einen Gleiter einfuegt"""

def gleiter(position, spielfeld):
	output = spielfeld[:]
	xpos, ypos = position
	try:
		output[ypos][xpos] = 1
		output[ypos][xpos + 1] = 1
		output[ypos][xpos + 2] = 1
		output[ypos - 1][xpos] = 0
		output[ypos - 1][xpos + 1] = 0
		output[ypos - 1][xpos + 2] = 1
		output[ypos - 2][xpos] = 0
		output[ypos - 2][xpos + 1] = 1
		output[ypos - 2][xpos + 2] = 0
	except IndexError:
		"""Wenn wir den Gleiter nicht ganz einfuegen koennen, so
		soll das Spielfeld nicht veraendert werden"""
		return spielfeld
	return output


def game_of_life2(runden):
	"""Leeres Spielfeld, nur ein Gleiter vorhanden"""
	spielfeld = [
		[False for x in range(50)]
		for y in range(18)
	]
	spielfeld = gleiter((5, 5), spielfeld)
	for i in range(runden):
		zeichne_feld(spielfeld)
		spielfeld = erzeuge_naechsten_schritt(spielfeld)
		time.sleep(0.4)
		
# ~ game_of_life2(20)
