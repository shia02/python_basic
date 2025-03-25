#メタクラス
class MetaException(Exception):
    pass

class Meta1(type):
    def __new__(metacls, name, bases, class_dict):
        print(f'metacls = {metacls}')
        print(f'name = {name}')
        print(f'bases = {bases}')
        print(f'class_dict = {class_dict}')
        if 'my_var' not in class_dict.keys():
            raise MetaException('my_varを定義してください')
        for base in bases: #継承させたくないクラスがある場合使用する、finalクラス
            if isinstance(base, Meta1):
                raise MetaException('継承できません')
        return super().__new__(metacls, name, bases, class_dict)
    
class ClassA(metaclass=Meta1):
    a = '123'
    my_var = 'm7'
    pass