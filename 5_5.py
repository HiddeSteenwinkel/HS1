zin = input("Voer een willekeurige zin in")
words = zin.split()
average = sum(len(word) for word in words) / len(words)
average(zin)