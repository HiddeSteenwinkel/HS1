infile = open('C:/Users/Hidde/kaartnummers.txt', 'r')
lines = infile.readlines()
infile.close()
aantalRegels = len(lines)
print("Deze file telt", aantalRegels, "regels.")

hoogsteKaartnummer = 0
regelNummer = 0
regel = 0

for line in lines:
    elements = line.split(",")
    kaartNummer = int(elements[0])
    if kaartNummer > hoogsteKaartnummer:
        hoogsteKaartnummer = kaartNummer
        regelNummer = regel


print("Het grootste kaartnummer is", hoogsteKaartnummer, "en dat daat op regel", regelNummer)