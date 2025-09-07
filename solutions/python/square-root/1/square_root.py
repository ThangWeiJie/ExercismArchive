def square_root(number):
    i = 1
    j = number

    while(i != j):
        m = int((i + j) / 2)
        
        if((m * m) == number):
            return m
        elif((m * m) > number):
            j = m - 1
        else:
            i = m + 1

    return i
