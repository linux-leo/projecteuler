print(sum(filter(lambda i: not (i % 3 and i % 5), range(1000))))


def sum_even_fibs_loop(limit):
    sum_even = 0
    i, j = 1, 1
    while j < limit:
        sum_even += i*(1-(i % 2))
        i, j = i + j, i
    return sum_even


print(sum_even_fibs_loop(4000000))
