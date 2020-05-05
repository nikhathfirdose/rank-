#26 Define a function which can compute the sum of two numbers.

def sums(a,b):
  return a+b
#27 Define a function that can convert a integer into a string and print it in console.

def converter(a):
  return str(a)+9
conv = lambda x: str(x)

#28 Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

sums = lambda x,y: int(x)+int(y)

#29 Define a function that can accept two strings as input and concatenate them and then print it in console.

conc = lambda x,y : str(x)+str(y)

#30 Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

def maxlen(a,b):
  al,bl = len(a),len(b)
  if al>bl:
    return "a is haing max lemgth"
  elif bl>al:
    return "b is having max length"
  return "same"

print(maxlen("aaa","lol"))
