a = input('Введите сторону a ')
b = input('Введите сторону b ')
c = input('Введите сторону c ')

if a == b or b == c or c == a:
    if a == b and b == c:
        print('Треугольник не является равнобедренным ')
    else:
        print('Треугольник является равнобедренным ')
else:
    print('Треугольник не является равнобедренным ')