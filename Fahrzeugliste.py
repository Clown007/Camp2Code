from tabulate import tabulate
import random

fahrzeugliste = []


def fuellen():
    hersteller = random.choice(("VW", "Audi", "Bugatti"))
    modell = random.choice(("id.3", "etron", "Golf", "Arteon", "Chiron"))
    leistung = random.randint(30, 1000)
    sitzanzahl = random.randint(2, 8)
    hoechstgeschwindigkeit = random.randint(150, 430)
    return (hersteller, modell, leistung, sitzanzahl, hoechstgeschwindigkeit)


def abfrage():
    hersteller = input("Hersteller ?")
    modell = input("Modell?")
    leistung = input("Leistung?")
    sitzanzahl = input("Anzahl Sitze?")
    hoechstgeschwindigkeit = input("Höchstgeschwindigkeit")
    return (hersteller, modell, leistung, sitzanzahl, hoechstgeschwindigkeit)


abfrage = input("Befüllung automatisch oder manuell (a/m) ")

if abfrage == "a":
    anzahl = int(input("Wie viele Fahrzeuge ?"))
    for i in range(anzahl):
        fahrzeugliste.append(fuellen())

else:
    while True:
        fahrzeugliste.append(abfrage())

        weitere = input("Weitere Fahrzeuge (J/N)?")
        if weitere != "J":
            break

print(
    tabulate(fahrzeugliste, headers=["Hersteller", "Modell", "Leistung", "Sitze", "Geschwindigk."], tablefmt="pretty"))
