
def unos_kompleksnosti(naziv_komponente, tezine):
    print(f"\nUnos za {naziv_komponente}:")
    broj_niskih = int(input(f"Unesi broj komponenti {naziv_komponente} niske kompleksnosti: "))
    broj_srednjih = int(input(f"Unesi broj komponenti {naziv_komponente} srednje kompleksnosti: "))
    broj_visokih = int(input(f"Unesi broj komponenti {naziv_komponente} visoke kompleksnosti: "))

    ukupna_kompleksnost = (
        broj_niskih * tezine['low'] +
        broj_srednjih * tezine['ave'] +
        broj_visokih * tezine['high']
    )
    print(f"Ukupna vrijednost za {naziv_komponente}: {ukupna_kompleksnost}")
    return ukupna_kompleksnost

def izracun_ei():
    tezine = {'low': 3, 'ave': 4, 'high': 6}
    return unos_kompleksnosti("External Inputs (EI)", tezine)

def izracun_eo():
    tezine = {'low': 4, 'ave': 5, 'high': 7}
    return unos_kompleksnosti("External Outputs (EO)", tezine)

def izracun_eq():
    tezine = {'low': 3, 'ave': 4, 'high': 6}
    return unos_kompleksnosti("External Queries (EQ)", tezine)

def izracun_ilf():
    tezine = {'low': 7, 'ave': 10, 'high': 15}
    return unos_kompleksnosti("Internal Logical Files (ILF)", tezine)

def izracun_eif():
    tezine = {'low': 5, 'ave': 7, 'high': 10}
    return unos_kompleksnosti("External Interface Files (EIF)", tezine)

def izracun_tafp(tufp):
    vaf = 0.65
    return tufp * vaf

def izracun_loc(tafp): 
    return tafp * 59

def main():
    tufp = (
        izracun_ei() +
        izracun_eo() +
        izracun_eq() +
        izracun_ilf() +
        izracun_eif()
    )
    tafp = izracun_tafp(tufp)
    loc = izracun_loc(tafp)

    print(f"\nUkupni broj neprilagođenih funkcijskih točaka (TUFP): {tufp}")
    print(f"Ukupni broj prilagođenih funkcijskih točaka (TAFP): {round(tafp, 2)}")
    print(f"Okviran broj linija C# koda: {round(loc,2)}")

if __name__ == "__main__":
    main()
