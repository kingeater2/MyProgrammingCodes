# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            

a = simpleGeneratorFun()
print(a)
"""
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)
"""