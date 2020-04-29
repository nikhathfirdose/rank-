#16Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. Suppose the following input is supplied to the program:

def sqrs():
  result = [int(s)*int(s) for s in input("Enter Numbers: ").split(',') if int(s)%2!=0 ]
  return result
print(sqrs())


