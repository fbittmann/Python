


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python

import copy
import random
from itertools import product
import statistics as stats
from collections import defaultdict


def strategiesucher(gewinnsumme=100):
	def wincheck(i, j, k):
		if (i, j, k) in wahrscheinlichkeit:
			# Wahrscheinlichkeit schon bekannt
			return wahrscheinlichkeit[i, j, k]

		if i + k >= gewinnsumme:
			# garantiert gewonnen
			return 1
		elif j >= gewinnsumme:
			# garantiert verloren
			return 0

		# Gewinnwahrscheinlichkeit bei Würfeln
		p_wurf = 1 - wincheck(j , i + 1, 0)
		for punkte in range(2, 7):
			p_wurf += wincheck(i, j, k + punkte)
		p_wurf /= 6
		# Bei Stop, Wahrscheinlichkeit dass j beginnt
		p_stop = 1 - wincheck(j, i + max(k, 1), 0)
		# welches ist die bessere Strategie
		p_best = max(p_wurf, p_stop)
		if p_wurf > p_stop:
			handlung[i, j, k] = "wurf"
		else:
			handlung[i, j, k] = "stop"
		wahrscheinlichkeit [i, j, k] = p_best
		return p_best
	wahrscheinlichkeit = {}
	handlung = {}
	wincheck(0, 0, 0)
	return (wahrscheinlichkeit, handlung)
	

def zufall(meinstand, deinstand):
	rundensumme = 0
	while True:
		if random.randint(0, 1) == 1:
			z = random.randint(1, 6)
			if z == 1:
				return 1
			else:
				rundensumme += z
		else:
			return max(1, rundensumme)
				
				
def gierig(meinstand, deinstand):
	rundensumme = 0
	while rundensumme + meinstand < 100:
		z = random.randint(1, 6)
		if z == 1:
			return 1
		else:
			rundensumme += z
	return rundensumme


def get20(meinstand, deinstand):
	rundensumme = 0
	while rundensumme < 20 and meinstand + rundensumme < 100:
		z = random.randint(1, 6)
		if z == 1:
			return 1
		else:
			rundensumme += z
	return rundensumme


def risky(meinstand, deinstand):
	rundensumme = 0
	if 80 <= deinstand < 100:	#Spieler muss riskieren
		while meinstand + rundensumme < 100:
			z = random.randint(1, 6)
			if z == 1:
				return 1
			else:
				rundensumme += z
		return rundensumme
	else:					#Spieler kann konservativ spielen
		while rundensumme < 20 and meinstand + rundensumme < 100:
			z = random.randint(1, 6)
			if z == 1:
				return 1
			else:
				rundensumme += z
		return rundensumme		


def optimal(meinstand, deinstand):
	rundensumme = 0
	while True:
		if meinstand + rundensumme >= 100:
			return rundensumme
		res = (meinstand, deinstand, rundensumme)
		if datenbank[1][res] == "stop":
			return rundensumme
		z = random.randint(1, 6)
		if z == 1:
			return 1
		else:
			rundensumme += z


from itertools import product
def turnier(strategien, runden):
	global datenbank
	datenbank = strategiesucher()
	gewinnbuch = {}
	for selbst in strategien:
		gewinnbuch[selbst] = {}
		for gegner in strategien:
			if selbst != gegner:
				gewinnbuch[selbst][gegner] = 0
	for strat0, strat1 in product(strategien, strategien):
		if strat0 != strat1:
			for runde in range(runden):
				p0, p1 = 0, 0
				while True:
					p0 += strat0(p0, p1)
					if p0 >= 100:
						gewinnbuch[strat0][strat1] += 1
						break
					p1 += strat1(p1, p0)
					if p1 >= 100:
						gewinnbuch[strat1][strat0] += 1
						break
	for selbst in gewinnbuch:
		print(selbst.__name__)
		for gegner in gewinnbuch[selbst]:
			winchance = 100 * gewinnbuch[selbst][gegner] / (runden * 2)
			print(gegner.__name__, round(winchance, 1))
		print("_" * 15)
					

random.seed(1234)		
turnier((zufall, gierig, get20, risky, optimal), 5000)		
	
