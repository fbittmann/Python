


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python

from itertools import combinations

def abstand(p1, p2):
	"""Abstand zweier Punkte"""
	xdiff = p1[0] - p2[0]
	ydiff = p1[1] - p2[1]
	return (xdiff**2 + ydiff**2)**0.5


def bruteforce(punkte):
    """Findet die zwei Punkte mit der geringsten Distanz per Brute Force"""
    return min(
        (abstand(*punkte_paar), punkte_paar)
        for punkte_paar in combinations(punkte, 2)
    )

	
	
def mindistanz(punktliste):
	"""Findet die zwei Punkte mit der geringsten Distanz ueber Teilen und Herrschen"""
	laenge = len(punktliste)	
	if laenge < 5:		#Base Case
		return bruteforce(punktliste)
	
	punkte_links = punktliste[:laenge//2]
	punkte_rechts = punktliste[laenge//2:]
	min_links = mindistanz(punkte_links)
	min_rechts = mindistanz(punkte_rechts)
	d = min(min_links, min_rechts)[0]
	limit_links = [p for p in punkte_links if abs(p[0] - punkte_rechts[0][0]) <= d]
	limit_rechts = [p for p in punkte_rechts if abs(p[0] - punkte_links[-1][0]) <= d]
	distanzen = [min_links, min_rechts]
	for x in limit_links:
		for y in limit_rechts:
			distanzen.append((abstand(x, y), (x, y)))
	return min(distanzen)
	
	
import time
import random

def main():
	random.seed(1234)
	allepunkte = [(random.random() * 100, random.random() * 100) for i in range(5000)]
	start = time.monotonic()
	print("Brute-Force Loesung")
	print(bruteforce(allepunkte))
	print(time.monotonic() - start)
	start = time.monotonic()
	print("Verbesserte Loesung")
	allepunkte.sort()
	print(mindistanz(allepunkte))
	print(time.monotonic() - start)
	
	
# ~ print(main())


def testskript(runs, npunkte):
	random.seed(1234)
	for run in range(runs):
		allepunkte = [(random.random() * 100, random.random() * 100) for i in range(npunkte)]
		allepunkte.sort()
		assert bruteforce(allepunkte) == mindistanz(allepunkte)
	print("Alles gut!")
testskript(9, 777)


########################################################################
### Aufgabe 1 ###
########################################################################


def mindistanz2(punktliste):
	punktliste.sort()
	def inner(punktliste):
		laenge = len(punktliste)	
		if laenge < 5:		#Base Case
			return bruteforce(punktliste)
		
		punkte_links = punktliste[:laenge//2]
		punkte_rechts = punktliste[laenge//2:]
		min_links = inner(punkte_links)
		min_rechts = inner(punkte_rechts)
		d = min(min_links, min_rechts)[0]
		limit_links = [p for p in punkte_links if abs(p[0] - punkte_rechts[0][0]) <= d]
		limit_rechts = [p for p in punkte_rechts if abs(p[0] - punkte_links[-1][0]) <= d]
		distanzen = [min_links, min_rechts]
		for x in limit_links:
			for y in limit_rechts:
				distanzen.append((abstand(x, y), (x, y)))
		return min(distanzen)
	return inner(punktliste)



