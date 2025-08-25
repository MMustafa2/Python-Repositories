""" 
Worked on:  
basic syntax in python
variables
data types
"""

#code
#1---------------BASIC SYNTAX OF PYTHON------------------
'''
print("Hello world")
name="Mustafa"
print(f'my name is {name}')
print("my name is",name)
print("hello","world")
'''
# 2 -------------Variables------------------  
'''
# variable are memory location used to store data 
name="Mustafa"
# name is variable used to store string data 
id=1234
print("id is:",id,"name is :",name)
weight="60kg"
print("My weight is:",weight)
print(name,id,weight)

'''

# 3------------------data types-------------
# data types in python means to clearify the  type of the data which stored
# different types of data types in python 
# 1- Integer data type
# 2- Float  data type
# 3- string data type
# 4- bolean data type
# 5- Complex dat type

# 1- Integer data type
'''
#Integer data type in python used to store integeer value only
a=24
b=34
print("Data type is:",type(a+b),"Addition is:",a+b)
number=int(input("Enter the number:"))
print(type(number),"Number is:",number)
'''
# 2- Float data type
'''
# float data type in python used to store data in point 
number=float(input("Input Enter the number:"))
print("type is:",type(number),"Number is",number)
# calculate the radius
diameter=4.5
value_of_pi=3.14
print("Radius is:",(2*value_of_pi)*diameter)
print(type((2*value_of_pi)*diameter))
'''

# 3-String data type
# string data-type used to store combination of alphabet
'''

print("Welcome to Pakistan")
print(type("Welcome to Pakistan"))
# Concatination
print("Hello"+"World")
print("101",2)
name="Mustafa"
print("Check the length of string:",len(name))
print("prestent in this index:",name.index('Mus'))
print("To print only 3 alphabet:",name[0:3])
print("Ends with:",name.endswith('a'))
print("Start with:",name.startswith('M'))
print("Split the part:",name.split('us'))

'''
#4-complex data type
'''
number=3j
print(number)
print(type(number))
number1=1+3j
print(number1)
print(type(number1))
name=""""Mustafa"""
print(type(name))
'''

# 5-bolean data types
'''
print(type(True))
print(type(False))
name="mustafa"
print(type(name.endswith('f')))   #name is integer data type but print the the type in bolean true.false
a=10
b=20
print("a,b wequal hai:",a is b)
print("a,b equal nai hai:",a is not b)
'''

#------Condiitional statement-------------
# if,if elif ,else 
'''
#----------------if
age=19
if(age>=18):
    print("U are eligible")


# ---------------if-else
#---------Is mai agar ek bhi condition false hu jy gy tho user vote kay lya eligible nai hu ga 
v_age=int(input("Enter the voter age:"))
nationality=str(input("Enter the Nationality:"))
if(v_age>=18 and nationality=="pakistani"):
    print("You are Eligible for voting")
else:
    print("U are not eligible for vote")



#--------to build a calculator by using if,if-elif,else 
user=input("Use the calculator to Enter yes/No:")
if(user =="yes"):
    print("-----welcome to calculator-------")
    number_1=int(input("Enter the number_1:"))
    number_2=int(input("Enter the number_2:"))
    operation=input("Enter the operation to perform number:")
    if(operation == "+"):
        print("Answer is:",number_1+number_2)
    elif(operation=="-"):
        print("Answer is:",number_1-number_2)
    elif(operation=="*"):
        print("Answer is:",number_1*number_2)
    elif(operation=="%"):
        print("Division is:",number_1 % number_2)
else:
    print("----EROOR 4004----")
'''



#---------------Loops--------------
# In python define to types of loop 
# 1----------while loop
# 2----------for loop
'''
#Question2-)to print natural number
number=1
while number<=10:
    print("Natural number is:",number)
    number=number+1

# Question1-)to print the table user enter the value
table=int(input("Enter the table to print:"))
number=1
while number<=10:
    print(table,"*",number,"=",table*number)
    number=number+1


number=5
factorial=1
while number>=1:
     factorial*=number
     number=number-1
print(factorial)


# -------------Break and continue is while loop
number=10
while number>=1:
    print(number)
    if(number==3):
       break
    number=number-1
print("break is apply")

number=4
while number<=10:
    print(number)
    if number%2==0:
       break
    number=number+1
print("break is:",number)
  

  
# -----Continue
#----to skip the task in iteration 
number=6
while number>0:
    number=number-1
    if(number ==3):
        continue
    print(number)
print("loop is ended")

number=1
table=2
while number<=10:
    number=number+1
    if(number*table==4):
        continue
    print(table*number)
print("Loop is continue after 2,4")
'''
