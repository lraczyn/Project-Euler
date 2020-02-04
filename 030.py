def digit_power(power):
    l = []
    for i in range(2, 295245):
        _sum = 0
        for digit in str(i):
            _sum += int(digit)**power
        if i == _sum:
            l.append(i)
        value = sum(l)
    return print(value)


digit_power(5)
