#セット
set_a = {'a','b','c','d','a'}

print(set_a)
print('a' in set_a)
print('a' not in set_a)
print(len(set_a))

# method
set_a.add('A')
print(set_a)
set_a.remove('d')
print(set_a)
set_a.discard('B')
val = set_a.pop()
print(val)
set_a.clear()
print(set_a)

#集合
s = {'a','b','c','d'}
t = {'c','d','e','f'}

u = s | t #s.union(t)
print(u)
x = s & t #s.intersection(t)
print(x)
u = s - t #s.difference(t)
print(u)
u = s ^ t #s.symmetric_difference(t)
print(u)

print(s.issubset(t))
print(t.issuperset(s))

print(t.isdisjoint(s)) #重なっている要素があるかどうか
print(t.isdisjoint(u))