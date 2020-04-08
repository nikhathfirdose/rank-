#4 Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

n = str(input())
li = n.split(",")
print(list(li))
print(tuple(li))

#5 Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use init method to construct some parameters

class define:
  def __init__(self):
    pass
  def get(self):
    self.s = str(input())
  def prin(self):
    print(self.s.upper())

obj = define()
obj.get()
obj.prin()

#6 Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:
import math
def calculate():
  c=50
  h=30
  value=[]
  items = [x for x in input().split(",")]
  for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
  print(",".join(value)) #works on str so append(str/|\)

calculate()

#7 Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i * j.

# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

# Then, the output of the program should be:

# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
  
# def matri():
#   ival =[]
#   jval=[]
#   X = int(input("X="))
#   Y = int(input("Y="))
#   for i in range(X):
#     ival.append(i)
#   for j in range(Y):
#     jval.append(j)
#   for 

  
# matri()
