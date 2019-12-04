from math import sqrt

primes = [2, ]
count = 1
num = 2

while count < 10_001:
    num += 1
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            break
    else:
        primes.append(num)
        count += 1


print(primes[10_000])


# with applied for-if-else conection
# https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops
