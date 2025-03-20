#論理型
is_animal = True
if is_animal:
    print('動物です')
else:
    print('動物ではないです')

is_man = True
is_adult = False

if is_man or is_adult:
    print('男か大人')

if is_man and is_adult:
    print('成人男性')