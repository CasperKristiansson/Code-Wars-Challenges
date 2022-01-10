def fib(n, c={0: 1, 1: 1}):
    def re_fib(n, c={0: 1, 1: 1}):
        if n in c:
            return c[n]
        else:
            c[n] = re_fib(n-1) + re_fib(n-2)
            return c[n]
    
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    if n not in c:
        x = n // 2
        c[n] = fib(x-1) * fib(n-x-1) + fib(x) * fib(n - x)
    return c[n]


print(fib(1))
