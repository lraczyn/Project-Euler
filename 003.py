from math import sqrt

factors = []
value = 600851475143
for i in range(2, int(sqrt(value))):
    if value % i == 0:
        factors.append(i)

prime_factors = factors[:]
for factor in factors:
    for i in range(2, factor):
        if factor % i == 0:
            prime_factors.remove(factor)
            break


print(max(prime_factors))
