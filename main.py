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
