'''
Worked On :
-------------Arrays
What is Array?
Array operations
1-Traversal
2-Deletion
3-Searching
4-Updation
5-Silicing
---------------Linked List
what is linked list?
linked list question
'''
#-------------what is array?
# A array is an collection of element in python usually list instead of array

#----------In python use array to import array
'''
import  array
import sys
# 1-"f" in floating element
arr_1=array.array("f",[1.2, 2.3, 3.4, 4.5, 5.6])
print(type(arr_1))
print("using floating f:",arr_1)
print("check byts in floating=",sys.getsizeof(arr_1),"bytes")

# 2-"d" in double floating element
arr_2=array.array("d",[1.2, 2.3, 3.4, 4.5, 5.6])
print(type(arr_2))
print("using double float d:",arr_2)
print("check bytes in double string=",sys.getsizeof(arr_2),"bytes")
# 3-"i" integer value use in array
arra_3=array.array('i',[1,2,3,4,5,6])
print(type(arra_3))
print("using integer valaue only i:",arra_3)
print("check bytes to cover in integer:",sys.getsizeof(arra_3))
'''
# ------------------Array operation
#-------traversal
'''
list_1=[1,2,3,4,5,6,7]
for value in list_1:
    print(value)
arr=[1,2,3,4,5,6]
for key,value in enumerate(arr):
    print("key is:",key,"Value is:",value)
'''
#--------insertion
'''
# this comlexity is O(1) beacuse insert at end no element shiftine
# Best Case
list_1=[1,2,3,4,5]
list_1.insert(5,6)
print(list_1)
# ------Deletion 
list_1.remove(6)
print(list_1)
# ------Searching
# Is mai hm nay 5 ko find karna hai len() function list_1 ky legth tk chala ga jb us ko 5 milla ga tho got finded chow karwa dy ga
find=5
if len(list_1)== find:
    print("Got finded")
else:
    print("Not finded")

# -------updating
for update in range(len(list_1)):
    list_1[update]+=10
print(list_1)

#------Silicing
# silicing complexity in worst case because copy all element from orginal list and show the element is silicing
print(list_1[0:3])
'''
#------------What is linked list
# linked is liner data structre element not stored in cotinous memory 
# multiple node in a single link list 
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)

# link node
node1.next=node2
node2.next=node3

# print
current=node1
while current:
    print(current.data,end="->")
    current=current.next
print("None")
'''      
#---------------To add new node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def add_node(self):
        return self.data,self.next
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

# ---To linked nodes
node1.next=node2
node2.next=node3
node3.next=node4
current=node1
while current:
    print(current.data ,end=" -> ",)
    add=current.data+1
    print("New node is",add)
    find=current.data
    current=current.next
    

        
