def meanderingArray(unsorted):
    sorted_array = sorted(unsorted)
    
    a = [-1,1] * len(unsorted)
    b = a[:len(unsorted)]
    arr = list()
    res = list()
    
    for i, v in enumerate(b):
        if i == 0:
            arr.append(v)
            continue
            
        if v < 0:
            arr.append(v - (i/2))
        else:
           arr.append(i // 2)
    
    for index in arr:
        res.append(sorted_array[int(index)])
    
    return res
print(meanderingArray([5, 2, 7, 8, -2, 25, 25]))