def minimumSwaps(arr):
    swaps = 0
    arr_dict = {v : i for i, v in enumerate(arr)}
    
    for i in range(len(arr)):
        index_to_swap = arr_dict[i+1]
        
        if index_to_swap != i:   
            arr_dict[arr[i]] = index_to_swap
                                
            arr_dict[i+1] = i
            
            arr[i], arr[index_to_swap] = arr[index_to_swap], arr[i]
            
            swaps += 1
    return swaps

print(minimumSwaps([4,3,1,2]))