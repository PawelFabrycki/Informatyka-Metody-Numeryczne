a = -1
b = 4
E = 0.0001


def f(x):
    return 2 * x - 1


def wb(x):
    return abs(x)


if f(a) * f(b) > 0:
    print("Funkcja niema miejsca zerowego")

else:
    while wb(a - b) > E:

        s = (a + b) / 2
        if f(a) * f(s) <= 0:
            b = s
        else:
            a = s
    print(f"Przybliżone miejsce zerowe to {(a + b) / 2}")