def fib_gen():
    i=0
    j=1
    yield 0
    yield 1
    while(True):
        yield i+j
        i,j=j,i+j
    
fib=fib_gen()
print(fib.__next__())
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
        