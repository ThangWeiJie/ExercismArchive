def append(list1, list2):
    return list1 + list2


def concat(lists):
    newList = []

    for list in lists:
        newList += list

    return newList


def filter(function, list):
    newList = [x for x in list if function(x)]
    
    return newList


def length(list):
    count = 0
    for item in list:
        count += 1

    return count


def map(function, list):
    newList = [function(x) for x in list]
    return newList


def foldl(function, list, initial):
    for i in range(0, len(list)):
        initial = function(initial, list[i])

    return initial


def foldr(function, list, initial):
    for i in range(-1, -len(list) - 1, -1):
        initial = function(initial, list[i])

    return initial


def reverse(list):
    first = 0
    last = len(list) - 1

    while first < last:
        temp = list[first]
        list[first] = list[last]
        list[last] = temp

        first += 1
        last -= 1
    
    return list
