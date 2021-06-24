from collections import Counter


def makeAnagram(a, b):
    # Write your code here
    
    a_counter = Counter(a)
    b_counter = Counter(b)
    
    a_counter.subtract(b_counter)
    return sum(abs(value) for value in a_counter.values())

print(makeAnagram('cde','abc'))