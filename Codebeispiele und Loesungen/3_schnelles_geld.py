


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python


import random


def spiel(zielsumme):
	einkommen = 20
	runde = 0
	guthaben = 0
	kaufzeitpunkt_maschinen = []
	while guthaben < zielsumme:
		runde += 1
		guthaben += einkommen + runde
		zinsen = sum(0.05 if runde - t <= 10 else 0.03 for t in kaufzeitpunkt_maschinen)
		guthaben += guthaben * zinsen
		preis = 50 * 2 ** len(kaufzeitpunkt_maschinen)
		if guthaben >= preis and len(kaufzeitpunkt_maschinen) < 5:
			kaufzeitpunkt_maschinen.append(runde)
			guthaben -= preis
	return runde, kaufzeitpunkt_maschinen
	

print(spiel(5000))


def spiel2(bestmarke, zielsumme):
	einkommen = 20
	runde = 0
	guthaben = 0
	kaufzeitpunkt_maschinen = []
	while guthaben < zielsumme:
		if runde >= bestmarke:
			return None
		runde += 1
		guthaben += einkommen + runde
		zinsen = sum(0.05 if runde - t <= 10 else 0.03 for t in kaufzeitpunkt_maschinen)
		guthaben += guthaben * zinsen
		preis = 50 * 2 ** len(kaufzeitpunkt_maschinen)
		if guthaben >= preis and len(kaufzeitpunkt_maschinen) < 5 and random.randint(0, 1) == 1:
			kaufzeitpunkt_maschinen.append(runde)
			guthaben -= preis
	return runde, kaufzeitpunkt_maschinen


print(spiel2(9999, 5000))


def simulation(n):
	bestmarke = 999
	for i in range(n):
		output = spiel2(bestmarke, 5000)
		if output:
			bestmarke, zugfolge = output
	return bestmarke, zugfolge
	

"""Einkommentieren zum Ausfuehren"""	
# ~ print(simulation(10 ** 6))



########################################################################
### Aufgabe 1 ###
########################################################################

def computer1(p_ausfall):
	startwert = p_ausfall
	platinen = 0
	zeit = 0
	while zeit < 168:
		if random.random() < p_ausfall:
			zeit += 6
			p_ausfall = startwert
		else:
			platinen += 1
			p_ausfall += 0.002
			zeit += 1
	return platinen
	
	
def sim1(p_ausfall, reps):
	"""Wie viele Platinen werden im Schnitt produziert?"""
	return sum(computer1(p_ausfall) for i in range(reps)) / reps
	
"""Baseline bei 0.05"""	
print(sim1(0.05, 9000))
		
		
		
########################################################################
### Aufgabe 2 ###
########################################################################

def sim2():
	for p in range(10, 60, 2):		#Von 1% zu 6% in Schritten von 0,2%
		print("Basline-Ausfallwahrscheinlichkeit:", p / 1000)
		print(round(sim1(p / 1000, 9000), 2))
		print("******************************************")
		

"""Wie hoch darf die Baseline maximal sein fuer min. 120 Platinen pro
Woche?"""		
sim2()
