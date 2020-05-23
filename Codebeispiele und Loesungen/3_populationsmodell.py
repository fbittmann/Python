


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python



import time
import random
from itertools import combinations

SIZE = 10

class Schaf:
	def __init__(self):
		self.position = [random.random() * SIZE, random.random() * SIZE]
		self.hunger = 0
		self.traechtig = 0
		self.alter=0

	def bewegen(self):
		while True :
			x = self.position[0] + random.random() * 4 - 2
			y = self.position[1] + random.random() * 4 - 2
			if 0 <= x < SIZE and 0 <= y < SIZE:
				break
		self.position = (x, y)

	def abstand(self, other):
		return (
			(self.position[0] - other.position[0]) ** 2
			+ (self.position[1] - other.position[1]) ** 2
		) ** 0.5

	def fressen(self, gras):
		xpos, ypos = map(int, self.position)
		if gras[xpos, ypos] == 2:
			self.hunger = 0
			gras[xpos, ypos] = 0

	def lebendig(self):
		return self.alter < 20 and self.hunger < 3

	def willig(self):
		return self.traechtig == 0 and self.hunger == 0


def statistik(schafe, runde):
	hunger = traechtig = gras = alter = 0
	for schaf in schafe:
		hunger += schaf.hunger
		alter += schaf.alter
		if schaf.traechtig:
			traechtig += 1
	print(f"Runde : {runde}")
	print(f"Schafe auf der Weide: {len(schafe)}")
	print(f"Durchschnittlicher Hunger: {hunger / len(schafe):.2f}")
	print(f"Durchschnittliches Alter: {alter / len(schafe):.2f}")
	print(f"Traechtig: {traechtig}")
	print("#" * 40)


def simulation(runden):
	gras = {(x, y): 2 for x in range(SIZE) for y in range(SIZE)}
	schafe = [Schaf() for _ in range(10)]
	for runde in range(runden):
		# Gras waechst
		for pos in gras:
			if gras[pos] < 2:
				gras[pos] += 1
		random.shuffle(schafe)
		
		# Bewegungsphase und fressen
		laemmer = 0
		for schaf in schafe:
			schaf.alter += 1
			schaf.hunger += 1
			schaf.bewegen()
			schaf.fressen(gras)
			if schaf.traechtig == 8:
				schaf.traechtig = 0
				laemmer += 1
			elif schaf.traechtig > 0:
				schaf.traechtig += 1
		schafe.extend(Schaf() for _ in range(laemmer))
		statistik(schafe, runde)
		
		# Paaren
		willige_schafe = [schaf for schaf in schafe	if schaf.willig()]
		muede_schafe = set()
		for schaf, partner in combinations(willige_schafe, 2):
			if schaf in muede_schafe or partner in muede_schafe:
				pass
			elif schaf.abstand(partner) <= 1:
				schaf.traechtig = 1
				muede_schafe.update([schaf, partner])
		
		# Sterbephase
		schafe = [schaf for schaf in schafe	if schaf.lebendig()]
		if not schafe:
			break
		time.sleep(0.7)


simulation(40)


########################################################################
### Aufgabe 1 ###
########################################################################
class Person:
	def __init__(self):
		self.position = (random.random() * SIZE, random.random() * SIZE)
		self.status = 0			#Gesund (0), infiziert (1), immun (2)
		self.infektstatus = 0	#Aktuelles Stadium der Infektion
		
		
				
	def bewegen(self):
		"""Person kann sich einen Meter bewegen"""
		while True :
			x = self.position[0] + random.random() * 2 - 1
			y = self.position[1] + random.random() * 2 - 1
			if 0 <= x < SIZE and 0 <= y < SIZE:
				break
		self.position = (x, y)
				
	def abstand(self, other):
		"""Berechnet Abstand zu einer anderen Person"""
		return (
			(self.position[0] - other.position[0]) ** 2
			+ (self.position[1] - other.position[1]) ** 2
		) ** 0.5


def statistik(personen):
	n = len(personen)
	gesund, infiziert, immun = 0, 0, 0
	for p in personen:
		if p.status == 0:
			gesund +=1
		elif p.status == 1:
			infiziert += 1
		elif p.status == 2:
			immun += 1
	print(f"Lebendig: {n} | Gesund: {gesund} | Infiziert: {infiziert} | Immun: {immun}")
		
		
def simulation(runden, npersonen, infiziert):
	STERBECHANCE = 0.01			#Chance, dass eine infizierte Person an einem Tag stirbt
	INFEKTCHANCE = 0.40			#Chance, dass eine infizierte Person bei Kontakt eine andere infiziert
	personen = [Person() for i in range(npersonen)]
	random.shuffle(personen)
	for i, p in enumerate(personen):
		if i < infiziert:
			p.status = 1
	
	for r in range(runden):
		#Bewegungsphase
		for p in personen:
			p.bewegen()
		
		#Infektionsphase:
		for p1, p2 in itertools.combinations(personen, 2):
			if p1.abstand(p2) < 2 and (p1.status == 1 or p2.status == 1) and random.random() < INFEKTCHANCE:
				# ~ print("INFEKTION!")
				if p1.status == 0:
					p1.status = 1
				if p2.status == 0:
					p2.status = 1
					
		#Alterungsphase
		for p in personen:
			if p.status == 1:
				p.infektstatus += 1
			if p.infektstatus >= 10:
				p.status = 2
				
		#Sterbephase
		survivors = []
		for p in personen:
			if p.status == 1 and random.random() < STERBECHANCE:
				#Person stirbt an der Krankheit
				continue
			else:
				survivors.append(p)
		personen = survivors
		print(f"Runde: {r + 1}")
		statistik(personen)
		if len(personen) == 0:
			break
		time.sleep(0.6)

# ~ SIZE = 15			
# ~ simulation(30, 20, 2)
