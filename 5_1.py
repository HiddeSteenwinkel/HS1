def convert(Celsius):
    Tf = Celsius * 1.8 + 32
    return (Tf)

def table():
    print(' F        C')
    formatStr = "{0:2d} {1:6d}"
    for Celsius in range(-30, 41, 10):
        Tf = Celsius * 1.8 + 32
        print(formatStr.format(Tf, Celsius))

table()
