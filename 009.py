def check(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


for a in range(1, 1000):
    for b in range(a, 1000 - a):
        c = 1000 - a - b
        if check(a, b, c):
            print(a*b*c)
