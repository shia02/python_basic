
def genarate_emeny_hand():
    while True:
        yield '1'
        yield '2'
        yield '3'

def is_won(my_hand, emeny_hand):
    if my_hand == '1' and emeny_hand == '2':
        return True
    elif my_hand == '2' and emeny_hand == '3':
        return True
    elif my_hand == '3' and emeny_hand == '1':
        return True
    else:
        return False


hands_dict = {'1': 'グー', '2': 'チョキ', '3':'パー'}
lose_count = 0
emeny_hands = genarate_emeny_hand()

while True:
    my_hand = input('何を出す? 1:グー 2:チョキ 3:バー')
    if my_hand not in ('1','2','3'):
        print('間違った入力です')
        continue
    emeny_hand = next(emeny_hands)
    # from random import randint
    # emeny_hand = str(randint(1,3))
    print(f'あなたの手：{hands_dict.get(my_hand)} 相手の手:{hands_dict.get(emeny_hand)}')

    if my_hand == emeny_hand:
        print('あいこ')
    elif is_won(my_hand, emeny_hand):
        print('あなたの勝ち')
        break
    else:
        lose_count += 1
        if lose_count == 3:
            print('あなたは負けました')
            break
        else:
            print('あなたの負け、再チャレンジ')
    