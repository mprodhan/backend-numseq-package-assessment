def primes(n):
    """Returns a list of primes not including n"""
    numbers = set(range(n, 1, -1))
    primes_list = []
    while numbers:
        p = numbers.pop()
        primes_list.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes_list

def is_prime(m):
    """Returns True or False if m is prime or not"""
    if type(m) != int:
        raise TypeError("m-value must be an integer")
    n = 2
    if m < n:
        return False
    else:
        while n < m:
            if m % n == 0:
                return False
                break
            n += 1
        else:
            return True

