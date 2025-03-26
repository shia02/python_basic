#python v3.9 新機能

#dict連結
ages = {
    'taro': 21,
    'jiro': 32
}
ages_2 = {
    'saburo': 30,
    'hanako': 22,
    'taro': 23
}

#3.8 より前の方法
ages_3 = {**ages, **ages_2}
#3.9
ages_4 = ages | ages_2
print(ages_4)

#removeprefix, removesuffix
msg = 'Hello World'
msg2 = msg.removeprefix('He')
msg2 = msg2.removesuffix('ld')
print(msg2)

#数学
import math
#最大公約数
print(math.gcd(12, 32, 46))
#最小公倍数
print(math.lcm(12,32,46))

#type checking

def add(a: int, b: int):
    return a + b

def print_msg(msg: str):
    print(msg.upper())

print(add(21,32))
print_msg("basic")