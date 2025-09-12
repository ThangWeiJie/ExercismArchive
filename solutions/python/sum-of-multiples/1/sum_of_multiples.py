def sum_of_multiples(limit, multiples):
    combined_sets = set()
    result = 0
    
    for num in multiples:
        if num != 0:
            multiplier = num
            while num < limit:
                combined_sets.add(num)
                num += multiplier

    for num in combined_sets:
        result += num

    return result
