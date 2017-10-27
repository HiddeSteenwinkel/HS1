#Schrijf (en test) functie wijzig() met één parameter: letterlijst. Zorg dat de functie de lijst leegt en de
#letters [ ‘d’, ‘e’, ‘f’ ] toevoegt. Er is geen return-waarde! Test je programma als volgt:
#lijst = ['a', 'b', 'c']
#print(lijst)
#wijzig(lijst)
#print(lijst)

def wijzig(letterlijst):
    lst.remove(lst[0])
    lst.remove(lst[1])
    lst.remove(lst[2])
    return lst

lst = ['a', 'b', 'c', 'd']
wijzig(lst)
print(lst)