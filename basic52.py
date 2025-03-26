from typing import Self

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, other: Self) -> bool:
        return self.name == other.name and self.age == other.age
    
    def copy(self: Self) -> Self:
        return User(self.name, self.age) # type: ignore
    
user1 = User('tao', 12)
user2 = User('tao', 12)
print(user1.compare(user2))
user3 = user1.copy()
print(user3.name)

from typing import LiteralString

def print_msg(msg: LiteralString):
    print(msg)

val = input()
print_msg(val)