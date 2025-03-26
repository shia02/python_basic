#python 3.10
 
#パターンマッチング
def check_size(size: str):
    match size:
        case 'L' | 'XL':
            print('LかXL')
        case 'M':
            print('M')
        case 'S':
            print('S')
        case _:
            print('そんなのない')

check_size('XL')

#ガード
def check_size_price(size: str, price: int):
    match size:
        case 'L' if price > 0:
            return 'L size'
        case 'M':
            return 'M size'
        case 'S':
            return 'S size'
        case _:
            return 'そんなのない'
        
print(check_size_price('L', 1))

#type hinting
def add_num(a: int | float, b: int | float) -> int | float:
    return a * b

num = add_num(12.3 , 3)
print(isinstance(num, int))
print(isinstance(num, int | float))