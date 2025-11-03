#

# https://www.datacamp.com/blog/numpy-interview-questions


#! 59. Import Numpy and Create Array
# ^ importing Numpy Library
import numpy as np

# ^ Creating a 1D Numpy Array and Checking Dimensions
a = np.array([1, 2, 3])  # passing list to as argument to array function

print(a)

# * a.ndim returns the dimension of the array
print(a.ndim)  # 1

# * Check type
print(a.dtype)  # ~ int64
# ? or:
print(type(a))


# ^ 🧱 Creating a 2D Numpy Array and Checking Properties (Dimension, Shape, Type)


b = np.array([[1.1, 2.4, 3.3], [4.1, 5.2, 6.5]])
print(b)  # [[1.1 2.4 3.3] [4.1 5.2 6.5]]

# * b.ndim returns the number of dimensions (2 for a 2D array)
print(b.ndim)  # 2

# * b.shape returns the shape (rows, columns)
print(b.shape)  # ~ (2,3): 2 rows, 3 columns

# * b.dtype returns the data type of elements in the array
print(b.dtype)  # ~ float64

# *============================================================================================

#! 60. Array Indexing and Slicing
# ^ 🧪 Executing a Code Snippet: 2D Integer Array and Element Access

c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], "\n")
print(c, "\n")

# ? print certain element
print(c[1, 2], "\n")  # ~ means element in second row and third column

# ? Print second row starting from second element
print("Second row", c[1, :], "\n")  # ~ : = all elements after second element

# ? el row ely abl el akheir
print("Second to Last Row", c[-2, :], "\n")  # ~ : = all elements

# ? last column
print("Last column", c[:, -1], "\n")

# ?  print the second and third element in second row
print("The middle 2 elements in row 2", c[1, 1:3], "\n")

# ? set third element at the first row = 20
c[0, 2] = 20
print("After change", "\n", c)

# *============================================================================================

#! 61. Create Ones, Zeros and Identity matrix


# ^ ⚪ Creating Arrays Filled with Zeros or Ones

# ~ number elements will be created in the matrix are by default in float

# ? creates array filled with zeros -> np.zeros(rows,columns) ->
a = np.zeros((2, 3))  # pass 2,3 as tuple to zeros method
print("a", "\n", a, "\n")

# ? creates array filled with ones -> np.ones(rows,columns)
b = np.ones((2, 3))
print("b", "\n", b, "\n")

# ? creates array filled with specific number -> np.full((rows,columns),number)
c = np.full((2, 3), "Kiwilytics")
print("c", "\n", c, "\n")

# ? creates array filled with ones at the diagonal and rest is zero -> np.identity(square -> Rows = columns)
s = np.identity(3)
print("s", "\n", s, "\n")

print(a.dtype)

# ~ Create Array with Random Numbers
# ^ 🎲 Generating Random Numbers

# * np.random.rand creates array of random numbers between 0 and 1 of specific size
d = np.random.rand(2, 3)
print(d, "\n")

# * np.random.randint creates array of random numbers
# * between specified start and end integer numbers of specific size
e = np.random.randint(1, 6, size=(2, 3))  # ~ end (6) is not included
print(e)

# *===============================================================================================

#! 62. Create A Copy of an Array and Arithmatic Operations

# ^ 🧪 2 Arrays that affect one another

x1 = np.array([[1, 2, 3], [4, 5, 6]])
print(x1, "\n")

# * Any change in x2 will be applied on x1
x2 = x1
x2[0, 1] = 10
print("x1", "\n", x1, "\n\n", "x2", "\n", x2)


# ^ 🧪 2 Arrays that do not affect one another

y1 = np.array([[1, 2, 3], [4, 5, 6]])
print(y1, "\n")
# copy() creates copy of y1 so any change in y2 will not be applied on y1
y2 = y1.copy()
y2[0, 1] = 10
print("y1", "\n", y1, "\n\n", "y2", "\n", y2)


