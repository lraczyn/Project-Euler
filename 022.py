from string import ascii_uppercase

with open('p022_names.txt') as f:
    names = sorted(next(f).replace('"', '').split(','))


letters_values = {k: v for k, v in zip(ascii_uppercase, range(1, len(ascii_uppercase) + 1))}


def calculate(names, values):
    total_score = 0
    position = 1
    for name in names:
        name_score = 0
        for letter in name:
            name_score += values[letter]
        total_score += position*name_score
        position += 1
    return print(total_score)


calculate(names, letters_values)
