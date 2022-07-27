N = int(input('Введите количество чисел '))
even_count = 0

for i in range(N):
    num = int(input('Введите число '))
    if num % 2 == 0:
        even_count += 1

print(f'Количество четных чисел: {even_count}')