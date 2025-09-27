def primes(limit):
    if limit < 2:
        return []

    num_list = [True] * (limit + 1) # Create an array where list[i] = i+1 == True iff list[i] is prime
    num_list[0] = num_list[1] = False # 1 is not prime

    for i in range(2, int(limit ** 0.5) + 1):
        if num_list[i] == True:
            for j in range(i * i, limit + 1, i):
                num_list[j] = False
    
    primes = [i for i, prime in enumerate(num_list) if prime]
    return primes

    
    
