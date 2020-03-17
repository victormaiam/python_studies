#escrever um programa que remove duplicatas de uma lista
numbers = [5, 2, 1, 5, 7, 4]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)