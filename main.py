# 8 Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
def sortwords():
  # strg = map(str,input().split(",") ) #itll map but to 1 value so returns an object
  items = [x for x in (input().split(","))]
  items.sort()
  print(",".join(items))

# sortwords()

# 9 Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
def cap():
  lst = []
  while True:
    x = input()
    if len(x)==0:
        break;
    lst.append(x.upper())
  for line in lst:
    print(line)
# cap()

# 10 Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def dupl():
  items = {x for x in input().split(" ")}
  j = sorted(items)
  print(" ". join(j))

# dupl()

