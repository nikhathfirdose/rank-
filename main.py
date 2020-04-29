#12Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

def evenNum():
  for i in range(1000,3001):
    if i%2==0:
      if (int(i/10))%2==0:
        if (int(i/100))%2 ==0:
          if (int(i/1000))%2==0:
            print(i, end=",")
def check(element):
    return all(ord(i)%2 == 0 for i in element)  # all returns True if all digits i is even in element

lst = [str(i) for i in range(1000,3001)]        # creates list of all given numbers with string data type
lst = list(filter(check,lst))                   # filter removes element from list if check condition fails
print(lst)
print(",".join(lst))