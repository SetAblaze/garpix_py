def average(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)

print(average(2, 2, 2, 2, 4, 6))