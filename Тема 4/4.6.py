my_list = []

while(True):
    buff = str(input('Введите строку '))
    if buff == 'q':
        break
    my_list.append(buff)

print(my_list)