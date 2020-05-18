


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python


from itertools import islice

def folgenentwicklung(x, r, n, prec):
	for i in range(n):
		print(round(x, prec))
		x = x * r * (1 - x)
		
		
def logistic(x, r):
	while True:
		yield x
		x = x * r * (1 - x)
	
	
def periodenfinder(x, r):
	iteration = 0
	seen = {x:iteration}
	gen = logistic(x, r)
	[next(gen) for i in range(10**6)]
	while True:
		iteration += 1
		x = next(gen)
		for element in seen:
			tdiff = abs(element - x)
			if tdiff < (1 / 10**6):
				return iteration - seen[element]
		seen[x] = iteration
		

def periodenfinder(x, r):
	numbers = logistic(x, r)
	# erste Million iterationen überspringen
	numbers = islice(numbers, 10**6, None)
	seen = {}
	for iteration, x in enumerate(numbers):
		for element in seen:
			if abs(element - x) < 1e-6:
				return iteration - seen[element]
		seen[x] = iteration
		
print(periodenfinder(0.5, 2))


def sprungfinder(x, r1, precision=4):
	p1 = periodenfinder(x, r1)
	schrittweite = 0.1
	while schrittweite > 0.1 ** precision:
		r2 = r1 + schrittweite
		print(r1, r2)
		p2 = periodenfinder(x, r2)
		if p1 == p2:
			r1 = r2
		else:
			schrittweite /= 2
	return round((r1 + r2) / 2, precision)

		
print(sprungfinder(0.5, 2.7))
print(sprungfinder(0.5, 3.1))
