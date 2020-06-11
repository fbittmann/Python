


#Felix Bittmann
#Praxishandbuch Python 3
#https://github.com/fbittmann/Python



import random
def gen_erzeuger(anzahl, laenge):
    alphabet = "ACGT"
    return [
        "".join(random.choices(alphabet, k=laenge))
        for _ in range(anzahl)
    ]


def lcs(eingabe):
    referenz = eingabe[0]
    tested = set()
    for laenge in range(len(referenz), 0, -1):
        for pos in range(0, len(referenz) + 1 - laenge):
            subsequenz = referenz[pos : pos + laenge]
            if subsequenz not in tested:
                if all(subsequenz in sequenz for sequenz in eingabe[1:]):
                    return subsequenz
                tested.add(subsequenz)
    return ""



def main():
	data = gen_erzeuger(3, 14)
	print(data)
	print(lcs(data))
	
	
random.seed(12345)
main()


