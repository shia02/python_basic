num = 10
print(num)
num_str = str(num)
num_list = [num_str, '20', '30']
num_list.append('40')
num_tuple = tuple(num_list)
val = input()
num_tuple = num_tuple + (val,)
num_set = {'40','50','60'}
print(set(num_tuple) | num_set)
num_dict = {num_tuple: num_str}
print(len(num_list))
print(num_dict.get('MyKey', 'Does not exist'))
num_list.extend(['50','60'])
val = input()
is_under_50 = int(val) < 50
print(f'{num_str=}')
print(dir(num_dict))