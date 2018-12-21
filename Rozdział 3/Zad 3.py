# Jaka to liczba?
#
# Komputer wybiera losowo liczbę z zakresu od 1 do 100.
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy podana przez niego liczba jest: za duża, za mała
# czy prawidłowa

import random

print("\tWitaj w grze 'Jaka to liczba?'!")
print("\nMam na myśli pewną liczbę od 1 do 100.")
print("Masz 5 podejść.\n")

# ustaw wartości początkowe
the_number = random.randint(1, 100)
guess = int(input("Ta liczba to... "))
tries = 5
proby = 1

# pętla zgadywania
while guess != the_number:
    if tries <= 1:
        break
    elif guess > the_number:
        print("Za duża...")
    else:
        print("Za mała...")    

    guess = int(input("Ta liczba to: "))
    tries -= 1
    proby += 1

if tries <= 1:
    print("Przegrałeś, spróbuj jeszcze raz!")
else:
    print("Wygrałeś, ta liczba to", the_number)
    print("Potrzebowałeś", proby, "prób!")



input("\n\nEnter")
