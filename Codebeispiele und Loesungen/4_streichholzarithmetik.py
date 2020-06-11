


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python



n_gleich = ["1+", "+=", "23", "35", "90", "60", "69"]
n_anders = ["-+", "-=", "17", "39", "56", "59", "68", "98", "08"]


def replace_at_index(string, index, zeichen):
	"""Ersetzt in einem String ein Zeichen an einer bestimmten Stelle"""
	return string[:index] + zeichen + string[index+1:]

# ~ print(replace_at_index("Maus", 0, "H"))
	


def add_match(string):
	"""Ersetzt systematisch Zeichen bei Hinzufügen eines Holzes"""
	for i, char in enumerate(string):
		for less, more in n_anders:
			if char == less:
				yield replace_at_index(string, i, more)


def change_match(string):
	for i, char in enumerate(string):
		for char1, char2 in n_gleich:
			if char == char1:
				yield replace_at_index(string, i, char2)
			if char == char2:
				yield replace_at_index(string, i, char1)
		for less, more in n_anders:
			if char == more:
				one_match_less = replace_at_index(string, i, less)
				yield from add_match(one_match_less)


def solver(gleichung):
	for kandidat in change_match(gleichung):
		if kandidat.count("=") == 1:
			try:
				if eval(kandidat.replace('=','==')):
					return kandidat
			except SyntaxError:
				pass
	raise RuntimeError("Keine Lösung gefunden")

print(solver("185+15=270"))

	
	
########################################################################
### Aufgabe 1 ###
########################################################################

def solver2(gleichung):
	"""Hier werden nun alle denkbaren Loesungen gesucht, was aber deutlich
	laenger dauern kann"""
	gefunden = []
	for kandidat in change_match(gleichung):
		if kandidat.count("=") == 1:
			try:
				if eval(kandidat.replace('=','==')):
					gefunden.append(kandidat)
			except SyntaxError:
				pass
	if gefunden:
		return gefunden
	else:
		raise RuntimeError("Keine Lösung gefunden")


# ~ print(solver2("185+15=270"))


########################################################################
### Aufgabe 2 ###
########################################################################
import random
def erzeuger():
	"""Erzeugt eine Streichholzgleichung und die korrekte Loesung"""
	while True:
		term1 = str(random.randint(10, 99))
		sign1 = random.choice(["+", "-"])
		term2 = str(random.randint(10, 99))
		outcome = str(random.randint(1, 198))
		equation = term1 + sign1 + term2 + "=" + outcome
		if "0" in equation or "00" in equation or "000" in equation:
			continue
		try:
			loesung = solver(equation)
			if loesung == equation:
				continue
		except RuntimeError:
			continue
		return(equation, loesung)
		
print(erzeuger())
	
	
