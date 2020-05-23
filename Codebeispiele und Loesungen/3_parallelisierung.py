


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python


import multiprocessing as mp

def primgen(n, queue):
	if n % 2 == 0:
		n += 1
	while True:
		for i in range(3, int(n**0.5 + 1), 2):
			if n % i == 0:
				break
		else:
			queue.put(n)
		n += 2
		

from multiprocessing import Process, Queue
def multiprimgen(cores, nfinal):
    schlange = Queue()
    prozesse = []
    for nummer in range(1, cores + 1):
        startwert = 10**14 // nummer
        prozess = Process(target=primgen, args=(startwert, schlange))
        prozess.start()
        prozesse.append(prozess)
    primzahlen = []
    while len(primzahlen) < nfinal:
        primzahlen.append(schlange.get())
    for prozess in prozesse:
        prozess.terminate()
    return primzahlen
	
	
def prime_product(inqueue, outqueue):
    while True:
        prime_a = inqueue.get()
        prime_b = inqueue.get()
        outqueue.put(prime_a * prime_b)



"""Wir lassen 2 Prozesse laufen und wollen insgesamt 20 Primzahlen generieren"""
print(multiprimgen(2, 10))




def serial(cores, nfinal):
	prozesse = []
	schlange1 = Queue()
	schlange2 = Queue()
	for nummer in range(1, cores + 1):
		startwert = (10**14) // (nummer)
		prozess = Process(target=primgen, args=(startwert, schlange1))
		prozess.start()
		prozesse.append(prozess)
	prozess = Process(target=prime_product, args=(schlange1, schlange2))
	prozess.start()
	prozesse.append(prozess)
	
	output = []
	while len(output) < nfinal:
		output.append(schlange2.get())
	for prozess in prozesse:
		prozess.terminate()
	return output


"""Wir lassen 2 Prozesse laufen und wollen insgesamt 20 Primzahlen generieren"""
print(serial(2, 10))
