my_list = [1, 2, 1, 5, 3, 1, 4, 3, 5, 5]
print(my_list)

for i in my_list:
    if my_list.count(i) > 1:
        for j in range(my_list.count(i) - 1):
            my_list.remove(i)

print(my_list)