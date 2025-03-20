#for
for i in range(5):
    print(i)
for j in range(2,10,2):
    print(j)

sample = ['a','b','c']
for arr in sample:
    print(arr)

#enumerate, zip, while
for index, arr in enumerate(sample):
    print(index, arr)

sample2 = ['c','d','e','f']
for arr in zip(sample, sample2):
    print(arr)

count = 0
while count < 10:
    print(count)
    count += 1