def twoStrings(s1, s2):
    # Write your code here
    s1_set = set()
    s2_set = set()
    for i in s1:
        s1_set.update(i)
    for i in s2:
        s2_set.update(i)

    if s1_set.intersection(s2_set) != set():
        return 'YES'
    else:
        return 'NO'


print(twoStrings('hi', 'world'))