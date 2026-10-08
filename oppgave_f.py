from datetime import datetime

FILNAVN = "sinnes_2014_2025_med_makstemperatur.csv"
MIN_TEMP = 5  # planten trenger minst 5 plussgrader for å vokse


def les_data(filnavn):
    """Leser filen og returnerer to lister: datoer (datetime) og middeltemperaturer."""
    datoer = []
    temperaturer = []
    with open(filnavn, encoding="utf-8-sig") as fil:
        fil.readline()  # hopper over overskriftslinjen
        for linje in fil:
            # Deler linjen opp i kolonner ved hvert semikolon
            deler = linje.strip().split(";")
            if deler[2] == "":  # hopper over tekstlinjen nederst i filen
                continue
            # Kolonne 2 er datoen, som vi gjør om fra tekst til datetime
            dato = datetime.strptime(deler[2], "%d.%m.%Y")
            # Kolonne 4 er middeltemperaturen
            temp_tekst = deler[4]
            if temp_tekst == "-":  # "-" betyr at verdien mangler
                temp = None
            else:
                # Filen bruker komma som desimaltegn, Python vil ha punktum
                temp = float(temp_tekst.replace(",", "."))
            datoer.append(dato)
            temperaturer.append(temp)
    return datoer, temperaturer


def plantevekst(datoer, temperaturer, aar):
    """Summerer (temperatur - 5) for alle dager i året med temperatur over 5 grader."""
    total = 0
    # zip lar oss gå gjennom dato og temperatur samtidig
    for dato, temp in zip(datoer, temperaturer):
        # dato.year gir årstallet; vi hopper over dager uten måling
        if dato.year == aar and temp is not None and temp > MIN_TEMP:
            total += temp - MIN_TEMP  # veksten denne dagen
    return total


def main():
    datoer, temperaturer = les_data(FILNAVN)
    aar = int(input("Skriv inn et årstall: "))
    print(f"Total plantevekst i {aar}: {plantevekst(datoer, temperaturer, aar):.1f}")


if __name__ == "__main__":
    main()