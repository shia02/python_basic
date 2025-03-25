#再帰
def sample(a):
    if a < 0:
        return
    else:
        print(a)
        sample(a-1)

def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
print(fib(10))