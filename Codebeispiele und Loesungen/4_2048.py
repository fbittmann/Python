


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python


import random
import itertools


# ~ a = [[1,2,3], [4,5,6], [7,8,9]]
# ~ b = zip(*a)
# ~ for zeile in a:
	# ~ print(zeile)
# ~ print("*********")
# ~ for zeile in b:
	# ~ print(list(zeile))

	
def zusammenfassen(zahlen):
	zahlen = [z for z in zahlen if z != 0]
	for z in range(0, len(zahlen) - 1):
		if zahlen[z] == zahlen[z + 1]:
			zahlen[z] = zahlen[z] * 2
			zahlen[z + 1] = 0
	zahlen = [z for z in zahlen if z != 0]
	return zahlen + [0 for z in range(4 - len(zahlen))]
	
	
def move(feld, richtung):
	"""Berechnet das Feld nach einem Zug neu"""
	if richtung == "links":
		feld = [zusammenfassen(zeile) for zeile in feld]
	elif richtung == "rechts":
		feld = [zusammenfassen(zeile[::-1])[::-1] for zeile in feld]
	elif richtung == "oben":
		feld = [zusammenfassen(zeile) for zeile in zip(*feld)]
		feld = [list(t) for t in zip(*feld)]
	elif richtung == "unten":
		feld = [zusammenfassen(zeile[::-1])[::-1] for zeile in zip(*feld)]
		feld = [list(t) for t in zip(*feld)]
	return feld
		
		
def neuezahl(feld):
	"""Fuegt an einer Zufallsposition in ein leeres Feld die Zahl 2 ein"""
	output = feld[:]
	spaltenpos = [0, 1, 2, 3]
	zeilenpos = [0, 1, 2, 3]
	random.shuffle(spaltenpos)
	random.shuffle(zeilenpos)
	for zeile in zeilenpos:
		for spalte in spaltenpos:
			if output[zeile][spalte] == 0:
				output[zeile][spalte] = 2
				return output
	return output
	
	
def spiel_gewonnen(feld):
    """Testet, ob das Spiel gewonnen ist"""
    return any(512 in zeile for zeile in feld)


def anzeigen(feld, zug, score):
	"""Stellt das feld grafisch in der Konsole dar"""
	mapping = {0: "[  ]", 2: "[2¹]", 4: "[2²]", 8: "[2³]", 16: "[2⁴]", 32: "[2⁵]", 64: "[2⁶]", 128: "[2⁷]", 256: "[2⁸]",
	512:"[2⁹]"}
	for zeile in feld:
		for spalte in zeile:
			print(mapping[spalte], end= "")
		print("")
	print("================")
	print("Aktueller Zug:", zug)
	print("Score:", score)
	
	
TASTEN = {
    "\x1b[D": "links",
    "\x1b[C": "rechts",
    "\x1b[A": "oben",
    "\x1b[B": "unten",
}


def main():
	feld = [[0] * 4 for _ in range(4)]
	feld [3][0] = 2
	feld [3][1] = 2
	for zug in itertools.count(1):
		score = sum(sum(zeile) for zeile in feld)
		anzeigen(feld, zug, score)
		if spiel_gewonnen(feld):
			break
		while True:
			eingabe = input()
			if eingabe in TASTEN:
				break
			print("Ungueltige Eingabe! Nur Pfeiltasten benutzen!")
		feld = move(feld, TASTEN[eingabe])
		feld = neuezahl(feld)
		for _ in range(40):
			print()
	print("Gewonnen!")

			
			
main()


########################################################################
### Aufgabe 1 ###
########################################################################

def ist_spiel_verloren(feld):
	"""Es werden alle Züge ausprobiert. Ist keiner mehr möglich, so ist das Spiel
	verloren"""
	for zug in ("links", "rechts", "unten", "oben"):
		if feld != move(feld, zug):
			return False
	return True
			
