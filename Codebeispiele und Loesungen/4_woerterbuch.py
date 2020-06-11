


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python


#Die Originale Wortliste kann hier heruntergeladen werden:
#https://en.wikipedia.org/wiki/Moby_Project
#https://github.com/Hyneman/moby-project/tree/master/moby/mlang
#Archive.org	--> Seiten durchsuchen, die inzwischen offline sind


with open("wortliste1.txt", encoding="utf-8") as datei:  
	words = [line.rstrip().lower() for line in datei]
	print(len(words))
	print(words[:5])
	print(list(words[3]))
	longwords = [wort for wort in words if len(wort) > 3]
	longwords.sort(key=len)
	print(longwords[0], longwords[-1])
	
	longwords.sort(key=lambda wort: wort[::-1])
	print(longwords[:6])

	
	#Wörter mit den meisten gs
	f = lambda wort: sum (1 for zeichen in wort if zeichen == "g")
	print(f("gartenzwerge!"))
	longwords.sort(key=lambda wort: sum(1 for zeichen in wort if zeichen == "g"), reverse = True)
	print(longwords[:3])


########################################################################
### Aufgabe 1 ###
########################################################################

def ist_palindrom(wort):
	"""Testet, ob ein Wort / String ein Palindrom ist"""
	return wort == wort[::-1]


########################################################################
### Aufgabe 2 ###
########################################################################


import random
def passwortgenerator(max_laenge, min_laenge, wortliste, anzahl):
	"""Nimmt eine Wortliste entgegen und generiert dann eine bestimmte
	Anzahl an Passwortstrings mit jeweils einer definierten maximalen
	Laenge"""
	
	allwords = []
	for i in range(anzahl):
		pw = []
		while True:
			laenge = sum(len(x) for x in pw)
			if min_laenge <= laenge <= max_laenge:
				break
			elif laenge > max_laenge:
				pw.pop(-1)
				#Hier bauen wir eine Sicherung ein und loeschen noch ein Wort mehr,
				#wenn wir fast an der Grenze sind, damit immer passende Woerter
				#gefunden werden koennen
				if sum(len(x) for x in pw) + 3 > max_laenge:
					pw.pop(-1)
			else:
				pw.append(random.choice(wortliste))
		allwords.append("".join(pw))
	for element in allwords:
		print(element)		

# ~ passwortgenerator(26, 20, words, 20)


########################################################################
### Aufgabe 3 ###
########################################################################

def diversitaet(wort):
	"""Wir berechnen die Diversitaet als die Anzahl der einmalig enthaltenen
	Buchstaben, was wir recht simpel mit einem Dict loesen"""
	histogramm = {}
	for zeichen in wort.lower():
		if zeichen not in histogramm:
			histogramm[zeichen] = 1
		else:
			histogramm[zeichen] += 1
	# ~ print(histogramm)
	einmalig = 0
	for wert in histogramm.values():
		if wert == 1:
			einmalig += 1
	return einmalig / len(wort)
	
	
# ~ print(diversitaet("Tischkreissäge"))

def tester(wortliste, mindestzeichen):
	"""Welche Woerter haben die hoechste Diversitaet?"""
	ergebnisse = [(diversitaet(wort), wort) for wort in wortliste if len(wort) >= mindestzeichen]
	ergebnisse.sort(reverse = True)
	print(ergebnisse[:10])
	
# ~ tester(words, 6)
# ~ tester(words, 15)



########################################################################
### Aufgabe 4 ###
########################################################################
def anagrammfinder(wort, wortliste):
	"""Wir suchen Anagramme zu einem gegebenen Wort"""
	def histogramm(wort):
		output = {}
		for zeichen in wort.lower():
			if zeichen not in output:
				output[zeichen] = 1
			else:
				output[zeichen] += 1
		return output
	
	anagramme = []		
	for element in wortliste:
		if len(element) == len(wort) and histogramm(element) == histogramm(wort):
			anagramme.append(element)
	return anagramme

# ~ print(anagrammfinder("sauber", words))
