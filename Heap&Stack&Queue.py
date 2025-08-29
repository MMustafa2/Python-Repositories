'''
Worked On
Heap, Stack, Queue.

1---------------------------------------------------------Heap
What is heap?
To build heap tree is full-fill the ACBT(Alomst Completed Binary tree) Property
----two types of heap tree
1-Max Heap
2-Min heap


--Max Heap:
Parent > child 
Parent is Greater then Child
--Min Heap
parent < child
Parent is less then child

'''

import heapq
'''
# ---------------Push value in heap
# Create empty heap
heap=[]
# Insert element in heap 
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,30)


print("Min Heap:",heap)


# -----------------Smallest Element in heap

heap_1=[]
heapq.heappush(heap_1,10)
heapq.heappush(heap_1,5)
heapq.heappush(heap_1,15)
heapq.heappush(heap_1,9)
heapq.heappush(heap_1,11)
heapq.heappush(heap_1,12)
heapq.heappush(heap_1,8)

print("Print all data",heap_1)
print("Smallest Element is :",heap_1[0])

# -----------------Pop Element in heap
heap=[]
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,6)
heapq.heappush(heap,14)

pop_heap=heapq.heappop(heap)
print("Pop the element",pop_heap)
print("Heap after pop:",heap)


# ------------max value in heap
nums=[10,17,16,18,20,12,19]
max_value=[]

for num in nums:
    heapq.heappush(max_value,num)
print("Find maximum number is:", max(max_value))

#-----------min value in heap
nums=[10,17,16,18,20,12,19]
min_value=[]
for num in nums:
    heapq.heappush(min_value,num)
print("Minimum value is :",  min(min_value))

# --------- repalce value in heap 
value=[23,10,15,16,19,14,11]
heapq.heapify(value)

removed=heapq.heapreplace(value, 8)
print("Removed",removed)
print("New heap is:",value)

'''
'''
#2------------------------------------------------Stack
what is stack
Stack is the linear data structure that follow principle of LIFO
Last In,First Out
#-------Stack basic operation:
push
pop
top
'''
'''
#----------Push element on Stack
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
#----------Pop Element on stack
stack.pop()
print("Poped the top element:",stack)
#----------Top element 
# To find peak element in stack 
print("Top element :",stack[-1])


#-------------write a program to push the value in stack
class Stack:
    def __init__(self):
        self.value=[]
    def push(self,x):
        self.value.append(x)
        print(f"Pushed{x} -> Stack after push{self.value}")


#------Push value in Stack 
data=Stack()
data.push(10)
data.push(20)
data.push(23)
data.push(27)

print("Stack is :",data.value)

#-------------write a program to push the value in stack by user
class Stack:
    def __init__(self):
        self.value=[]
    def push(self,x):
        self.value.append(x)
data=Stack()

n=int(input("How many value enter in stack:"))

for num in range(n):
    push_num=int(input(f"Enter the value{num+1}: "))
    data.push(push_num)
print("Stack after push number:",data.value)
'''

#-------------write a program to Pop the value in stack by user

class Stack:
    def __init__(self):
        self.value=[]
    def push(self,x):
        self.value.append(x)
        print(f"Pushed {x} ->Pushed after stack{self.value}")
    def pop(self):
        self.value.pop()

# Push the number in stack
data=Stack()
data.push(10)
data.push(15)
data.push(17)
data.push(20)
data.push(25)
print("Stack is:",data.value)

# Pop the largest Stack
data.pop()
print("Pop after Stack:",data.value)