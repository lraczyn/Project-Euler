# checking
def check(num):
    for i in range(1, 21):
        if num % i != 0:
            return False

    return True


# loop
num = 20
while True:
    if check(num):
        break
    else:
        num += 20

print(num)
