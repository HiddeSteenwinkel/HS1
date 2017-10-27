def seizoen(maand):
    if maand <= 0:
        print("Deze maand bestaat niet.")
    elif maand > 12:
        print("Deze maand bestaat niet.")
    elif maand < 4:
        print("Winter")
    elif maand < 6:
        print("Lente")
    elif maand < 9:
        print("Zomer")
    elif maand < 12:
        print("Herfst")

seizoen(5)