


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python




def countdown1(n, counter=0, sequenz=""):
	if n == 1:
		return (counter, sequenz)
	counter += 1
	results = []
	if n % 2 == 0:
		results.append(countdown1(n // 2, counter, sequenz + "2"))
	if n % 3 == 0:
		results.append(countdown1(n // 3, counter, sequenz + "3"))
	results.append(countdown1(n - 1, counter, sequenz + "1"))
	return min(results)


print(countdown1(43))




def countdown2(n):
	buch = {1: (0, "")}
	def inner(n):
		if n in buch:
			return buch[n]
		results = []
		if n % 2 == 0:
			counter, sequence = inner(n // 2)
			results.append((counter + 1, "2" + sequence))
		if n % 3 == 0:
			counter, sequence = inner(n // 3)
			results.append((counter + 1, "3" + sequence))
		counter, sequence = inner(n - 1)
		results.append((counter + 1, "1" + sequence))
		buch[n] = min(results)
		return buch[n]
	return inner(n)
	
	
print(countdown2(43))



########################################################################
### Aufgabe 1 ###
########################################################################
"""Lösung der Aufgabe ohne Rekursion. Die Idee ist es, schlichtweg
alle Zahlen zu berechnen und die Ergebnisse in einem Dict zu speichern."""

def countdown_norec(n):
	buch = {1: (0, "")}
	for zahl in range(2, n + 1):
		a = b = (9**9, "")
		if zahl % 2 == 0:
			res = buch[zahl // 2]
			a = (res[0] + 1, "2" + res[1])
		if zahl % 3 == 0:
			res = buch[zahl // 3]
			b = (res[0] + 1, "3" + res[1])
		res = buch[zahl - 1]
		c = (res[0] + 1, "1" + res[1])
		buch[zahl] = min(a, b, c)
	return buch[n]

print(countdown_norec(43))
			
	
