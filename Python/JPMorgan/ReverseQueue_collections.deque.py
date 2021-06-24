from collections import deque

def reverseQueueFirstKElements(k, Queue):
    if (len(Queue) == 0 or
             k > len(Queue)):
        return
    if (k <= 0):
        return
 
    Stack = []
 
    # put the first K elements
    # into a Stack
    for i in range(k):
        Stack.append(Queue[0])
        Queue.popleft()
 
    # Enqueue the contents of stack
    # at the front of the queue
    while (len(Stack) != 0 ):
        Queue.appendleft(Stack[0])
        Stack.pop(0)
  
# Utility Function to print the Queue
def Print(Queue):
    while len(Queue) != 0:
        print(Queue[0], end =" ")
        Queue.popleft()
 
# Driver code
if __name__ == '__main__':
    Queue = deque()
    Queue.append(10)
    Queue.append(20)
    Queue.append(30)
    Queue.append(40)
    Queue.append(50)
    Queue.append(60)
    Queue.append(70)
    Queue.append(80)
    Queue.append(90)
    Queue.append(100)
 
    k = 5
    reverseQueueFirstKElements(k, Queue)
    Print(Queue)
 
# This code is contributed by PranchalK