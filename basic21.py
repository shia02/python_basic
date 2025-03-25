#inner関数
def outer():
    outer_value = 'outer'
    def inner():
        nonlocal outer_value
        outer_value = 'inner'
        print(outer_value, id(outer_value))
    inner()
    print(outer_value, id(outer_value))

outer()