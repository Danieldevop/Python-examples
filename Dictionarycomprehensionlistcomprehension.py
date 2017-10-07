# Dictionary comprehension - list comprehension

pares = []

for num in range(1,31):
    if num % 2 == 0:
        pares.append(num)

pares = [num for num in range(1,31) if num % 2 == 0]