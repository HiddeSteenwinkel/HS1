def standaardprijs(afstandKM):
    if afstandKM >= 50:
        vastBedrag = 15
        variableBedrag = 0.60
        normaleprijs = vastBedrag + (variableBedrag * afstandKM)
        return normaleprijs
    elif afstandKM <= 0:
        return 0
    else:
        variableBedrag = 0.80
        normaleprijs = (variableBedrag * afstandKM)
        return normaleprijs




def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    kinderen = leeftijd < 12
    ouderen = leeftijd >= 65
    if (kinderen or ouderen) and weekendrit == False:
        return prijs * 0.7
    elif (kinderen or ouderen) and weekendrit:
        return prijs * 0.65
    elif (kinderen or ouderen) == False and weekendrit == False:
        return prijs
    else:  # (kinderen == False and ouderen == False) and weekendrit
        return prijs * 0.6

print(ritprijs(11, False, -1))