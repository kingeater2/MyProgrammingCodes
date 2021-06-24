def divide(A: int, B: int) -> int:
        if A == 0: return 0
        MAX = 2147483647
        MIN = -2147483648
        if A == MIN and B == -1:
            return MAX
        minus = A * B  < 0
        A,B = abs(A), abs(B)
        
        def f(n):
            return A - n * B
        
        lo = 0
        hi = MAX
        
        while lo <= hi:
            m = lo + (hi - lo) //2
            
            c = f(m)
            if c == 0:
                return -m if minus else m
            
            if c > 0:
                lo = m + 1
            else:
                hi = m - 1
        
        if lo == MAX:
            return MIN if minus else MAX
        
        if f(lo) < 0:
            lo -= 1
        
        return -lo if minus else lo
    
print(divide(10,3))