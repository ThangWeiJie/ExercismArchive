def is_pangram(sentence):
    alphset = set()
    
    for c in sentence.casefold().replace(' ', ''):
        if c.isalpha():
            alphset.add(c)
    
    return len(alphset) == 26