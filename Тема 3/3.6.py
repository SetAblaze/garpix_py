reps_num = int(input('Введите количество повторений '))
fib_num = 1
prev_num = 0


for i in range(reps_num):
    fib_num, prev_num = fib_num + prev_num, fib_num
    print('$ ' * fib_num)