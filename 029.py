set = set()


def distinct_powers(a, b):
    for a in range(2, a+1):
        for b in range(2, b+1):
            set.add(a**b)


distinct_powers(100, 100)
print(len(set))
