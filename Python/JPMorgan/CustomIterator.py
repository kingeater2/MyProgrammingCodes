class CustomIterator:
				
    # constructor
    def __init__(self, limit):
        self.limit = limit
    
    # creates iterator object
    # called when iteration is initialised
    def __iter__(self):
        self.x = 10
        return self # this means that the __iter__ method returns a reference to the instance object
    
    # To move to next element
    def __next__(self):
        
        # store current value of x
        x = self.x
        
        # stop iteration when limit reached
        if x > self.limit:
            raise StopIteration
        
        # else increment and return old value
        self.x += 1	
        return x
					
for i in CustomIterator(15):
    print(i)


for i in CustomIterator(5):
    print(i)