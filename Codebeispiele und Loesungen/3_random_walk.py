


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python


import math
import time
import random

def randomwalk(steps):
	position = (0, 0)
	for i in range(steps):
		zufall = random.random() * 360
		xpos = position[0] + math.cos(math.radians(zufall))
		ypos = position[1] + math.sin(math.radians(zufall))
		position = (xpos, ypos)
	return position
	
	
def randompos(position, nzeilen, nspalten):
	while True:
		zufall = random.random() * 360
		xpos = position[0] + math.sin(math.radians(zufall))
		ypos = position[1] + math.cos(math.radians(zufall))
		position = (xpos, ypos)
		gridpos = postogrid(position, nzeilen, nspalten)
		if 0 <= gridpos[1] <= nzeilen - 1 and 0 <= gridpos[0] <= nspalten - 1:
			return position
			
			
def postogrid(position, nzeilen, nspalten):
	xpos, ypos = position	#tuple unpacking
	spaltenpos = int(xpos + nspalten / 2)
	zeilenpos = int(-ypos + nzeilen / 2)
	return (spaltenpos, zeilenpos)

def partikel_anzeigen(partikel, n_zeilen, n_spalten):
	screen = [[" "] * n_spalten for _ in range(n_zeilen)]
	for element in partikel:
		xgrid, ygrid = postogrid(element, n_zeilen, n_spalten)
		screen[ygrid][xgrid] = "*"
	print("#" * (n_spalten + 2))
	for zeile in screen:
		print(f"#{''.join(zeile)}#")
	print("#" * (n_spalten + 2))



FPS = 10
def main(n, n_zeilen=18, n_spalten=50):
	partikel = [(0, 0)] * n # hier erlaubt, weil Tuple unveraenderlich sind.
	while True:
		partikel = [randompos(p, n_zeilen, n_spalten) for p in partikel]	
		partikel_anzeigen(partikel, n_zeilen, n_spalten)
		time.sleep(1 / FPS)
		

# ~ main(10)


########################################################################
### Aufgabe 1 ###
########################################################################
"""Will man direkt in Radiant rechnen, so ist der Definitionsbereich auf
0 bis 2 Pi (ca. 6.28) zu beschraenken"""

def randomwalk2(steps):
	position = (0, 0)
	for i in range(steps):
		zufall = random.random() * 6.283185
		xpos = position[0] + math.cos(zufall)
		ypos = position[1] + math.sin(zufall)
		position = (xpos, ypos)
	return position


########################################################################
### Aufgabe 2 ###
########################################################################

"""Wir aendern die Funktion so ab, sodass verschiedene Symbole benutzt werden"""

def partikel_anzeigen2(partikel, n_zeilen, n_spalten):
	screen = [[" "] * n_spalten for _ in range(n_zeilen)]
	for element in partikel:
		xgrid, ygrid = postogrid(element[0], n_zeilen, n_spalten)
		screen[ygrid][xgrid] = element[1]
	print("#" * (n_spalten + 2))
	for zeile in screen:
		print(f"#{''.join(zeile)}#")
	print("#" * (n_spalten + 2))
	
		
FPS = 10
def main2(n, n_zeilen=18, n_spalten=50):
	symbole = ["*", "#", "@", "+", "o"]
	partikel = [((0, 0), random.choice(symbole)) for i in range(n)]
	while True:
		partikel = [[randompos(p[0], n_zeilen, n_spalten), p[1]] for p in partikel]	
		partikel_anzeigen2(partikel, n_zeilen, n_spalten)
		time.sleep(1 / FPS)

# ~ main2(10)


########################################################################
### Aufgabe 3 ###
########################################################################


FPS = 10
def main3(n, n_zeilen=18, n_spalten=50):
	symbole = ["*", "#", "@", "+", "o"]
	partikel = [((random.randint(0, n_spalten), random.randint(0, n_zeilen)), random.choice(symbole)) for i in range(n)]
	while True:
		partikel = [[randompos(p[0], n_zeilen, n_spalten), p[1]] for p in partikel]	
		partikel_anzeigen2(partikel, n_zeilen, n_spalten)
		time.sleep(1 / FPS)
		
# ~ main3(10)
