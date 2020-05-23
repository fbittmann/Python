

import random
from itertools import combinations

def berechne_abstand(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def entferne_kreise(kreise):
    """ Entfernt solche Kreise, die vollstaendig in einem groesseren Kreis liegen"""
    zu_entfernen = set()
    for paar in combinations(kreise, 2):
        kleiner_kreis, grosser_kreis = sorted(paar, key=lambda k: k[2])
        abstand_mittelpunkte = berechne_abstand(kleiner_kreis, grosser_kreis)
        if grosser_kreis[2] >= abstand_mittelpunkte + kleiner_kreis[2]:
            # kleiner_kreis liegt innerhalb grosser_kreis
            zu_entfernen.add(kleiner_kreis)
    return [k for k in kreise if k not in zu_entfernen]

def ermittle_umschreibendes_rechteck(kreise):
    xmin = min(k[0] - k[2] for k in kreise)
    xmax = max(k[0] + k[2] for k in kreise)
    ymin = min(k[1] - k[2] for k in kreise)
    ymax = max(k[1] + k[2] for k in kreise)
    return xmin, xmax, ymin, ymax

def iter_teilbereiche(xmin, xmax, ymin, ymax, n):
    xsize = (xmax - xmin) / n
    ysize = (ymax - ymin) / n
    for xstep in range(n):
        for ystep in range(n):
            xmin_teil = xmin + xstep * xsize
            ymin_teil = ymin + ystep * ysize
            yield xmin_teil, xmin_teil + xsize, ymin_teil, ymin_teil + ysize

def ist_box_innerhalb(box, kreise):
    xmin, xmax, ymin, ymax = box
    for kreis in kreise:
        if (berechne_abstand([xmin, ymin], kreis) < kreis[2] and
            berechne_abstand([xmin, ymax], kreis) < kreis[2] and
            berechne_abstand([xmax, ymin], kreis) < kreis[2] and
            berechne_abstand([xmax, ymax], kreis) < kreis[2]):
            return True
    return False

def ermittle_trefferquote(box, kreise, iterationen):
    xmin, xmax, ymin, ymax = box
    treffer = 0
    for i in range(iterationen):
        zx = xmin + (xmax - xmin) * random.random()
        zy = ymin + (ymax - ymin) * random.random()
        for kreis in kreise:
            if berechne_abstand((zx, zy), kreis) < kreis[2]:
                treffer += 1
                break
    return treffer / iterationen

def berechne_flaeche(kreise, n, iterationen):
    total_simulationen = 0
    total_boxes = 0
    skipped_boxes = 0
    total_points = 0
    kreise = entferne_kreise(kreise)
    xmin, xmax, ymin, ymax = ermittle_umschreibendes_rechteck(kreise)
    boxflaeche = ((xmax - xmin) * (ymax - ymin)) / (n ** 2)
    for box_teil in iter_teilbereiche(xmin, xmax, ymin, ymax, n):
        if ist_box_innerhalb(box_teil, kreise):
            skipped_boxes += 1
            total_boxes += boxflaeche
        else:
            total_points += iterationen
            trefferquote = ermittle_trefferquote(box_teil, kreise, iterationen)
            total_simulationen += boxflaeche * trefferquote
    print(f"Anteil uebersprungener Rechtecke: {skipped_boxes / n**2}")
    print(f"Summe aller gezogenen Punkte (in Tsd.): {total_points // 10**3}")
    return total_simulationen + total_boxes

data = [(1.6417233788,   1.6121789534,   0.0848270516,),
    (-1.4944608174 ,  1.2077959613,   1.1039549836,),
     (0.6110294452,  -0.6907087527,   0.9089162485,),
     (0.3844862411,   0.2923344616,   0.2375743054,),
    (-0.2495892950,  -0.3832854473,   1.0845181219,),
     (1.7813504266,   1.6178237031,   0.8162655711,),
    (-0.1985249206,  -0.8343333301,   0.0538864941,),
    (-1.7011985145,  -0.1263820964,   0.4776976918,),
    (-0.4319462812,   1.4104420482,   0.7886291537,),
     (0.2178372997,  -0.9499557344,   0.0357871187,),
    (-0.6294854565,  -1.3078893852,   0.7653357688,),
     (1.7952608455,   0.6281269104,   0.2727652452,),
     (1.4168575317,   1.0683357171,   1.1016025378,),
     (1.4637371396,   0.9463877418,   1.1846214562,),
    (-0.5263668798,   1.7315156631,   1.4428514068,),
    (-1.2197352481,   0.9144146579,   1.0727263474,),
    (-0.1389358881,   0.1092805780,   0.7350208828,),
     (1.5293954595,   0.0030278255,   1.2472867347,),
    (-0.5258728625,   1.3782633069,   1.3495508831,),
    (-0.1403562064,   0.2437382535,   1.3804956588,),
     (0.8055826339,  -0.0482092025,   0.3327165165,),
    (-0.6311979224,   0.7184578971,   0.2491045282,),
     (1.4685857879,  -0.8347049536,   1.3670667538,),
    (-0.6855727502,   1.6465021616,   1.0593087096,),
    ( 0.0152957411,   0.0638919221,   0.9771215985)]
	

"""Einkommentieren zum Ausfuehren"""	
# ~ print(berechne_flaeche(data, 100, 2000))

########################################################################
### Aufgabe 1 ###
########################################################################
"""Offenbar ist die Anzahl der Rechtecke streng deterministisch, hier
wirkt kein Zufallsfaktor. Je mehr Rechtecke wir definieren, desto genauer wird
unsere Schaetzung. Haben wir extrem viele Rechtecke, so koennen wir theoretisch
auf eine Simulation verzichten, da das Raster so fein ist, dass auch damit bereits
gute Ergebnisse approximiert werden koennen. Haben wir hingegen nur sehr wenige
Rechtecke und dafuer sehr viele Punkte, so ist dies fast wie bei der Berechnung
von Pi in einem frueheren Kapitel, dort haben wir auf Rechtecke verzichtet."""


########################################################################
### Aufgabe 2 ###
########################################################################

def simulation2():
	true_value = 21.56503660
	nrechtecke = (5, 20, 50, 100, 400)
	nziehungen = (50, 100, 500, 2000, 5000)
	for nr in nrechtecke:
		for nz in nziehungen:
			print(f"Anzahl Rechtecke: {nr} | Anzahl Ziehungen: {nz}")
			res = berechne_flaeche(data, nr, nz)
			absdiff = round(abs(res - true_value), 6)
			print(absdiff)
			print("************************************")
	
	
"""Einkommentieren zum Ausfuehren. Dieser Code wird eine Weile laufen."""	
simulation2()

