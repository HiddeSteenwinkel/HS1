
def getal_invullen():
    lst = []

    uitkomst = eval(input("Geef een getal: "))

    while uitkomst != 0:
        lst.append(uitkomst)
        uitkomst = eval(input("Geef een getal: "))

    print("Er zijn", len(lst), "getallen ingevoerd, de som van deze getallen is: ", sum(lst))

getal_invullen()