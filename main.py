# jacker rank solve 
sets = set()
noOfInputs = int(input())
for i in range(noOfInputs):
    value = input()
    sets.add(value)
    count = len(sets)
print(count)
#22 Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

# Suppose the following input is supplied to the program:

def countSort():
  sentence = input("Enter your sentence: ")
  words = sentence.split()
  sortList={}
  for word in words:
    if word in sortList:
      sortList[word]+=1
    else:
      sortList[word] =1
  for key in sortList:
    result = key+ ":"  +str(sortList[key])
    print(result)

(countSort()) 
#23 Write a method which can calculate square value of number


def sqrVal():
  number = int(input("Enter number: "))
  return "sqr is "+ str(number**2)

print(sqrVal())

#24 python built in functions
print(str.__doc__)
print(sorted.__doc__)

def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p

print(pow(3,2))
print(pow.__doc__) 

#25 Define a class, which have a class parameter and have a same instance parameter.

class Person:
  def __init__(self,f,l):
    self.f = f
    self.l =l
  def intro(self):
    print("hello " + self.f + self.l)

p1 = Person("john", "stamos")
p1.intro()
class Car:
    def __init__(self,name = None):
        self.name = name

honda=Car("Honda")
print("name is {0}".format(honda.name))

toyota=Car()
toyota.name="Toyota"
print("name is %s"%(toyota.name))

