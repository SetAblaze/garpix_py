def two_sum(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    else:
        raise TypeError('Ожидаемый тип данных — число')

print(two_sum(2,3))
two_sum('se', 2)
