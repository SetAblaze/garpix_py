reps_num = int(input('Введите количество повторений '))
fib_num = 1
prev_num = 0
buff = 0

for i in range(reps_num):
    buff = fib_num
    fib_num += prev_num
    prev_num = buff
    print('$ ' * (fib_num))