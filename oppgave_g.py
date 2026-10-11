from datetime import datetime

filnavn = "sinnes_2014_2025_med_makstemperatur.csv"

lengste_periode = 0
gjeldende_periode = 0

lengste_start = None
lengste_slutt = None

gjeldende_start = None


with open(filnavn, "r", encoding="UTF-8") as fil:

    fil.readline()

    for linje in fil:
        if linje.strip() == "":
            continue
        deler = linje.strip().split(";")
        if deler[2].strip() == "":
            continue

        dato = datetime.strptime(deler[2], "%d.%m.%Y")

        nedbør = deler[5].strip()

        if nedbør == "0" or nedbør == "0,0":

            if gjeldende_periode == 0:
                gjeldende_start = dato

            gjeldende_periode += 1

            if gjeldende_periode > lengste_periode:
                lengste_periode = gjeldende_periode
                lengste_start = gjeldende_start
                lengste_slutt = dato

        else:
            gjeldende_periode = 0
            gjeldende_start = None


print("Lengste sammenhengende periode uten nedbør:")
print("Antall dager:", lengste_periode)
print("Startdato:", lengste_start.strftime("%d.%m.%Y"))
print("Sluttdato:", lengste_slutt.strftime("%d.%m.%Y"))
