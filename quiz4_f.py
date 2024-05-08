sequence = input('Enter a sequence of integers seprated by whitespace: ')
sequence = sequence.split(' ')  # str -> list
sequence = [int(x) for x in sequence]  # char -> int

temp_LICS = [sequence[0]]  # 5
LICS = []  # initial empty

for element in sequence[1:]:
    if element > temp_LICS[-1]:
        temp_LICS.append(element)  # 5, 6
    else:
        if len(temp_LICS) > len(LICS):
            LICS = temp_LICS
        temp_LICS = [element]

if len(temp_LICS) > len(LICS):
    LICS = temp_LICS

print("Length : ",len(LICS))
print("LICS : ",LICS)