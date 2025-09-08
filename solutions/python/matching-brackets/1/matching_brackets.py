def is_paired(input_string):
    stack = []

    for c in input_string:
        if(c in {'(', '{', '['}):
            stack.append(c)
        elif(c in {')', '}', ']'}):
            if(len(stack) == 0):
                return False
            
            top = stack[-1]
            if(top == '(' and not c == ')' or top == '{' and not c == '}' or top == '[' and not c == ']'):
                return False

            stack.pop()
    
    return len(stack) == 0

