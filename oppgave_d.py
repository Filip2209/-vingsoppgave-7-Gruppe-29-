import matplotlib.pyplot as plt
from datetime import datetime

filnavn = "sinnes_2014_2025.csv"

årstall = input("Skriv inn et årstall: ")

datoer = []
snødybde = []
nedbør = []
middeltemperatur = []
middelvind = []


def gjør_tall(verdi):
    if verdi == "-":
        return None
    return float(verdi.replace(",", "."))


høyeste_dato = None

with open(filnavn, "r", encoding="UTF-8") as tekstfil:

    # Hopper over overskriften
    overskrift = tekstfil.readline()

    for linje in tekstfil:
        linje = linje.strip()

        # Hopper over tomme linjer
        if linje == "":
            continue

        deler = linje.split(";")

        # Dato ligger i kolonne 2
        dato_tekst = deler[2].strip()

        # Hopper over rader uten dato
        if dato_tekst == "":
            continue

        dato = datetime.strptime(dato_tekst, "%d.%m.%Y")

        # Forkaster datoer som er tidligere enn
        # eller lik den høyeste datoen vi har lest
        if høyeste_dato is not None and dato <= høyeste_dato:
            continue

        høyeste_dato = dato

        # Sjekker om datoen er fra året brukeren skrev inn
        if dato.year == int(årstall):

            datoer.append(dato)

            # Middeltemperatur
            middeltemperatur.append(gjør_tall(deler[4]))

            # Nedbør
            nedbør.append(gjør_tall(deler[4]))

            # Høyeste middelvind
            middelvind.append(gjør_tall(deler[5]))

            # Snødybde
            snødybde.append(gjør_tall(deler[6]))


# Lager grafene
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(datoer, snødybde)
plt.ylabel("Snødybde")
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(datoer, nedbør)
plt.ylabel("Nedbør")
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(datoer, middeltemperatur)
plt.ylabel("Temperatur")
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(datoer, middelvind)
plt.ylabel("Middelvind")
plt.xlabel("Dato")
plt.grid()

plt.suptitle("Værdata for " + årstall)

plt.tight_layout()
plt.show()