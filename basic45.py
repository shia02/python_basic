#ファイル入力

file_path = 'input.txt'
# f = open(file_path, mode='r', encoding='utf-8')

# # line = f.read()
# # print(line)

# while (line := f.readline()):
#     print(line.strip('\n'))
# f.close()

with open(file_path, mode='r', encoding='utf-8') as f:
    while (line := f.readline()):
        print(line.strip('\n'))