#ファイル出力

file_path = '../resources/output.txt'

f = open(file_path, mode='w', encoding='utf-8', newline='\n')
f.write('aaa\nbbb\n')
f.close()

with open(file_path, mode='a', encoding='utf-8', newline='\n') as f:
    list_a = ['a', 'b', 'c']
    f.writelines(list_a)