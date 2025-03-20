# list
list_a = [1,2,3,4]
list_b = []
print(list_a)
print(list_a[1])

list_a = [1,[1,2,'apple'],3,'banana']
print(list_a)
print(list_a[1][2])
list_a[1][0] = 'lemon'
print(list_a)

# slice, method, sort
list_a = [1,2,3,4,5]
list_b = list_a[:3]
print(list_b)

list_a.append('apple')
print(list_a)
list_a.extend(['banana', 'melon'])
print(list_a)
list_a.insert(1, 'grape')
print(list_a)
list_a.clear()
print(list_a)
list_a = [0,3,2,5,6,1,3]
list_a.remove(3)
print(list_a)
value = list_a.pop()
print(list_a, value)
value = list_a.pop(2)
print(list_a, value)
print(list_a.count(2))
print(list_a.index(1))

list_b = list_a.copy()
print(list_a)
list_b[0] = 4
print(list_a, list_b)
list_a.sort()
# list_a = sorted(list_a) #↑　same
print(list_a)
list_a.reverse()
print(list_a)