def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_devisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_devisible(n), it)


if __name__ == '__main__':
    # for n in primes():
    #     if n < 1000:
    #         print(n)
    #     else:
    #         break

    # print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(L))
    print(sorted(L, reverse=True))
