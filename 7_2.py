def string_invullen():

    uitkomst = input("Geef een string van 4 letters: ")

    while len(uitkomst) != 4:
        print(uitkomst, "heeft", len(uitkomst), "letters")
        uitkomst = input("Geef een string van 4 letters: ")
        if len(uitkomst) == 4:
            print("Inlezen van correcte string is geslaagd: ", uitkomst)
            break





string_invullen()