#インスタンス変数
class SampleA():
    class_val = 'class val'
    def set_val(self):
        self.instance_val = 'instance val'

    def print_val(self):
        print(f'class={self.class_val=}')
        print(f'instance={self.instance_val=}')

instance_a = SampleA()
instance_a.set_val()
print(instance_a.instance_val)
instance_a.print_val()
print(SampleA.class_val)
print(id(instance_a.__class__.class_val))
instance_b = SampleA()
print(id(instance_b.__class__.class_val))