


iterable_value = 'Geeks'
iterable_obj = iter(iterable_value)

while True:
    try:
        item = next(iterable_obj)
        print(item)
    
    except StopIteration:
        break
    
"""_________________________________________________________________________________________________________________________"""

iterable_value = 'Geeks'
for i in iterable_value:
    print(i)
