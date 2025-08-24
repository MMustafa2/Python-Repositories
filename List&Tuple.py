#                         ------------for loop-------------
'''
pointers=[(1,2,3),(3,4,5),(5,6,7),(7,8,9)]
for x,y,z in pointers:
    print(f"{x=},{y=},{z=}")
    print("Add in x+y+z=",x+y+z)


table=int(input("Enter the value="))
for value in range(1,11):
    print(table,"*",value,"=",table*value)

for number in range(1,11):
    if number%2==0:
        print("Even Number is:",number)

for i in range(1,6):
    print("* "*i)
'''

#                          ------------Type Casting-------------
# to convert the data from one  type to another type are type casting
'''
number_1=10
number_2=20.0
new_num=number_1+number_2
print("Convert in",type(new_num))
print(new_num)

a=23
b='20'
c=int(b)
print(a+c)
print(type(a+c))

name="Musatafa"
print(name+" Naseer!")

'''

#                           ----------------Function----------
#-----------without parameter,or without return
'''
def sum():
    a=25
    b=25
    print(a+b)
sum()
# --------with parameter without return
def subtract(a,b):
    print(a-b)
subtract(10,20)
# --------with parameter and with return
def multiply(a,b):
    c=a*b
    return c
print(multiply(2,10))


number=int(input("Enter the number:"))
def calc_week():
    if(number == 1):
        print('Today is Monday')
    elif(number==2):
        print('Today is Tuesday')
    elif(number == 3):
        print('Today is Wednesday')
    elif(number ==4):
        print('Today is Thursdat')
    elif(number==5):
        print("Today is Friday")
    elif(number==6):
        print("Today is Sarturday")
    else:
        print("Today Is SUnday")
        print("Happy Holiday!")
calc_week()


balance=int(input("Enter the balance amount:"))
Credit=int(input("Enter the Credit amount:"))
def  calc_credit():
    total=balance-Credit
    if total<=1000:
        print("Total Balance is less then 1000 rupess")
        print("U dont withdraw the amount")
        print("Thank you for using services")
    else:
        print("Total Amount:",total)
        print("Thank you for using services")
        return total
calc_credit()
'''
#                                     ------------------List-------------
'''
list_1=[1,2,3,4,5,6,7,8,9,10]
print(list_1)
print(type(list_1))

list1=[1,2,3,4,5]
list2=['musa','harry','ali']
print(type(list1+list2))


list_1=[1,2,3,4,5]
print(len(list_1))
#  append the name
 list_1.append("mustafa")
 print(list_1)
# index in list to check 
list_1.index(6)
print(list_1)

data=[1,5,2,4,3,6]
# To set in reverse order
data.sort()
print(data)
# to remove the element from last
data.pop()
print(data)

list_1=[1,2,3,4,5,6]
if 6 in list_1:
    print("Yes")
else:
    print("No")

if len(list_1)==6:
    print("length is right")
else:
    print("Wrong")


# Create a list of 5 numbers and print the first and last element.
list_1=[1,3,4,5,6]
print("First number is:",list_1[0])
print("Last number is:",list_1[4])

# nsert a number at the 2nd position of a list.
list_1.insert(1,2)
print(list_1)

# Remove an element from a list using .remove().
list_1.remove(6)
print(list_1)

# Print all elements of a list using a for loop.
for value in list_1:
    print(value)

# Reverse a list using .reverse().
list_1.reverse()
print(list_1)

# Count how many times a value occurs in a list.
new_list=[1,2,3,2,2,4,5]
number_count=new_list.count(2)
print(number_count)

# Write a program to find the maximum and minimum number in a list.
list_1=[1,2,3,4,5,6]
max_num=max(list_1)
min_num=min(list_1)
print("Number is maximum:",max_num)
print("Number is minimum:",min_num)

# Remove duplicates from a list.
data=[1,2,3,4,5,3]
unique=list(set(data))
print(unique)

# Find the second largest number in a list.
list_1=[12,34,56,78,54]
list_1.sort()
print(list_1)
Second_largest_num=list_1[-2]
print("Second largest number:",Second_largest_num)

# Merge two lists into one 
data1=[1,2,3,4,5,6]
data2=[7,8,9,10]
# data1.insert(6,data2)
# print(data1)
if len(data1)==6:
    print(data1+data2)

# often use set() to:
# Remove duplicates from a list
# Find common elements between lists
list_1=[1,2,3,4,5,6]
list_2=[7,2,3,1,8]
common= list(set(list_1) & set(list_2))
print("Common data is",common)


'''
#                           ------------------Tupple--------------
'''
tupple_1=(1,2,3,4,5,6)
print(tupple_1)
print(tupple_1[0])
# Difference between list and tupple list is mutable tupple in immutable or data cannot bs changed
list_1=[1,2,3,4]
print(list_1)
list_1[0]="Mustafa"
print(list_1)
tupple_1.index(6)
print(tupple_1)

# Create a tuple of 5 numbers and print the first and last element.
number=(1,2,3,4,5,6)
print("First element is:",number[0])
print("Last element is:",number[5])

# Create a tuple with different data types (int, string, float) and print all elements.
diff_tuple=(23,"Mustafa",23.6)
print(diff_tuple)
# Write a program to access the 3rd element of a tuple.
number=(1,2,3,4,5,6)
print("Third element is",number[2])
# Write a program to print each element of a tuple using a for loop.
for value in number:
    print(value)

# Write a program to find how many times a value appears in a tuple
number=(1,2,3,4,5,6,2,)
num_appear=number.count(2)
print("2 is appear in times:",num_appear)

# Write a program to find the index of a value in a tuple
fruits=("apple","bnanan","malta","cherry")
check_index=fruits.index("cherry")
print("Cherry present in index:",check_index)
# Concatenate two tuples into one.
tuple1=(1,2,3,4,5)
tuple2=(6,7,8)
result=tuple1+tuple2
print("Join  two tuple",result)

# lice a tuple to get elements from index
print(tuple1[2:6])

# Sort a tuple of numbers
number=(1,2,6,3,5,0,4)
print("Before sorting of tuple:",number)
give_list=list(number)
give_list.sort()
print("After sorting of tuple",tuple(give_list))
print(type(tuple(give_list)))
'''