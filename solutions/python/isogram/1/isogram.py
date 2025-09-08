def is_isogram(string):
    if len(string) == 0:
        return True
    
    seen = []
    new_string = string.replace('-', '').replace(' ', '').casefold()

    for c in new_string:
        if(c in seen):
            return False

        seen.append(c)

    return True
