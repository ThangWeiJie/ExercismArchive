def egg_count(display_value):
    count = 0 
    mask = 1

    for i in range(0, 32):
        if display_value & mask == mask:
            count += 1
        
        mask = mask << 1
    
    return count
