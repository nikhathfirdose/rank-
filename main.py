#Day 1
# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
for i in range(2000,3201):
  if i%7==0:
    if i%5!=0:
      print(i, end=",")
#2 Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
def fact(n):
  if n==1:
    return 1
  else:
    return fact(n-1)*n
print("\n")
print(fact(8))
print("\n")

#3 With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
def integral(num):
  result = {}
  for i in range(1, num+1):
    result[i] = i*i
  return result
print(integral(8))
print("\n")
#or
n = int(input())
a={i: i*i for i in range(1,n+1)}
print(a)
