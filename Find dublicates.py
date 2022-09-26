# Найти элементы, которые повторяются во всех списках

list1 = [1, 2, 4, 5]
list2 = [3, 3, 4]
list3 = [2, 3, 4, 5, 6]

set1 = set()
set1 = set(list1) & set(list2) & set(list3)
print(set1)

result = [x for x in list1 if x in list2 and x in list3]
print(result)
