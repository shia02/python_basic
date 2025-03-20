#tuple
fruit = ('apple', 'banana', 'grape')
print(fruit[0])
fruit = fruit + ('orange',)
print(fruit)
print(type(fruit))
list_fruit = ['apple', 'banana']
fruit = tuple(list_fruit)
print(fruit)
print(fruit.count('apple'))
print(fruit.index('banana'))