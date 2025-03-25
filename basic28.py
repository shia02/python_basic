#list内包表記
list_a = [1,2,3,'a',5]
new_list = [x for x in list_a] #下記と同様
# for x in list_a:
#     new_list.append(x)
new_list2 = [x * x for x in list_a if type(x) == int]
print(new_list2)
list_b = [x for x in range(100) if x % 7 == 0]
print(list_b)

dict_a = {'a': 'A', 'b': 'B'}
list_c = [dict_a.get(x) for x in list_a if dict_a.get(x) != None]
print(list_c)