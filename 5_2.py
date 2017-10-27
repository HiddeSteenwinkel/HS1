infile = open('C:/Users/Hidde/kaartnummers.txt', 'r')
lines = infile.readlines()
infile.close()

naam = 0
kaartNummer = 0


for line in lines:
    elements = line.split(",")
    kaartNummer = int(elements[0])
    naam = elements[1]


print(naam, "heeft kaartnummer:", kaartNummer )
print(naam, "heeft kaartnummer:", kaartNummer )
print(naam, "heeft kaartnummer:", kaartNummer )
print(naam, "heeft kaartnummer:", kaartNummer )
print(naam, "heeft kaartnummer:", kaartNummer )
print(naam, "heeft kaartnummer:", kaartNummer )