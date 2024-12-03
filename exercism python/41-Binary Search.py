def find(search_list, value):
    arr = sorted(search_list)
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == value:
            return middle
        elif arr[middle] > value:
            end = middle - 1
        else:
            start = middle + 1
    raise ValueError("value not in array")