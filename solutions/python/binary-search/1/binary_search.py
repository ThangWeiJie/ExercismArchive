def find(search_list, value):
    left = 0
    right = len(search_list) - 1

    while(left <= right):
        mid = (left + right) // 2

        if search_list[mid] == value:
            return mid
        elif value < search_list[mid]:
            right = mid - 1
        else:
            left = mid + 1

    raise ValueError("value not in array")

        
