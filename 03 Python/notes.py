#
#! 46. Create and Assign Variable
x = 5
# print("x =", x)
y = x
# y = print("y =", y)

a = 7  # if a = 7.0 , it transforms (a) from int to float
b = 5.2
c = "Any Random"
d = True

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))


#! 47. Arithmetic Operations


num1 = 4
num2 = 2

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1**num2)

#! 48. Concatenate
word1 = "Number"
x = 2
# print(word1 + " " + str(x))

# * new line
# print(word1 + "\n" + str(x))


#! 49. Wait and Input from user
# s = input("what is your name: ")
# print(s)

# ? wait: wait function is important and has applications

import time

# s = input("what is your name: ")
# time.sleep(1)
# print("Hello", s)


# ? input:

age = int(input("enter age:"))
time.sleep(1)
print("Age after two years:", age + 2)
# *====================================================================================

#! 50 Lists:

# * list -> collection of ordered and changeable elements
list1 = [1, 2, 3, 4, 5]

# * slicing [start:end:steps] returns new list from the existing list
print(list1[0])  # 1
print(list1[0:3])  # index 3 not included

print(list1[1:4:2])  # [2, 4]
print(list1[1:])  # [2, 3, 4, 5]
print(list1[:2])  # [1, 2]
print(list1[-1])  # 5  # -1 = last element
print(list1[:-1])  # [1, 2, 3, 4]

print([list1] * 2)
print(list1[0:3] * 2)  # [1, 2, 3, 1, 2, 3]


#? Multiply each item by value:
print([x*2 for x in list1])

animals = ["bird", "cat", "dog", 1, 2, 3]

print(animals)

# append() is a method that adds an element at the end of the list
animals.append("hamster")
print(animals)

# insert() is a method that adds an element at the specified position
animals.insert(2, "turtle")
print(animals)

# remove() is a method that removes the first item with the specified value
animals.remove("turtle")
print(animals)


# *====================================================================================
#! 51. Tuple


#? Definition
#* A Tuple is a collection of elements that are immutable (unchangeable).
#* Python Tuple = collection of objects separated by commas.

#? Comparison with List
#^ Similar to lists in terms of:
#*   - Indexing
#*   - Nested objects
#*   - Repetition
#~ Key difference: 
#^ Tuples are immutable, Lists are mutable.

#? Immutability
#* Once created, the value of a tuple cannot be changed.
#* If an object cannot be altered in Python, it is called immutable.
#* Tuples are immutable → their contents remain the same after creation.

#? Example Code
#* Creating and checking a tuple:
   ```python
   tuple1 = ('cat', 'dog')
   print(tuple1)
   print(type(tuple1))
# *====================================================================================

#! 52. Dictionary

#* dictionary are used to store data values in key:value pairs

dict = {"name": "Ahmed",
        "age": "20",
        "job": "Engineer"}

print(dict)

print(dict["age"])

print(dict.keys())

print(dict.values())

print(dict.items())

#*======================================================================================

#! 53: if condition

#* if condition:
#*   do something
#* else: the condition is false
#*   do something

x = 5
y = 2

if x+y > 20:
    print(x+y," > 20")
else:
    print(x+y,"<20")
#*======================================================================================
#! else if
#& Conditional Statements and List Membership in Python

# elif = else if -> to check another condition

grade = 55
if grade >= 70:
    print("A")
elif grade < 70 and grade >= 60:
    print("B")
elif grade < 60 and grade >= 50:
    print("C")
else:
    print("F")


#? Example: Conditional with Boolean vs Integer
#^ Code

x = True
if x != 1:  # != checks if not equal
    print("true")
else:
    print("false")

#^ Output
#* false
#* Explanation: In Python, True == 1 → so condition (x != 1) is False → else branch runs.

#? Example: Check if Element Exists in a List
#^ Code

fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list.")

if "orange" not in fruits:
    print("Orange is not in the list.")

#^ Output
#* Apple is in the list.
#* Orange is not in the list.


x = False  # False = 0, True = 1
if x == 0:
    print("true")
else:
    print("false")


#*======================================================================================

#! for loop:

#* for loop is used for iterating over a sequence like list

numbers = ["one","two","three"]
print(numbers)
for x in numbers:
    print(x)

numbers= [1,2,3,4,5,6]
for x in numbers:
    print(x+10)

#? loop over string
for x in "hello":
    print(x)
    

#? loop over range:
# range(start,end,steps) function returns a sequence of numbers
# end is not included in the sequence

for i in range(4):
    print(i)
    
for i in range(1,5):
    print(i)
    
for i in range(1,10,2):
    print(i)
    
    
#? nested for loop:
x1 =[1,2]
x2=[1,2,3,4,5]

for i in x1:
    for j in x2:
        print(i*j)

#*==========================================================================================

#! while loop:

#* while loop -> execute a set of statements as long as condition is true (i<5)

i =0 
while i < 5:
    print(i)
    i+=1
    
#? draw pyramid
x = 4
i = 1
while i <= x:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print("")
    i += 1
    
#^ better method:

x = 5
i = 1
while( i <= x):
    print(i*"*")

#? break:

#* break used to Terminates the loop even if the while condition is true
x = 10
while x >= 1:
   
    if x == 6:
        print("Terminates the loop")
        break
    print(x)
     x-=1
     
    #? continue:
    
# continue used to skip only the current iteration then continue in while loop
i = 10
while i > 1:
    i -= 1
    if i == 6:
        print("Skip this iteration")
        continue
    print(i)

    
#*=============================================================================================

#! function:

def sum(x,y):
    sum = x+y
    print(sum)
    
sum(3,5)
    
    
#^=========


def createList(num):
    list=[]
    for i in range(5):
        list.append(i)
    print(list)
    
createList(5)


#*================================

#! coding exercise:

nums = list(map(int, input().split()))

def sum_list(nums):
    sum=0
    for i in nums:
        sum+=i
    print(sum)

sum_list(nums)