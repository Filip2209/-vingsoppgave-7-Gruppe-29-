import matplotlib.pyplot as plt
from datetime import datetime

filnavn = "sinnes_2014_2025_med_makstemperatur.csv"

årstall = input("Skriv inn et årstall: ")

datoer = []
snødybde = []
nedbør = []
middeltemperatur = []
middelvind = []

sommerdager = 0
høysommerdager = 0
tropedager = 0


def gjør_tall(verdi):
    if verdi == "-":
        return None
    return float(verdi.replace(",", "."))

høyeste_dato = None 

with open(filnavn, "r", encoding="UTF-8") as tekstfil:

    overskrift = tekstfil.readline()

    for linje in tekstfil:
        linje = linje.strip()
        if linje == "":
            continue

        deler = linje.split(";")

        dato_tekst = deler[2].strip()

        if dato_tekst == "":
            continue

        dato = datetime.strptime(dato_tekst, "%d.%m.%Y")

        if høyeste_dato is not None and dato <= høyeste_dato:
            continue

        høyeste_dato = dato

        # Sjekker om datoen er fra året brukeren skrev inn
        if dato.year == int(årstall):

            datoer.append(dato)

            middeltemperatur.append(gjør_tall(deler[4]))
            nedbør.append(gjør_tall(deler[5]))
            middelvind.append(gjør_tall(deler[6]))
            snødybde.append(gjør_tall(deler[7]))



            maks_temp = gjør_tall(deler[3])

            if maks_temp is not None:
                if maks_temp > 20:
                    sommerdager += 1

                if maks_temp > 25:
                    høysommerdager += 1

                if maks_temp > 30:
                    tropedager += 1 


# Finner lengste sammenhengende periode uten nedbør

lengste_periode = 0
gjeldende_periode = 0

lengste_start = None
lengste_slutt = None

gjeldende_start = None

for i in range(len(datoer)):

    if nedbør[i] == 0:
        if gjeldende_periode == 0:
            gjeldende_start = datoer[i]

        gjeldende_periode += 1

        if gjeldende_periode > lengste_periode:
            lengste_periode = gjeldende_periode
            lengste_start = gjeldende_start
            lengste_slutt = datoer[i]

    else:
        gjeldende_periode = 0
        gjeldende_start = None


print("Lengste periode uten nedbør:")
print("Lengde:", lengste_periode, "dager")
print("Startdato:", lengste_start.strftime("%d.%m.%Y"))
print("Sluttdato:", lengste_slutt.strftime("%d.%m.%Y"))

print("Antall sommerdager:", sommerdager)
print("Antall høysommerdager:", høysommerdager)
print("Antall tropedager:", tropedager)

# Lager fire grafer
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