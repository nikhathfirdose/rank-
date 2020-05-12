#31Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

def sqrdict():
  d = dict()
  for num in range(1,21):
    d[num]= num**2
  return d

print(sqrdict())

#32 Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

def keyOnly():
  m = dict()
  j = list()
  for num in range(1,21):
    m[num] = num**2
  for k in m.keys():
    j.append(k)

  return j

print(keyOnly())

#33 Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

def sqrlist():
  l = [x**2 for x in range(1,21)]
  return l
print(sqrlist())

#34 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

def sqrlist2():
  l = [x**2 for x in range(1,21)]
  return l[:5]

print(sqrlist2())

#35 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

def sqrlist3():
  l = [x**2 for x in range(1,21)]
  return l[-5:]

print(sqrlist3())

#36 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

def sqrlist4():
  l = [x**2 for x in range(1,21)]
  return l[5:]
print(sqrlist4())

#37 Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

def sqrTup():
   l = [x**2 for x in range(1,21)]
   return tuple(l)
    
print(sqrTup())

####commit exercism day 3
## commit accneture 2600
