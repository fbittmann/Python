


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python




def primgenerator(n = 2):
	"""Generiert konsekutive Primzahlen groesser gleich n"""
	if n == 2:
		yield 2
		n = 3
	if n % 2 == 0:
		n += 1
	
	while True:
		for teiler in range(3, int(n**0.5 + 1), 2):
			if n % teiler == 0:
				break
		else:			#break nie ausgeloest
			yield n
		n += 2


	
#Generator aufrufen
a = primgenerator()
for i in range(5):
	print(next(a))
	
#Mit islice
import itertools
a = primgenerator()
print(list(itertools.islice(a, 100, 120)))


########################################################################
### Aufgabe 1 ###
########################################################################

t = primgenerator()
res= [next(t) for i in range(5000)]
print(res[:20])


########################################################################
### Aufgabe 2 ###
########################################################################
"""Hier suchen wir nun Primzahlzwillinge und Primzahldrillinge"""

zwillinge = 0
for i in range(0, len(res) - 1):
	if res[i] + 2 == res[i + 1]:
		zwillinge += 1
print("Gefundene Zwillinge:", zwillinge)


"""Achtung, Drillinge haben die Form (p, p+2, p+6), siehe
https://de.wikipedia.org/wiki/Primzahltupel#Primzahldrilling"""
drillinge = 0
for i in range(0, len(res) - 2):
	if res[i] + 2 == res[i + 1] and res[i] + 6 == res[i + 2]:
		drillinge += 1
print("Gefundene Zwillinge:", drillinge)



########################################################################
### Aufgabe 3 ###
########################################################################
"""Unser Vorgehen zum Finden einer Semiprimzahl ist zweistufig.
Zunächst müssen wir die Zahl Faktorisieren und dann testen, ob beide
Faktoren Prinzahlen sind. Ist dies der Fall, so müssen wir prüfen,
ob diese beiden Teiler jeweils
Primzahlen sind. Dann ist eine Semiprimzahl gefunden, andernfalls nicht"""


def primtest(n):
	"""Testet, ob n prim ist"""
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5 + 1), 2):
		if n % i == 0:
			return False
	else:
		return True

def semiprimzahl(n):
	"""Testet, ob n semiprim ist"""
	for i in range(2, n//2):
		if n % i == 0:
			j = n // 2
			if primtest(i) == True and primtest(j) == True:
				return True
			else:
				return False
	return False

print(semiprimzahl(35))
print(semiprimzahl(12))

