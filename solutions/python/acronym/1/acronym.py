def abbreviate(words):
    word_list = words.replace('-', ' ').split()
    
    for index, word in enumerate(word_list):
        for i in range(0, len(word)):
            if not word[i].isalpha():
                temp = word.replace(word[i], '')
                word_list[index] = temp    
    
    capital_list = [word[0].capitalize() for word in word_list]

    return ''.join(capital_list)
