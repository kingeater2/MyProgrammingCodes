from collections import Counter

def checkMagazine(magazine, note):
    mag_counter = Counter(magazine)
    note_counter = Counter(note)
    diff = note_counter - mag_counter
    if diff == {}:
        print('Yes')
    else:
        print('No')


checkMagazine(['two', 'times', 'three', 'is', 'not', 'four'],['two', 'times', 'two', 'is', 'four'])