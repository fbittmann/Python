

import time
import copy



def npos(position, pfad, size):
	"""Zeigt für eine Position an, wie viele Zugmoeglichkeiten von dieser
	aus bestehen"""
	npos = 0
	for a in (-2, -1, 1, 2):
		for b in (-2, -1, 1, 2):
			if abs(a) == abs(b):
				continue
			if (0 <= position[0] + a <= (size - 1) and 0 <= position[1] + b <= (size - 1) and
				(position[0] + a, position[1] + b) not in pfad):
					npos += 1
	return npos
	

			
def feldfinder(position, pfad, sackgassen, size):
	""" Findet alle Felder auf die ein Springer von Position aus springen kann.
	Felder, die schon auf dem Pfad liegen oder in einer Sackgasse enden werden
	ignoriert.
	"""
	posfelder = []
	for a, b in [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
			(1, -2), (1, 2), (2, -1), (2, 1)]:
		a += position[0]
		b += position[1]
		if 0 <= a <= size - 1 and 0 <= b <= size - 1:
			# Position liegt noch innerhalb des Feldes
			if (a, b) not in pfad and (pfad + [(a, b)]) not in sackgassen:
				posfelder.append((a, b))
	return posfelder
	

def springer_problem(size=5):
	startpos = (0, 0)
	pfad = [startpos]
	sackgassen = []
	iteration = 1
	while len(pfad) < size ** 2:
		iteration += 1
		# Alle weiteren moeglichen Zuege generieren:
		moves = feldfinder(pfad[-1], pfad, sackgassen, size)
		if moves:
			pfad.append(moves[0])
		elif pfad == [startpos]:
			raise ValueError("Spielfeld nicht lösbar")
		else:
			#Backtrack wenn Sackgasse:
			sackgassen.append(pfad)
			pfad = pfad[:-1]
	print("Iterationen:", iteration)
	print(pfad)
	print([b * size + a for a, b in pfad])

	
springer_problem()

########################################################################
### Aufgabe 1 ###
########################################################################
	
def npos(position, pfad, size):
	"""Zeigt für eine Position an, wie viele Zugmoeglichkeiten von dieser
	aus bestehen"""
	npos = 0
	for a in (-2, -1, 1, 2):
		for b in (-2, -1, 1, 2):
			if abs(a) == abs(b):
				continue
			if (0 <= position[0] + a <= (size - 1) and 0 <= position[1] + b <= (size - 1) and
				(position[0] + a, position[1] + b) not in pfad):
					npos += 1
	return npos


def springer_problem2(size):
	startpos = (0, 0)
	pfad = [startpos]
	sackgassen = []
	iteration = 1
	while len(pfad) < size ** 2:
		iteration += 1
		# Alle weiteren moeglichen Zuege generieren:
		moves = feldfinder(pfad[-1], pfad, sackgassen, size)
		if moves:
			moves2 = [(zug, npos(zug, pfad, size)) for zug in moves]
			moves2.sort(key=lambda x: x[1])
			pfad.append(moves2[0][0])
		elif pfad == [startpos]:
			raise ValueError("Spielfeld nicht lösbar")
		else:
			#Backtrack wenn Sackgasse:
			sackgassen.append(pfad)
			pfad = pfad[:-1]
	print("Iterationen:", iteration)
	print(pfad)
	print([b * size + a for a, b in pfad])

print(springer_problem2(6))

########################################################################
### Aufgabe 2 ###
########################################################################
#Ausgelagert nach 2_Sudoku.py
