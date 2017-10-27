kluizen = []

maxKluizen = 12

def lees_kluizen():

    bestand = open('C:/Users/hidde/kluizen.txt', 'r')
    regels = bestand.readlines()
    for regel in regels:
        kluizen.append(regel.split(';'))
    bestand.close()
    return kluizen

def schrijf_kluizen(kluisnummer, wachtwoord):
    bestand = open('C:/Users/hidde/kluizen.txt', 'a')
    s = str(kluisnummer) + ";" + str(wachtwoord) + '\n'
    bestand.write(s)
    bestand.close()


def zoek_kluis(kluizen, kluis_nr):
    for kluis in kluizen:
        if kluis[0] == kluis_nr:
            return kluis
        return

def toon_aantal_kluizen_vrij():
    kluizen = lees_kluizen()
    print("Aantal vrije kluizen: ", maxKluizen - len (kluizen))
    #doe iets

def nieuwe_kluis():
    kluizenlijst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    kluizen = lees_kluizen()

    for kluis in kluizen:
        for kluisnummer in kluizenlijst:
            if kluisnummer == int(kluis[0]):
                kluizenlijst.remove(int(kluis[0]))

    print("U krijgt kluis: ", kluizenlijst[0])
    wachtwoord = eval(input("Geef hier je wachtwoord: "))
    schrijf_kluizen(kluizenlijst[0], wachtwoord)
    print("U heeft kluisnummer: ", kluizenlijst[0], "met wachtwoord:", wachtwoord)


def kluis_openen():
    kluizen = lees_kluizen()
    gebruiker_kluisnummer = eval(input('Welk kluisnummer is van jou?: '))
    gebruiker_wachtwoord = eval(input("Welk wachtwoord hoort bij deze kluis?: "))
    combi = False
    for kluis in kluizen:
        if int(kluis[0]) == gebruiker_kluisnummer and gebruiker_wachtwoord == int(kluis[1]):
            combi = True
            break

    if combi:
        print("Gelukt, dat is jouw kluis.")
    else :
        print("Foute combi.")





def kluis_teruggeven():
    print("kluis_teruggeven")
    kluizen = lees_kluizen()
    #doe iets
    schrijf_kluizen(kluizen)

while True:
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: ik geef mijn kluis terug")
    print("5: Ik wil stopppen")

    keuze = eval(input("Uw keuze: "))
    if keuze == 1:
        toon_aantal_kluizen_vrij()
    elif keuze == 2:
        nieuwe_kluis()
    elif keuze == 3:
        kluis_openen()
    elif keuze == 4:
        kluis_teruggeven()
    elif keuze == 5:
        break
    else:
        print("Ongeldige keuze")