# ^ # 🧪 Arithmatic Operations on Arrays

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("arr", "\n", arr, "\n")
print("arr+2", "\n", arr + 2, "\n")
print("arr-2", "\n", arr - 2, "\n")
print("arr*2", "\n", arr * 2, "\n")
print("arr/2", "\n", arr / 2, "\n")
print("arr**2", "\n", arr**2, "\n")

# *===================================================================================

#! 63. Repeating and Stacking Arrays

# ^ Useful NumPy Functions for Data Work

# & 🧪 Extend an array with a repeat

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# * repeat(arr,number) flattening the array and repeat the array number of times
print("arr", "\n", arr, "\n")

arr1 = np.repeat(arr, 2)
print("arr1", "\n", arr1, "\n")

# * if the axis is specified no flattening will happen
arr2 = np.repeat(arr, 2, axis=0)  # ~ 0 = row
print("arr2", "\n", arr2, "\n")

arr3 = np.repeat(arr, 2, axis=1)  # ~ 1 = column
print("arr3", "\n", arr3, "\n")


# ^ 🧪 Create a bigger Array using smaller ones through stacking

a = np.array([1, 2, 3, 4])
print("a", a)
b = np.array([5, 6, 7, 8])
print("b", b)

# * np.vstack creates vertical stack of specific order ([order])
print("vertical", "\n", np.vstack([a, b, a, b]), "\n")
# * np.hstack creates horizontal stack of specific order ([order])
print("horizontal", np.hstack([b, a, b, a]))
# *===================================================================================


#! 64. Array Concatenation VS Stacking

# ^ 🧪 Create Bigger Array through concatenating smaller ones

k = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("K", k, "\n")

k1 = np.array([[9, 10, 11, 12], [13, 14, 15, 16]])
print("K1", k1, "\n")

print("Concatenate")
print(np.concatenate((k, k1), axis=0), "\n")  # 0 = row (on top)  === Vstacking
print(np.concatenate((k, k1), axis=1), "\n")  # 1 = column (Beside) === Hstacking

# ^Comparing with Stacking

print("Stacking")
print(np.vstack([k, k1]), "\n")
print(np.hstack([k, k1]), "\n")


# *===================================================================================


#! 65. Array Manipulation Reshape and Transpose
# & Array Manipulation (Generate, Reshape and Transpose Arrays)

# np.arange(start,end,number of steps) creates array , end is not included
x = np.arange(1, 11, 2)
print(x, "\n")
# np.linspace(start,end,number of samples) creates evenly spaced samples
y = np.linspace(1, 100, 11)
print(y, "\n")
arr = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print("arr", "\n", arr, "\n")
# arr.reshape(Rows,columns) changes the array size (before 7*2=14, after must equal 14)
print(arr.reshape(7, 2))

print("transposed", "\n", np.transpose(arr))

print("flattened", "\n", arr.flat[:])

# print("arr1","\n",arr1,"\n")

# np.transpose(arr1)-> row=column and column=row
# *===================================================================================

#! 66. Append and Append Array to Another

# ^ Append an Array to another array

u = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("u", "\n", u, "\n")

u1 = np.append(u, [[9, 10, 11, 12]], axis=0)  # Underneath
print("u1", "\n", u1, "\n")

u2 = np.append(u, [[5], [9]], axis=1)  #
print("u2", "\n", u2, "\n")
# *===================================================================================

#! 66. Insert and Delete from Arrays

# ^ Append an Array to another array

r = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("r", "\n", r, "\n")

r1 = np.insert(r, 2, [[11, 12, 13, 14]], axis=0)
print("r1", "\n", r1, "\n")

r2 = np.insert(r, 3, [10, 11], axis=1)
print("r2", "\n", r2, "\n")

# print(r,"\n\n",r1,"\n\n",r2,"\n\n")
r3 = np.delete(r, 1, axis=1)
print("r3", "\n", r3, "\n")
# *===================================================================================

#! 67. Create Array as Subset of Another

# * Select Subset of an Array
a = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
)
print(a)

# * Try to print only 11,12,16,17
b = a[2:4, 0:2]
print(b)
