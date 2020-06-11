


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python

import random
from functools import partial

def erzeuge_hash(string):
	"""Erzeugt einen Hash fuer einen String"""
	data = [ord(element) for element in string]
	sum1, sum2 = 0, 0
	for element in data:
		sum1 = (sum1 + element * 11111) % (10 ** 6)
		sum2 = (sum2 + sum1) % (10 ** 6)
	return str(sum1) + str(sum2)

	
a = ["Hallo", "Hello", "12345678", "12334567", "einsehrlangerstringwirddurchhasherkuerzergemacht"]
for element in a:
	print(erzeuge_hash(element))
	
	
def umdreher(eingabe):
	return eingabe[::-1]

def vertauscher(eingabe):
	assert len(eingabe) % 2 == 0
	ausgabe = ""
	for i in range(0, len(eingabe) - 1, 2):
		ausgabe += eingabe[i + 1]
		ausgabe += eingabe[i]
	return ausgabe


def zipper(eingabe, reverse=False):
	assert len(eingabe) % 2 == 0
	ausgabe = ""
	if not reverse:
		for i in range(0, len(eingabe) // 2):
			ausgabe += eingabe[i]
			ausgabe += eingabe[-i - 1]
	else:
		a = [eingabe[i] for i in range(0, len(eingabe), 2)]
		b = [eingabe[i] for i in range(1, len(eingabe), 2)][::-1]
		for i in range(len(eingabe) // 2):
			ausgabe += a[i]
		for i in range(len(eingabe) // 2):
			ausgabe += b[i]
	return ausgabe
		
		
def encrypt(nachricht, passwort):
	"""Verschluesselt eine Nachricht"""
	nachricht = nachricht.upper()
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
	if len(nachricht) % 2 == 0:
		nachricht += "".join(random.choices(alphabet, k=20)) + "ZZ"
	else:
		nachricht += "".join(random.choices(alphabet, k=20)) + "AAA"
	
	hashwert = erzeuge_hash(passwort)
	funclist = [vertauscher, zipper, umdreher]
	
	for element in hashwert:
		rest = int(element) % 3
		nachricht = funclist[rest](nachricht)	
	return nachricht
	
	
def decrypt(code, passwort):
	"""Entschluesselt einen Code"""
	hashwert = erzeuge_hash(passwort)[::-1]
	funclist = [vertauscher, partial(zipper, reverse=True), umdreher]
	for element in hashwert:
		rest = int(element) % 3
		code = funclist[rest](code)
	if code.endswith("ZZ"):
		return code[:-22]
	else:
		return  code[:-23]
		
		
botschaft = "TREFFPUNKTUNTERDERBRUECKEUMSIEBENUHR"
passwort = "unsergeheimnis"

code = encrypt(botschaft, passwort)
print(code)

decode = decrypt(code, passwort)
print(decode)

assert botschaft == decode
