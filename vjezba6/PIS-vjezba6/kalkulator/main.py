from kalkulator.izrsavanje_operacije import IzrsavanjeOperacije
from kalkulator.file_writer import FileWriter

def main():
    print("Unesite dva operanda i odaberite matematičku operaciju:")
    print("1 za zbrajanje\n2 za oduzimanje\n3 za množenje\n4 za dijeljenje\n")

    try:
        operand1 = float(input("Operand 1: "))
        operand2 = float(input("Operand 2: "))
        izbor = int(input("Izbor (1-4): "))

        if izbor not in [1, 2, 3, 4]:
            print("Neispravan izbor!")
            return

        writer = FileWriter()
        izvrsi = IzrsavanjeOperacije(writer)
        rezultat = izvrsi.izvrsi_operaciju_spremi(operand1, operand2, izbor)
        print(f"Rezultat je: {rezultat}")

    except ValueError as e:
        print(f"Greška: {e}")

if __name__ == "__main__":
    main()
