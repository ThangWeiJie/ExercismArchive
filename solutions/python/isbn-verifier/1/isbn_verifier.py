def is_valid(isbn):
    LEN_ISBN = 10
    cleaned_isbn = isbn.replace('-', '')

    if len(cleaned_isbn) != 10:
        print("Too short or too long")
        return False
    
    num_list = []
    for i in range(0, LEN_ISBN - 1):
        if not cleaned_isbn[i].isdigit():
            print("Invalid character found")
            return False
        num_list.append(cleaned_isbn[i])

    check_character = cleaned_isbn[LEN_ISBN - 1]
    if check_character.isdigit() or check_character == 'X':
       num_list.append(check_character)
    else:
        return False 

    sum = 0
    if num_list[-1] == 'X':
        sum += 10
    else:
        sum += int(num_list[-1])

    for i in range(-2, -LEN_ISBN - 1, -1):
        sum += int(num_list[i]) * (-i)

    return sum % 11 == 0
