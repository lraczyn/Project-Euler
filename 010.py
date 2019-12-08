sieve = [True] * 2_000_000
sieve[0], sieve[1] = False, False
prime = []

for i in range(2, len(sieve)):
    if sieve[i]:
        prime.append(i)
        for j in range(i*i, len(sieve), i):
            sieve[j] = False

print(sum(prime))
