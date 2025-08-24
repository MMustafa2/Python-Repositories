
#                                   --------------Set---------------
# -----Set is t he collection of unique numbers
'''
set_1={1,2,3,4,4,5}
print(set_1)
# To add number 
set_1.add(6)
print(set_1)
# To remove number
set_1.remove(6)
print(set_1)
#---------to find difference in two sets/ difference means return the element that are in first set but did not present in second set
a={1,2,3,4,5}
b={1,3,5,4,7}
print(a.difference(b))
print(a.symmetric_difference(b)) 

#-----------------Create two sets of numbers {1,2,3,4,5} and {4,5,6,7,8}.
#-----Find their union.
#------Find their intersection.
# ------Find their difference (set1 - set2).
set_1={1,2,3,4,5}
set_2={4,5,6,7,8}
print("Union is:",set_1.union(set_2))
print("Intersection is:",set_1.intersection(set_2))
print("difference is:",set_1.difference(set_2))

#-----------------Given a set {10,20,30}, add the number 40 to it.
data={10,20,30}
data.add(40)
print(data)
if 10 in data:
    print("yes")


#----------------Find common elements in three sets:
set_1 = {1, 2, 3, 4}
set_2 = {2, 3, 5, 6}
set_3 = {1, 2, 3, 7}
diff=(set_1.difference(set_2))
total_diff=diff.difference(set_3)
print(total_diff)
 
#----------------Remove multiple items {"banana", "mango"} from this set:
fruits = {"apple", "banana", "cherry", "mango", "grapes"}
fruits.difference_update({"apple","banana"})
print(fruits)


# Find elements that appear in only one of the two sets:
#--------------to find uniques element in  both sets
set_1 = {100, 200, 300}
set_2 = {200, 400, 500}
find_element=set_1.symmetric_difference(set_2)
print(find_element)


#--------------Convert two lists into sets and find common values
list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7]
set_1=set(list_1)
set_2=set(list_2)
common_value=set_1 & set_2
print(common_value)
print(type(common_value))

#-------------------Check if the following two sets are disjoint (no common elements):
set_1 = {1, 2, 3}
set_2 = {4, 5, 6}
disjoint=set_1.isdisjoint(set_2)
print(disjoint)
'''

#                         ------------------dictionary-------------------
# ---Dicitionary are used to store key and value pairs of data
'''
data={
    "name":"Mustafa",
    "Gender":"Male",
    "age":23,
    "blood_group":"AB+"
}
print(data["age"],data["blood_group"])
data["name"]="Muhammad Mustafa"
print(data)

# Nested-Dicitionary
students={
    "name":["mustafa","ali","haider"],
    "degree":{
        "mustafa":"BSCS",
        "ali":"BSIT",
        "haider":"BSSE",
    },
    "age":[23,22,21]
}
# to return all keys
print("Use key method:",students.keys())
# to return all values in key
print("use value method:",students.values())
# to return all items present in dictionary
print("Use item method:",students.items())
#  to get the values in key
print("Use get method:",students.get("age"))

update_stu=students.copy()
print(update_stu)
'''
#-------------Create a dictionary of 3 students with their marks. Print only the keys (student names).

'''
students={
    "Musa":98,
    "Ali":100,
    "Arslan":67,
}
print(students.keys())
#-------------Print all the values (marks) from the dictionary.
print(students.values())
# Write a program to check if a key exists in a dictionary.
key_check="Ali"
if key_check in students:
    print("Yes present")
else:
    print("Not present")
#-------Use .get() to safely fetch a value for a key
print("Number of arslan is:",students.get("Arslan"),)
print(update_stu)
'''
# -----You have a dictionary:
# -----Increase the price of "banana" by 10.
# -----Add a new fruit "orange": 40.
'''
fruits = {"apple": 50, "banana": 20, "mango": 100}
print("Before Increse:",fruits.values())
fruits["banana"]=30
print("After Increase:",fruits.values())
print("Before add fruits:",fruits )
fruits["orange"]=120
print("Add fruit orange",fruits)
'''
#------------Remove "apple" using .pop().
'''
fruits = {"apple": 50, "banana": 20, "mango": 100}
fruits.pop('apple')
print("After pop",fruits)
'''
#------------Remove the last inserted item using
'''
fruits = {"apple": 50, "banana": 20, "mango": 100}
print("Pop Last item:",fruits.popitem())
'''
#-----to add value by default in dict key
''' 
key=["a","b","c"]
new_dict=dict.fromkeys(key,0)
print(new_dict)
'''
# Merge these two dictionaries:
'''
dict_1={
     "a":1,
     "b":2,
     "c":3
     }
dict_2={
    "d":4,
    "e":5,
    "f":6
    }
print("Merge two dictionary",dict_1 | dict_2)
'''
#-----------------Write a program to find the student with highest marks in this dictionary:

# marks={
#     "ali":100,
#     "musa":200,
#     "harry":250,
#     "akram":80
# }
# topper=max(marks)
# least=min(marks)
# print("Class topper is",topper)
# print("Lowest number is :",least)


#                               -------------Exception handling--------------
#--------Exception ka matlab hai eroor ana kay bd bhi program smoothly run kara
'''
a=10
b=0
c=10/0
print(c)
print("This data is important")
print("This data is very important")
print("This data is very very important")
print("This data is  most important")
'''
# in this result to produce (ZeroDivisionError)

# --------solve by Exception handling
#-------built in error 
'''
try:
    a=10
    b=0
    c=10/0
except ZeroDivisionError as z:
    print("This is the error", z)
else:
    print(c)
finally:
    print("This data is important")
    print("This data is very important")
    print("This data is very very important")
    print("This data is  most important")

'''
# ----------user define error

class VotingEroor(Exception):
    pass

age=int(input("Enter the age of the voter="))
nationality=input("Enter the Nationality=")
try:
    if age<=18 or nationality !="pakistani":
        raise VotingEroor()
except VotingEroor as v:
    print("You are not eligible for Vote")
    print("Thanks for Using Voting-Machine")
else:
    print("You are eligible for vote")
    print("Age of voter is:",age)
    print("Nationality of voter is",nationality)
finally:
    print("-----------INFORMATION----------")
    print("Total five provinces in pakistan")
    print("Capital of pakistan is Islamabad")
    print("Pakistan is tha agricultural country")
    print("Quaid-e-Azam is the First Governer of pakistan")