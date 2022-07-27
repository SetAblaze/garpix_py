a = int(input('Введите сторону '))
b = int(input('Введите сторону '))
c = int(input('Введите сторону '))

if a < b + c and b < a + c and c < a + b:
    print('Треугольник существует')
else:
    print('Треугольник не существует')