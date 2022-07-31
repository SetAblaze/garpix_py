lst1 = ['Санкт-Петербург', 'Москва', 'Казань', ]
lst2 = ['Воронеж', 'Санкт-Петербург', 'Иваново', 'Жуковский']
my_list1 = []
my_list2 = []

for i in lst1:
    for j in lst2:
        if i == j:
            my_list1.append(i)
        if lst2.count(i) == 0 and my_list2.count(i) < 1:
            my_list2.append(i)
        elif lst1.count(j) == 0 and my_list2.count(j) < 1:
            my_list2.append(j)

print(my_list1)
print(my_list2)