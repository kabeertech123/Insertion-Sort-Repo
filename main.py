def InsertionSort():
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 
    n = len(arr)
    
    for index in range(1, n):
        current = arr[index]
        index2 = index
        while index2 > 0 and arr[index2 - 1] > current:
            arr[index2] = arr[index2 - 1]
            index2 = index2 - 1 
        arr[index2] = current
    
    print(arr)
InsertionSort()