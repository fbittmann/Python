


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python



roemische_zahlen = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
	(100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
	(9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def nach_roemisch(zahl):
	if not isinstance(zahl, int) or not 0 < zahl < 4000:
		raise ValueError()
	ausgabe = ""
	for wert, symbol in roemische_zahlen:
		while zahl >= wert:
			ausgabe += symbol
			zahl -= wert
	return ausgabe


def von_roemisch(eingabe):
	if not isinstance(eingabe, str):
		raise ValueError()
	ausgabe = 0
	for wert, symbol in roemische_zahlen:
		while eingabe.startswith(symbol):
			ausgabe += wert
			eingabe = eingabe[len(symbol):]
	return ausgabe

	
for i in range(1, 4000):
	assert i == von_roemisch(nach_roemisch(i)) 
	
print(nach_roemisch(2020))
print(nach_roemisch(1994))
