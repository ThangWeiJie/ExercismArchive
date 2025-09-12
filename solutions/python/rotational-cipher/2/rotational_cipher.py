def rotate(text, key):
    UPPERCASE_START = 65
    LOWERCASE_START = 97
    ans = ""

    for char in text:
        i = ord(char)

        if char.isupper():
            i -= UPPERCASE_START
            char = chr(((i + key) % 26) + UPPERCASE_START)
        elif char.islower():
            i -= LOWERCASE_START
            char = chr(((i + key) % 26) + LOWERCASE_START)

        ans += char

    return ans
