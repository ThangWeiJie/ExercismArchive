def commands(binary_str):
    num = int(binary_str, base=2)

    actions = ["wink", "double blink", "close your eyes", "jump"]
    result = []

    mask = 1

    for i in range(0, 4):
        if num & mask == mask:
            result.append(actions[i])
        mask = mask << 1
    
    if num & mask == mask:
        result.reverse()

    return result
