def sieve(n: int) -> list[int]:
    if n < 2:
        return []

    num_list = [True] * (n + 1) # Create an array where list[i] = i+1 == True iff list[i] is prime
    num_list[0] = num_list[1] = False # 1 is not prime

    for i in range(2, int(n ** 0.5) + 1):
        if num_list[i] == True:
            for j in range(i * i, n + 1, i):
                num_list[j] = False
    
    primes = [i for i, prime in enumerate(num_list) if prime]
    return primes

def prime(number):
    if number <= 0:
        raise ValueError('there is no zeroth prime')

    prime_list = sieve(1000000)
    return prime_list[number - 1]
