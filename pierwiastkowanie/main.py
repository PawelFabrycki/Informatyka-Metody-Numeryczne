P = 9
E = 0.001
a1 = 1
a2 = P

def wb(a):
    return abs(a)

while wb(a1 - a2) > E:
    a1 = (a1 + a2) / 2
    a2 = P/a1

print("Przybliżony pierwiastek kwadratowy z", P, "to: ", a1)
