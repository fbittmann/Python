


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python


def collatz1(n):
	while n > 1:
		if n % 2 == 0:
			n = n // 2
		else:
			n = (n * 3) + 1
	return True
	

print(collatz1(100))	
	
	
def collatz2(n):
	besucht = set()
	while True:
		if n == 1:
			return True
		elif n in besucht:
			return False
		else:
			besucht.add(n)
			if n % 2 == 0:
				n = n // 2
			else:
				n = (n * 3) + 1
				
print(collatz2(100))		
		
		
				
########################################################################
### Aufgabe 1 ###
########################################################################

def collatz_counter(n):
	counter = 0
	while n > 1:
		if n % 2 == 0:
			n = n // 2
		else:
			n = (n * 3) + 1
		counter += 1
	return counter

print(collatz_counter(8))	
print(collatz_counter(100))


res = [(i, collatz_counter(i)) for i in range(2, 5001)]
res.sort(key = lambda x: x[1], reverse = True)
"""Das ist nun also die laengste Collatz-Sequenz unter den ersten 5000
natuerlichen Zahlen"""
print(res[0])


########################################################################
### Aufgabe 2 ###
########################################################################

def collatz3(n):
	"""Wir können abbrechen, sobald n unter die genannte, sehr hohe Zahl geht"""
	while n > 87 * (2**60):
		if n % 2 == 0:
			n = n // 2
		else:
			n = (n * 3) + 1
	return True
	
print(collatz3((10**5500) - 87845834658388888888593694356934569435693441))
