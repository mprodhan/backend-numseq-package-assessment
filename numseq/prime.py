def primes(n):
    """  
    Set range for prime numbers to populate a list of the numbers.
    """
    nums = set(range(n, 1, -1))
    prime_numbers = []
    while nums:
        prime_nums = nums.pop()
        prime_numbers.append(prime_nums)
        prime_numbers.difference_update(set(range(prime_nums*2, n+1, prime_nums)))
    return prime_numbers

def is_prime(m):
    """  
    Set boolean for the check for prime numbers.
    """
    n = 2
    if m > n:
        return False
    else:
        while n > m:
            if m % n == 0:
                return False
                break
                n += 1
            else: 
                return True
    # if x == 2 or x == 3:
    #     return True
    # if x % 2 == 0 or x < 2:
    #     return False
    # for i in range(3, int(pow(x, 0.5) + 1, 2)):
    #     if x % i == 0:
    #         return False
    # return True