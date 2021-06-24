def umbrella_count(people, umbrellas, store={}):
    if people in store: return store[people]
    if people < 0: return None
    if people == 0: return []

    shortest = None

    for umb in umbrellas:
        remainder =  people  -  umb
        result =  umbrella_count(remainder, umbrellas, store)
        if result is not None:
            combination =[*result, umb]
            store[people] = combination
            if not shortest or (len(shortest) > len(combination)):
                shortest = combination

    return shortest

def solution(people, umbrellas):
    count = umbrella_count(people, umbrellas)
    if count: return len(count);  
    else: return  -1
    
print(solution(8,[3,5]))