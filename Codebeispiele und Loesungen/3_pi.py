


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python


import random

def pi2(n):
	innen = 0
	for i in range(n):
		x, y = random.random(), random.random()
		distanz = (x**2 + y**2)**0.5
		if distanz <= 1:
			innen += 1
	return 4 * (innen / n)
	
	
	
########################################################################
### Aufgabe 1 ###
########################################################################

import math
import statistics as stats

def pitester():
	referenz = str(math.pi)
	for prez in (2, 3, 4, 5, 6, 7):
		korrekt = []
		for runde in range(50):
			res = str(pi2(10 ** prez))
			counter = 0
			for i in range(len(res)):
				if referenz[i] == res[i]:
					counter += 1
				else:
					break
		korrekt.append(counter)
		print("Stellen:", 10**prez)
		print("Korrekt im Schnitt:", stats.mean(korrekt))


"""Hier einkommentieren"""		
# ~ pitester()	


########################################################################
### Aufgabe 2 ###
########################################################################


def monty(wechsel):
	"""Die Idee hier ist folgende: der Spielleiter öffnet garantiert eine Tuer mit einer Ziege und man wechselt garantiert.
	Hat man am Anfang eine Ziege gewaehlt, so ist man danach garantiert beim Gewinn. Umgekehrt: hat man bei der ersten Wahl
	den Gewinn gewaehlt, so hat man danach eine Ziege. Somit drehen wir hier nur die Wahlen um."""
	stage = [0, 0, 1]		#Zwei Ziegen, ein Gewinn
	random.shuffle(stage)
	wahl1 = random.randint(0, 2)
	if wechsel == False:
		if stage[wahl1] == 1:
			return True
		else:
			return False
	else:
		if stage[wahl1] == 1:	#Anfangs Gewinn, jetzt Niete
			return False
		else:
			return True			#Anfangs Niete, jetzt Gewinn
		
		
def simulation(n):
	win_wechsel = sum([monty(wechsel = True) for i in range(n)]) / n
	win_keinwechsel = sum([monty(wechsel = False) for i in range(n)]) / n

	print("Siegchancen beim Wechsel:", win_wechsel)
	print("Siegchancen beim Beibehalten der 1. Wahl:", win_keinwechsel)
	
"""Hier einkommentieren"""		
# ~ simulation(5000)


########################################################################
### Aufgabe 3 ###
########################################################################
import math
def geburtstag_formel(n):
	"""Wie hoch ist die Wahrscheinlichkeit, dass bei n Personen in einer Gruppe
	mindestens 2 am gleichen Tag Geburtstag haben?"""
	return 1 - (math.factorial(365) / (math.factorial(365 - n) * (365 ** n)))
	

def geburtstag_statistik(n, runs=5000):
	"""Wie hoch ist die Wahrscheinlichkeit, dass bei n Personen in einer Gruppe
	mindestens 2 am gleichen Tag Geburtstag haben?"""
	def doubledates(n):
		dates = random.choices(range(365), k=n)
		seen = set()
		for element in dates:
			if element not in seen:
				seen.add(element)
			else:
				return True
		return False
	
	ohne_doppelung = sum(doubledates(n) for i in range(runs))
	return mit_doppelung / runs

"""Hier einkommentieren"""		
# ~ print(geburtstag_formel(25))
# ~ print(geburtstag_statistik(25))


########################################################################
### Aufgabe 4 ###
########################################################################
def lottosimulation(zahlen, ziehungen):
	"""Wie hoch ist der durchschnittliche Gewinn nach einer bestimmten
	Anzahl an Lottoziehungen? Die eigenen Zahlen werden als Liste uebergeben
	wobei die letzte Zahl fuer die Superzahl steht"""
	assert len(zahlen) == 7 and 0 <= zahlen[-1] <= 9
	lottozahlen = range(1, 50)	#1-49
	superzahl = range(0, 10)	#0-9
	quote = {(2, 1): 5, (3, 0): 10, (3, 1): 20, (4, 0): 42, (4, 1): 109,
		(5, 0): 3340, (5, 1): 10022, (6, 0): 574596, (6, 1): 8949642}
	gewinn = 0
	for i in range(ziehungen):
		z1 = list(random.sample(lottozahlen, k=6))
		z2 = random.choice(superzahl)
		korrekt = sum(1 for zahl in zahlen[:-1] if zahl in z1)
		if zahlen[-1] == z2:
			korrekt_superzahl = 1
		else:
			korrekt_superzahl = 0
		if (korrekt, korrekt_superzahl) in quote:
			gewinn += quote[(korrekt, korrekt_superzahl)]
	return gewinn - (1.5 * ziehungen)		#Ein Spiel kostet 1,50
	
print(lottosimulation([22, 47, 3, 5, 30, 11, 6], 52 * 50))


