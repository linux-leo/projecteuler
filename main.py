import math

print(sum(filter(lambda i: not (i % 3 and i % 5), range(1000))))

class Fibonacci:
    def fib(self):
        a, b = 0, 1
        def next_fib():
            nonlocal a, b
            a, b = b, a + b
            return a
        return next_fib

f = Fibonacci().fib()
even_sum = 0
fib_number = 0

while fib_number < 4_000_000:
    if not (fib_number := f()) % 2:
        even_sum += fib_number

print(even_sum)


def factors(n):
    wheel = [1,2,2,4,2,4,2,4,6,2,6]
    w, f, = 0, 2
    while f*f <= n:
        while n % f == 0:
            n /= f
        f, w = f + wheel[w], w+1
        if w == 11: w = 3
    return int(n)

print(factors(600851475143))

