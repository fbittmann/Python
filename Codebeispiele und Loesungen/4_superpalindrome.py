


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python
import random

def ist_palindrom(string):
	"""Testet ob ein String ein Palindrom ist"""
	return string == string[::-1]


def rest(links, rechts):
	"""Findet die Zeichenkette, die beiden Strings nicht gemeinsam ist"""
	links = "".join(links)
	rechts = "".join(rechts)
	return links[len(rechts):] or rechts[:-len(links)]


def wortfinder(wortschatz, string, wortbeginn, gesperrt):
	"""Findet passendes neues Wort"""
	if wortbeginn:
		for wort in wortschatz:
			if wort.startswith(string) and wort not in gesperrt:
				return wort
	else:
		for wort in wortschatz:
			if wort.endswith(string) and wort not in gesperrt:
				return wort
	return None			#kein passendes Wort gefunden
	
	
def main(mindestlaenge):
	with open("wortliste1.txt", encoding="utf8") as daten:
		wortschatz = [zeile.strip().upper() for zeile in daten]
	links =  ["GEIST", "ZIERT", "LEBEN"]
	rechts = ["UMNEBELT", "REIZT", "SIEG"]
	
	gesamt = "".join(links) + "".join(rechts)
	gesperrt = set()
	zuletzt_rechts = True
	while len(gesamt) < mindestlaenge or not ist_palindrom(gesamt):
		restzeichen = rest(links, rechts)
		if restzeichen == "":
			while True:
				neuwort = random.choice(wortschatz)
				if neuwort not in gesperrt:
					break
		else:
			neuwort = wortfinder(wortschatz, restzeichen[::-1], zuletzt_rechts, gesperrt)
	
		if not neuwort:					#Backtrack
			if zuletzt_rechts:
				rechts.pop(0)
				zuletzt_rechts = False
			else:
				links.pop(-1)
				zuletzt_rechts = True
		else:
			gesperrt.add(neuwort)
			if zuletzt_rechts:
				links.append(neuwort)
				zuletzt_rechts = False
			else:
				rechts.insert(0, neuwort)
				zuletzt_rechts = True
	
		gesamt = "".join(links) + "".join(rechts)
	
		print("Restzeichen: ", restzeichen)
		print("Neues Wort: ", neuwort)
		print(links, rechts)
	assert ist_palindrom(gesamt)
	return gesamt


print(main(60))
