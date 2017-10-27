lst = [5, 9, 7, 1, 7, 8, 3, 2, 4, 8, 7, 9]

print('het laagste getal is: ', min(lst))
print('het hoogste getal is: ', max(lst))

aantalGetallen = 0
for i in lst:
    aantalGetallen = aantalGetallen + 1

print('som van de getallen: ', sum(lst), ' en het aantal getallen: ', aantalGetallen)

testGetal = 0

for i in lst:
    if i > 0:
        testGetal += i


gemiddeldeGetallen = testGetal / aantalGetallen
print('Het gemiddelde van deze getallen is: ', gemiddeldeGetallen)