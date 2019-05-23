# fib(0) = 0
# fib(1) = 1
# fib(n) = fib(n-1) + fib(n-2)

# Brute force solution with poor run time:

# def fib(n):
#     if n == 0:
#         return 0
    
#     if n == 1:
#         return 1
    
#     return fib(n-1) + fib(n-2)

# for i in range(10):
#     print(fib(i))


# Memoization (top down) solution

cache = {}

def fib_memo(n):

    if n not in cache:
        cache[n] = fib_memo(n-1) + fib_memo(n-2)

    return cache[n]

cache[0] = 0
cache[1] = 1

for i in range(50):
    print(fib_memo(i))

print(cache)

# Iterative (bottom up) solution

