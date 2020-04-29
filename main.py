#14 Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

#Suppose the following input is supplied to the program:

def calcCases():
  upper,lower =0,0
  sentence = input("Enter your sentence: ")
  for letter in sentence:
      upper+=letter.isupper()
      lower+=letter.islower()
  result = f"Upper: {upper} \nLower: {lower}"
  return result

print(calcCases())

#author

# for i in word:
#         lower+=i.islower()
#         upper+=i.isupper()
