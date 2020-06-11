


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python



def palindrom(string):
	assert len(string) > 1
	return string == string[::-1]
	
print(palindrom("ABBA"))
	

def lps(string):
	result_start_pos = None
	result_length = 1
	laenge = len(string)
	for startpos in range(laenge):
		for endpos in range(laenge, startpos + result_length, -1):
			substring = string[startpos:endpos]
			print(substring)
			if palindrom(substring):
				result_start_pos = startpos
				result_length = len(substring)
				break
	return result_start_pos, result_length



print(lps("TOTABBA"))


########################################################################
### Aufgabe 1 ###
########################################################################
import random
def zufallsgene(laenge, n):
	alphabet = ("A", "T", "C", "G")
	alle_gene = []
	for i in range(n):
		gen = "".join(random.choice(alphabet) for x in range(laenge))
		alle_gene.append(gen)
	return alle_gene
	
print(zufallsgene(20, 5))


########################################################################
### Aufgabe 2 ###
########################################################################

def ist_aufsteigend(eingabe):
	"""Testet, ob eine Eingabe streng monotonisch ansteigt"""
	for i in range(len(eingabe) - 1):
		if eingabe[i + 1] <= eingabe[i]:
			return False
	return True
		

def lis(eingabe):
	"""Findet den longest increasing substring"""
	best = []
	for pos in range(len(eingabe)):
		for laenge in range(len(eingabe) - pos):
			teil = eingabe[pos: pos + laenge + 1]
			if not ist_aufsteigend(teil):
				break
			if ist_aufsteigend(teil) and len(teil) >= len(best):
				best = teil
	return best
			
testsequenz = [1,1,1,1,2,3,4,5,3,3,3,1,2,3,4,5,6,7,8]
print(lis(testsequenz))
		
	
