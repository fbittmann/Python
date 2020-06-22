



#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python

import copy


def subcheck(daten, zeilensek, spaltensek):
	"""Hier pruefen wir fuer jeden 3x3 Block innerhalb des Sudokus,
	ob jede Zahl genau 1 Mal vorkommt"""
	untersek = []
	for zeile in range(3 * zeilensek, 3 * zeilensek + 3):
		for spalte in range(3 * spaltensek, 3 * spaltensek + 3):
			untersek.append(daten[zeile][spalte])
	for i in range(1, 10):
		if i not in untersek:
			return False
	return True
	

def subpos(daten, zeile, spalte):
	"""Gibt für jeden 3x3 Sublock die noch möglichen Zahlen aus"""
	#Zuordnung der Eingabe nach Block
	lookup = ([0,1,2], [3,4,5], [6,7,8])
	for x in range(3):
		if zeile in lookup[x]:
			zeilensek = x
	for y in range(3):
		if spalte in lookup[y]:
			spaltensek = y
	untersek = []
	for zeile in range(3 * zeilensek, 3 * zeilensek + 3):
		for spalte in range(3 * spaltensek, 3 * spaltensek + 3):
			untersek.append(daten[zeile][spalte])
	possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for i in range(1, 10):
		if i in untersek:
			possible.remove(i)
	return possible


def printer(daten):
	"""Stellt das Sudoku grafisch in der Konsole dar"""
	print("Spielfeld")
	for element in daten:
		print(element)


def spaltengen(daten, spalte):
	"""Extrahiert eine Spalte aus der Datenmatrix"""
	neuspalte = []
	for zeile in daten:
		neuspalte.append(zeile[spalte])
	return neuspalte
	

def alle_felder_voll(daten):
	"""Prüft, ob jedes Feld eine gültige Zahl hat"""
	for zeile in daten:
		if 0 in zeile:
			return False
	return True
	
	
def gewonnen(daten):
	"""Prüft, ob das vollständige Soduku korrekt gelöst wurde"""
	#Zeilentest
	for zeile in daten:
		for x in range(1, 10):
			if x in zeile:
				continue
			else:
				return False
	#Spaltentest
	for y in range(0, 9):
		for i in range(1, 10):
			if i in spaltengen(daten, y):
				continue
			else:
				return False
	
	#Sektionetest
	for x in range(3):
		for y in range(3):
			if subcheck(daten, x, y) == False:
				return False
	return True


def posfinder(daten, zeile, spalte, deadends):
	"""Zeigt an, welche möglichen Zahlen an die Position noch gesetzt werden können"""
	zeilenpos = []
	for i in range(1,10):
		if i not in daten[zeile]:
			zeilenpos.append(i)
	spaltenpos = []
	tempspalte = spaltengen(daten, spalte)
	for i in range(1,10):
		if i not in tempspalte:
			spaltenpos.append(i)
	pos = []
	for i in range(1,10):
		if i in zeilenpos and i in spaltenpos:
			pos.append(i)
	
	pos2 = []	
	subpossibles = subpos(daten, zeile, spalte)
	if subpossibles == [] or pos == []:
		return []
	else:
		for x in range(1,10):
			if x in pos and x in subpossibles:
				pos2.append(x)
	
	finalpos = []
	for element in pos2:
		tempdaten = copy.deepcopy(daten)
		tempdaten[zeile][spalte] = element
		if tempdaten not in deadends:
			finalpos.append(element)
	return finalpos


def findempty(daten):
	"""Findet das nächste leere Feld in der Matrix"""
	for zeile in range(0,9):
		for spalte in range(0,9):
			if daten[zeile][spalte] == 0:
				return (zeile, spalte)
				
				
def sudoku_loeser(daten):
	"""Loest ein unvollstaendiges Sudoku mittels Backtracking"""
	path = [daten]
	deadends = []
	while True:
		currentfield = copy.deepcopy(path[-1])
		#Test auf Lösung
		if alle_felder_voll(currentfield) == True and gewonnen(currentfield) == True:
			break
		
		nextfield = findempty(currentfield)
		posnumbers = posfinder(currentfield, nextfield[0], nextfield[1], deadends)
		#~ print(nextfield, posnumbers)
		
		if len(path) == 1 and posnumbers == []:
			raise ValueError("Sudoku ist nicht lösbar!")
		
		#Backtrack wenn fail
		if posnumbers == []:
			assert currentfield not in deadends
			deadends.append(currentfield)
			path = path[:-1]
			continue
		else:
			currentfield[nextfield[0]][nextfield[1]] = posnumbers[0]
			path.append(currentfield)
			continue
	print("Gewonnen!")
	printer(path[-1])
	
	
if __name__ == '__main__':
	beispiel = [[0,0,5,0,0,8,0,9,4],
				[8,0,0,0,0,0,2,0,5],
				[0,0,0,9,5,3,0,0,0],
				[0,5,0,0,0,7,6,0,9],
				[0,0,0,2,3,6,0,0,0],
				[2,0,6,5,0,0,0,4,0],
				[0,0,0,8,7,1,0,0,0],
				[5,0,1,0,0,0,0,0,8],
				[6,8,0,4,0,0,1,0,0]]
	sudoku_loeser(beispiel)
	
				
