def find_divisors(number):
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            yield i
            if i != number // i:
                yield number // i

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    divisors = find_divisors(number)

    sum = 0
    for n in divisors:
        sum += n
    sum -= number
    
    if sum == number:
        return "perfect"
    elif sum < number:
        return "deficient"
    else:
        return "abundant"
