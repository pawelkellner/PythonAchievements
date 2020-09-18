import sys
import time

def bellen(naam, game, tijd):
    print("S: Hoi, met wie spreek ik")
    time.sleep(1)
    print("Y: Je spreekt met", naam)
    time.sleep(1)
    print("S: Oh, lang niet gesproken")
    time.sleep(1)
    print("S: Welke game speel je nu?")
    time.sleep(1)
    print("Y: Ik ben laatste tijd veel", game, " aan het spelen")
    time.sleep(1)
    print("S: Hoelaat is het nu bij jou?")
    time.sleep(1)
    print("Y: Het is", tijd)
    time.sleep(1)
    if int(tijd) <= 15:
        print("S: Wat is het vroeg bij jullie")
    else:
        print("S: Wat laat bij ons is het 15 uur")
    time.sleep(1)
    print("Y: Ik moet gaan doei!")
    print("S: Later!")

bellen(sys.argv[1], sys.argv[2], sys.argv[3])
