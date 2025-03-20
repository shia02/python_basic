#文字列
fruit = """apple
orange
grape"""

print(fruit * 2)
print(type(fruit))
print(fruit[10])
print(fruit[-1])
new_fruit = fruit + ' ok'
print(new_fruit)

#encode, decode
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))
str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

#count
msg = 'ABCDEABC'
print(msg.count('ABC'))

#startswith, endswith
print(msg.startswith('ABC'))
print(msg.endswith('BC'))

# strip, rstrip, lstrip
msg = ' ABC '
print(msg)
print(msg.strip())
print(msg.rstrip())
print(msg.lstrip())
msg = 'ABCDEFABC'
print(msg.strip('CB'))

# upper, lower, swapcase, replace, capitalize
msg = 'abcABC'
print(msg.upper())
print(msg.lower())
print(msg.swapcase())
print(msg.replace('abc', 'def'))
print(msg.capitalize())

# 一部取り出し, format, islower, isupper
msg = 'hello, my name is taro'
print(msg[1:5])
print(msg[1:15:2])
print('hello {}'.format('Taro'))
print(f'hello {msg}')
print(msg.islower(), msg.isupper())

# find, index, rfind, rindex
msg = 'ABCDEABC'
print(msg.find('ABC'))
print(msg.rfind('ABC'))
print(msg.index('ABC'))
print(msg.rindex('ABC'))