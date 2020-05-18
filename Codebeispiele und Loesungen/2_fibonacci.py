


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python


def fibonacci(n):
	assert n > 0
	a, b  = 1, 1
	for i in range(n):
		print(a)
		a, b = b, a + b
		

def fibonacci2(n):
	glieder = [1, 1]
	for i in range(n):
		glieder.append(glieder[-1] + glieder[-2])
	return glieder[:-2]


def fibonacci3(n):
	glieder = {1:1, 2:1}
	def inner(n):
		if n not in glieder:
			folgeglied = inner(n-1) + inner(n-2)
			glieder[n] = folgeglied
		return glieder[n]			
	return inner(n)
	
	
########################################################################
### Aufgabe 1 ###
########################################################################
a1 = fibonacci2(5000)
print(a1)




########################################################################
### Aufgabe 2 ###
########################################################################
"""Das Problem bei dieser Formel ist, dass die Genauigkeit der Ergebnisse
von den Nachkommastellen abhängt, die in die Analysen einbezogen werden.
Werden die Zahlen zu groß, so "verliert" man Nachkommastellen und die
Ergebnisse werden falsch insofern muss dann beispielsweise das Modul
Decimal genutzt werden. Sehen wir uns ein Beispiel für das Problem an."""

def binet(i):
	"""Erzeugt die i-te Fibonacci-Zahl ueber die Formel von Moivre-Binet"""
	return int((1 / (5**0.5)) * (((1 + 5**0.5) / 2)**i - ((1 - 5**0.5) / 2)**i))
	
a = fibonacci2(2000)
n1 = 10
print(binet(n1 + 1), a[n1])
#Die Ergebnisse stimmen überein

n2 = 1000
print(binet(n2 + 1) == a[n2])
#Das Ergebnis stimmt nicht mehr
	

"""Zum Verständnis picken wir uns einen Term aus der Gleichung heraus und
schauen diesen im Detail an. Wir sehen etwa, dass Wurzel(5) insgesamt drei
Mal vorkommt. Diese Zahl ist nun aber irrational, hat also unendlich viele
Nachkommastellen. Für ein detailliertes Ergebnis müssen wir also zunächst
diese Zahl mit sehr vielen Nachkommastellen bereitstellen und dann berechnen.
Andernfalls werden wir für große Zahlen falsche Ergebnisse erhalten. Eine
Umsetzung ist auf verschiedene Arten möglich. Hierbei sieht man, dass einem
auch durch die Formel "nichts geschenkt wird". Ob man nun also sehr viele
Nachkommastellen vorhalten möchte oder lieber gleich einfach alle vorher-
gehenden Terme aufsummiert, bleibt einem selbst überlassen."""
	

########################################################################
### Aufgabe 3 ###
########################################################################
import time

tstart = time.time()
x1 = fibonacci2(500)
tend = time.time()
print("Zeit mit regulaerer Formel:")
print(round(tend - tstart, 4))


tstart = time.time()
x2 = [fibonacci3(i + 1) for i in range(500)]
tend = time.time()
print("Zeit mit Rekursionsalgorithmus:")
print(round(tend - tstart, 4))
assert x1 == x2 
	
########################################################################
### Aufgabe 4 ###
########################################################################
golden = (1 + 5 ** 0.5) / 2
glieder = fibonacci2(10 ** 5)
for n in (1, 2, 3, 4, 5):
	empratio = glieder[(10 ** n) - 1] / glieder[(10 ** n) - 2]
	abweichung = abs(golden / empratio)
	print(n, empratio, abweichung)
#Wie erkennbar wird, reichen bereits 100 Zahlen aus, um eine sehr gute Näherung zu erhalten

########################################################################
### Aufgabe 5 ###
########################################################################	
#Summe der Kehrwerte der ersten 5000 Glieder
glieder = fibonacci2(5000)
summe = 0
for element in glieder:
	summe += 1 / element 
print("Summe der Kehrwerte:", summe)

########################################################################
### Aufgabe 6 ###
########################################################################
def zeckendorf(n):
	"""Zerlegt eine natuerliche Zahl n in eine oder mehrere Fibonacci-
	Zahlen, wobei direkt aufeinanderfolgende Fibonacci-Zahlen nicht
	vorkommen duerfen"""
	zahlen = fibonacci2(n + 1)
	zahlen.sort(reverse=True)
	result = ""
	skip = False
	for pos, zahl in enumerate(zahlen):
		if skip:
			skip = False
			continue
		if zahl <= n and n - zahl >= 0:
			n -= zahl
			result += str(len(zahlen) - pos)
			skip = True
		if n == 0:
			return result
			
print(zeckendorf(19))			
	

	
########################################################################
### Aufgabe 7 ###
########################################################################


"""Der Trick ist es, einen Default zu benutzen, der beim ersten Aufruf ignoriert werden kann,
aber dann bei den inneren Aufrufen immer explizit das Dict mit den gespeicherten Werten
mitführt"""

def fibonacci4(n, glieder = None):
	if glieder == None:
		glieder = {1:1, 2:1}
	if n in glieder:
		return glieder[n]
	else:
		folgeglied = fibonacci4(n-1, glieder) + fibonacci4(n-2, glieder)
		glieder[n] = folgeglied
		return folgeglied
