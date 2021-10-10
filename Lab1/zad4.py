def zad2(imie, nazwisko):


    return imie[0].capitalize() + ". " + nazwisko.capitalize()

def zad4(imie, nazwisko, func):
    return  func(imie, nazwisko)

print(zad4("bohdan", "lukaszewicz",zad2))


