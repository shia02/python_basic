#多重継承
class ClassA:
    def __init__(self, name):
        self.name = name

    def print_a(self):
        print(f'ClassA print {self.name}')

class ClassB:
    def __init__(self,name):
        self.name = name

    def print_b(self):
        print(f'ClassB print {self.name}')

class ClassC(ClassA, ClassB):
    def __init__(self, name, name_a):
        ClassA.__init__(self, name_a)
        ClassB.__init__(self, name)

class_c = ClassC('name', 'name_a')
class_c.print_a()
class_c.print_b()