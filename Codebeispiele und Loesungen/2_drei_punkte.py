


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python




import math


def norm(vektor):
	"""Betrag eines Vektors"""
	return sum(x**2 for x in vektor)**0.5


def kreuzprodukt(a, b):
	"""Kreuzprodukt der Vektoren a und b"""
	assert len(a) == len(b) == 3
	return [a[1] * b[2] - a[2] * b[1],
	a[2] * b[0] - a[0] * b[2],
	a[0] * b[1] - a[1] * b[0]]


def geradenabstand(gerade, punkt):
    """Abstand zwischen Gerade und Punkt
    Die Gerade wird als Tuple aus Stützpunkt und Richtung gegeben.
    Stützpunkt, Richtung und Punkt sind jeweils Listen der Länge drei.
    """
    stuetzpunkt, richtung = gerade
    abstand = [s - p for s, p in zip(stuetzpunkt, punkt)]
    return norm(kreuzprodukt(abstand, richtung)) / norm(richtung)


def punktabstand(x, y):
	"""Abstand zwischen zwei Punkten"""
	assert len(x) == len(y) == 2
	return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5


def normiere_vektor(vektor):
    laenge = norm(vektor)
    return [x / laenge for x in vektor]


def liegt_auf_linie(punkt_a, punkt_b, punkt_c, toleranz):
    """ Testet, ob die Punkte A, B und C auf einer Geraden liegen"""
    richtung_ab = normiere_vektor([a - b for a, b in zip(punkt_a, punkt_b)])
    richtung_bc = normiere_vektor([b - c for b, c in zip(punkt_b, punkt_c)])
    skalarprodukt = sum(x * y for x, y in zip(richtung_ab, richtung_bc))
    # Punkte liegen auf einer Linie, wenn das Skalarprodukt 1 oder -1 ist.
    return 1 - abs(skalarprodukt) < toleranz





def berechne_abstand(vektor, a, b, c):
    zentralgerade = ((0, 0, 0), (1, 1, 1)) # Stützpunkt und Richtung
    distanzen = [punktabstand(vektor, p) for p in (a, b, c)]
    abstand = geradenabstand(zentralgerade, distanzen)
    return abstand, distanzen, vektor

def verschiebe_vektor(vektor, koordinate, verschiebung):
    if koordinate == 0:
        return [vektor[0] + verschiebung, vektor[1]]
    else:
        return [vektor[0], vektor[1] + verschiebung]

def kreisfinder(a, b, c, toleranz=0.01, maxiter=10**5):
    if a == b or b == c or c==a:
        raise ValueError("Drei verschiedene Punkte eingeben!")
    if liegt_auf_linie(a, b, c, toleranz=0.1):
        raise ValueError("Alle drei Punkte liegen auf einer Geraden!")
    mittelpunkt = [(a[0] + b[0] + c[0]) / 3, (a[1] + b[1] + c[1]) / 3]
    step = 1
    abstand, distanzen, _ = berechne_abstand(mittelpunkt, a, b, c)
    for iteration in range(maxiter):
        kandidaten = []
        for vorzeichen in (-1, 1):
            for koordinate in (0, 1):
                kandidaten.append(berechne_abstand(verschiebe_vektor(mittelpunkt, koordinate, vorzeichen * step), a, b, c))
        neuer_abstand, neue_distanzen, neuer_mittelpunkt = min(kandidaten)
        if neuer_abstand < abstand:
            abstand, distanzen, mittelpunkt = neuer_abstand, neue_distanzen, neuer_mittelpunkt
        else:
            step *= 0.5
        if abstand < 0.01 * toleranz:
            break
    else:
        raise ArithmeticError("Konvergiert nicht")
    dist_a, dist_b, dist_c = distanzen
    if not (math.isclose(dist_a, dist_b, abs_tol=toleranz)
        and math.isclose(dist_a, dist_c, abs_tol=toleranz)):
        raise ArithmeticError("Gefundener Punkt ist nicht Kreismittelpunkt")
    return (round(mittelpunkt[0], 3), round(mittelpunkt[1], 3)), round(dist_a, 3)


print(kreisfinder((2,2), (-5,1), (-1,-6)))

# ~ a = (1,1)
# ~ c = (2,2)
# ~ b = (3,3)
# ~ print(kreisfinder(a, b, c, 3))


########################################################################
### Decorator ###
########################################################################


def date_adder(func, date):
	assert type(date) == str
	def inner(*args, **kwargs):
		print("Aktuelles Datum:", date)
		return func(*args, **kwargs)
	return inner



kreisfinder = date_adder(kreisfinder, "2020_03_04")
print(kreisfinder((2, 2), (-5, 1), (-1, -6), 3, 10**5))
