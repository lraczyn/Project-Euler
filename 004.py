polindromic_numbers = []


def check_polindromicity(n):
    n = str(n)
    if n == n[::-1]:
        return 'polindromic'


for i in range(100, 1000):
    for j in range(100, 1000):
        if check_polindromicity(i*j):
            polindromic_numbers.append(i*j)

print(max(polindromic_numbers))
