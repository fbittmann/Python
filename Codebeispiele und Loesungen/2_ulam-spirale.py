


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python

def cart_to_matrix(position, size):
	"""Konvertiert eine Position aus dem cartesischen Koordinatensystem
	in die Darstellung Listenmatrix"""
	spalte = (size // 2) + position[0]
	zeile = (size // 2) - position[1]
	return (zeile, spalte)
	

def next_position(daten, position):
    leerefelder = []
    # Positionen unten, rechts, oben und links
    # Reihenfolge ist wichtig, damit die Ecken richtig
    # behandelt werden.
    for x, y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        px, py = position[0] + x, position[1] + y
        pos = cart_to_matrix((px, py), len(daten))
        if daten[pos[0]][pos[1]] == "":
            leerefelder.append((px, py, px ** 2 + py ** 2))
    return min(leerefelder, key=lambda f: f[2])[:2]


def ulam(n):
	size = max(15, (int(n ** 0.5) // 2) * 2 + 11)
	daten = [[""] * size for i in range(size)]
	i = cart_to_matrix((0, 0), size)
	daten[i[0]][i[1]] = 1
	i = cart_to_matrix((0, 1), size)
	daten[i[0]][i[1]] = 2
	position = (1, 1)
	for zaehler in range(3, n + 1):
		a = cart_to_matrix(position, size)
		daten[a[0]][a[1]] = zaehler
		position = next_position(daten, position)
	print_field(daten)

	
def print_field(daten):
	size = len(daten)
	print("".join(["*" for i in range(size * 4)]))
	for zeile in daten:
		for element in zeile:
			if element == "":
				print(" " * 4, end = "")	#Genau 4 Leerzeichen
			else:
				print( f"{element:02d} ", end = "")	#Leerzeichen vor und nach dem f-string
		print("")
	print("".join(["*" for i in range(size * 4)]))
	
	
ulam(88)
