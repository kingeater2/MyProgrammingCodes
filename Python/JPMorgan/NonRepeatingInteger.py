
def non_repeating(arr):
    non_repeating = []
                           
    for n in arr:
        if n in non_repeating:
            non_repeating.pop(non_repeating.index(n))
        else:
            non_repeating.append(n)
    index = arr.index(non_repeating[0])
    #non_repeating[0] if non_repeating else None
    return index


print(non_repeating([1, 1, 1, 5, 2, 1, 3, 4, 2]))