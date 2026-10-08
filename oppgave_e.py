from datetime import datetime

FILNAVN = "sinnes_2014_2025.csv"
MIN_SNODYBDE = 20  # det er skiføre når snødybden er minst 20 cm


def les_data(filnavn):
    """Leser filen og returnerer to lister: datoer (datetime) og snødybder (cm)."""
    datoer = []
    snodybder = []
    with open(filnavn, encoding="utf-8-sig") as fil:
        fil.readline()  # hopper over overskriftslinjen
        for linje in fil:
            # Deler linjen opp i kolonner ved hvert semikolon
            deler = linje.strip().split(";")
            if deler[2] == "":  # hopper over tekstlinjen nederst i filen
                continue
            # Kolonne 2 er datoen, som vi gjør om fra tekst til datetime
            dato = datetime.strptime(deler[2], "%d.%m.%Y")
            # Kolonne 6 er snødybden
            snø_tekst = deler[6]
            if snø_tekst == "-":  # "-" betyr at verdien mangler
                snodybde = None
            else:
                # Filen bruker komma som desimaltegn, Python vil ha punktum
                snodybde = float(snø_tekst.replace(",", "."))
            datoer.append(dato)
            snodybder.append(snodybde)
    return datoer, snodybder


def skifore_dager(datoer, snodybder, aar):
    """Teller dager med skiføre i skisesongen: 1. november året før til 31. mai."""
    start = datetime(aar - 1, 11, 1)
    slutt = datetime(aar, 5, 31)
    antall = 0
    # zip lar oss gå gjennom dato og snødybde samtidig
    for dato, snodybde in zip(datoer, snodybder):
        # Bare dager i sesongen, og bare dager der snødybden er målt
        if start <= dato <= slutt and snodybde is not None:
            if snodybde >= MIN_SNODYBDE:
                antall += 1
    return antall


def main():
    datoer, snodybder = les_data(FILNAVN)
    aar = int(input("Skriv inn et årstall: "))
    antall = skifore_dager(datoer, snodybder, aar)
    print(f"Antall dager med skiføre i skisesongen {aar - 1}/{aar}: {antall}")


if __name__ == "__main__":
    main()