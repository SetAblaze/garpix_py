my_list = [1, 2, 3, 4, 5, 6]
buff = my_list[0]

print(my_list)

my_list[0] = my_list.pop()
my_list.append(buff)

print(my_list)