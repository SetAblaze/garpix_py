list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]

res = list(filter(lambda x: x != "",list1))

print(res)