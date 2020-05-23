


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python


import time
import random
import statistics as stats


def speedtest(funktionen, n):
	assert isinstance(funktionen, list), "Funktionen in einer Liste gesammelt uebergeben"
	zeiten = {f: [] for f in funktionen}
	for durchgang in range(n):
		random.shuffle(funktionen)
		for funktion in funktionen:
			start_time = time.monotonic()
			funktion()
			end_time = time.monotonic()
			zeiten[funktion].append(end_time - start_time)
	for funktion, laufzeit in zeiten.items():
		print(f"{funktion} | Mittelwert: {stats.mean(laufzeit):.3f} Median: {stats.median(laufzeit):.3f}")



########################################################################
### Aufgabe 1 ###
########################################################################
"""Zum Testen dieser Funktion nutzen wir hier beide Funktionen.
Beide erstellen eine Liste mit den ersten 500.000 Zahlen. Was ist schneller,
eine Schleife mit while oder eine list-comprehension?"""


def whilecounter(n=50_000):
	output = []
	counter = 0
	while counter < n:
		output.append(counter)
		counter += 1
	return output
	
	
def comprehension(n=50_000):
	return [i for i in range(n)]
	
	

speedtest([whilecounter, comprehension], 25)

#Wie man sieht, ist die comprehension etwa um den Faktor 3 schneller




########################################################################
### Aufgabe 2 ###
########################################################################
"""Hier definieren wir zuerst den Decorator als normale Funktion. Diesen
bringen wir dann an der neuen Funktion tester an und schauen, ob alles
klappt"""

def zeitenmesser(func, *args, **kwargs):
	def inner(*args, **kwargs):
		t_start = time.monotonic()
		res = func(*args, **kwargs)
		t_end = time.monotonic()
		runtime = round(t_end - t_start, 3)
		print(f"Runtime: {runtime}")
		return res
	return inner
	
"""Hier wird nun tester dekoriert und definiert"""	
@zeitenmesser	
def tester(n):
	time.sleep(0.5)
	return [i for i in range(n)]

print(tester(50))




########################################################################
### Aufgabe 3 ###
########################################################################
"""Moechte man Funktionen mit Argumenten uebergeben, so nutzt man partial
aus dem Modul functools"""

import functools
f1 = functools.partial(whilecounter, 50_000)
f2 = functools.partial(comprehension, 50_000)
speedtest([f1, f2], 25)

