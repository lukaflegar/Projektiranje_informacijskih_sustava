import math

def osnovne_operacije():
    print("\n--- Osnovne Operacije ---")
    # Kod za osnovne operacije (zbrajanje, oduzimanje, množenje, dijeljenje)

def napredne_operacije():
    print("\n--- Napredne Operacije ---")
    # Kod za napredne operacije ( potencija, logaritam s bazom 10, prirodni logaritam)

def binarne_operacije():
    print("\n--- Binarne Operacije ---")
    # Kod za binarne operacije (binarno zbrajanje, oduzimanje i shift lijevo ili desno) 
    
def pretvaranje_temperature():
    print("\n--- Pretvarač Temperature ---")
    #Kod za konverter temperature (pretvaranje vrijednosti temperature iz Celzijus u Farenhajt)

def main():
    while True:
        print("\n===== Jednostavni Kalkulator =====")
        print("1. Osnovne Operacije")
        print("2. Napredne Operacije")
        print("3. Binarne Operacije")
        print("4. Pretvarač Temperature")
        print("5. Izlaz")
        
        glavni_izbor = input("Unesite svoj izbor (1-5): ")
        
        if glavni_izbor == '1':
            osnovne_operacije()
        elif glavni_izbor == '2':
            napredne_operacije()
        elif glavni_izbor == '3':
            binarne_operacije()
        elif glavni_izbor == '4':
            pretvaranje_temperature()
        elif glavni_izbor == '5':
            print("Hvala što ste koristili kalkulator. Doviđenja!")
            break
        else:
            print("Neispravan izbor! Molimo pokušajte ponovno.")

if __name__ == "__main__":
    main()