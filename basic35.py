#特殊メソッド
class Human:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return 'Human:' + self.name + ',' + str(self.age) + ',' + str(self.phone)
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name + self.phone)
    
    def __bool__(self):
        return True if self.age >= 20 else False
    
    def __len__(self):
        return len(self.name)
    
man = Human('Taro', 20, '09000000000')
print(man)
man2 = Human('Taro', 19 ,'23')
man3 = Human('Taro', 19 ,'23')
print(man2)
print(man == man2)
set_mens = {man, man2, man3}
for x in set_mens:
    print(x)

if man2:
    print('20以上')
else:
    print('20未満')

print(len(man))