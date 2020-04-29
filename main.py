 #13Write a program that accepts a sentence and calculate the number of letters and digits.

#Suppose the following input is supplied to the program:

def numCal():
  countD = 0
  countL = 0 
  sentence = input("Enter your sentence: ")
  for letter in sentence:
    if letter.isdigit():
      countD+=1
    elif letter.isalpha():
      countL+=1
  result =  f"Letters: {countL} \nDigits: {countD}"
  return result 
     

print(numCal()) 
#author
word = input()
letter,digit = 0,0

for i in word:
    letter+=i.isalpha()         # returns True if alphabet
    digit+=i.isnumeric()        # returns True if numeric

print("LETTERS %d\nDIGITS %d"%(letter,digit))