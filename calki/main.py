calka = 0
a = 0
b = 2
E = 1000

szerokosc = (b - a) / E


def f(x):
    return x * x + 1


for i in range(E):
    wysokosc = f(a + i * szerokosc)
    calka += szerokosc * wysokosc

print("Całka wynosi:", calka)
