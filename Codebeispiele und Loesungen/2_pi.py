


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python



import math
import itertools

def arctan(z, stellen):
    extra_stellen = math.ceil(math.log10(stellen / math.log10(z)))
    vorzeichen = -1
    term = 10 ** (stellen + extra_stellen) // z
    ergebnis = term
    for potenz in itertools.count(3, 2):
        term //= z ** 2
        if term < 1:
            break
        ergebnis += (vorzeichen * term) // potenz
        vorzeichen *= -1
    return ergebnis // (10**extra_stellen)
	
	
def pi(stellen):
	return 4 * (4 * arctan(5, stellen) - arctan(239, stellen))
	
	
print(pi(30))

########################################################################
### Aufgabe 1 ###
########################################################################


import time


tstart = time.time()
a = pi(2500)
dauer = time.time() - tstart
print("Zeitdauer:", dauer)



tstart = time.time()
a = pi(5000)
dauer = time.time() - tstart
print("Zeitdauer:", dauer)


"""Offenbar waechst die Zeitdauer nicht linear!"""


########################################################################
### Aufgabe 2 ###
########################################################################
"""ggf. einkommentieren, um lange Laufzeit zu vermeiden"""
# ~ vielestellen = str(pi(20_000))

# ~ tel = "9345699"
# ~ datum = "19951206"
# ~ print(tel in vielestellen)
# ~ print(datum in vielestellen)



########################################################################
### Aufgabe 2 ###
########################################################################

def euler(stellen):
	"""Berechnet die Euler'sche Zahl beliebig genau"""
	stellen += 10		#Zur Sicherheit etwas erhoehen
	totale_summe = 2 * (10**stellen)	#Erste beide Terme der Reihe
	nenner = 1
	counter = 2
	term = None
	while term != 0:
		nenner = nenner * counter
		term = (10**stellen) // nenner
		totale_summe = totale_summe + term
		counter += 1
	return int(str(totale_summe)[:-10])	#Zusaetzliche Stellen wieder entfernen
	
print(euler(100))
		
