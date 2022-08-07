lst1 = ['Санкт-Петербург', 'Москва', 'Казань', ]
lst2 = ['Воронеж', 'Санкт-Петербург', 'Иваново', 'Жуковский']

my_list1 = set(lst1)
my_list1.intersection_update(lst1, lst2)
my_list2 = set(lst2)
my_list2.update(lst1)
my_list2.difference_update(my_list1)

print(my_list1)
print(my_list2)