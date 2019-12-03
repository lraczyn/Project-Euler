t = []
for i in range(1000):
    if i % 3 == 0:
        t.append(i)
        continue
    if i % 5 == 0:
        t.append(i)

print(sum(t))
