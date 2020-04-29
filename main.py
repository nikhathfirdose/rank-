#15 Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

#Suppose the following input is supplied to the program:

def getMath():
  a = input("Enter a value to compute: ")
  num = int(a)
  sums = num+(num*10+num)+(num*100+num*10+num)+(num*1000+num*100+num*10+num)
  return sums

a = input()
total,tmp = 0,str()        # initialing an integer and empty string
for i in range(4):
    tmp+=a  
    print(tmp)             # concatenating 'a' to 'tmp'
    total+=int(tmp)      # converting string type to integer type
print(total)