import math


def tickets(num):
    galnaMusen = math.floor(num/3)

    lustigaHuset = math.floor(num/2)
    
    flygandeKvasten = math.floor(num/4)

    print("Galna Musen:", galnaMusen, "Lustiga Huset:", lustigaHuset, "Flygande Kvasten:",  flygandeKvasten)

tickets(30)


