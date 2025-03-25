#ジェネレーター関数
def generator(max):
    print('ジェネレーター作成')
    for n in range(max):
        x = yield n
        print(f'{x=}')
        print('yield実行')

gen = generator(10)
next(gen)
gen.send(100)
# gen.throw(Exception)
# gen.close()
next(gen)
# for x in gen:
#     print(f'x = {gen}')

#listよりgeneratorのほうがメモリ使用率がはるかに少ないので、大量のデータを処理する際に使用する
import sys
list_a = [i for i in range(100000)]
def num(majx):
    i = 0
    while i < majx:
        yield i
        i += 1
gen = num(100000)
print(sys.getsizeof(list_a))
print(sys.getsizeof(gen))