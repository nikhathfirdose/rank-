#18 A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.ABd1234@1,a F1#,2w3E*,2We3345
import re
def passCheck():
  matched =[]
  passwords = input("Enter comma separated passwords:\n").split(",")
  for pw in passwords:
    if re.match("^[\w@#$]{6,12}$", pw):
      matched.append(pw)
      print("s")
    else:
      print("o")
  return (",".join(matched))

# print(passCheck())

#19 You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score

lst = []
while True:
    print("Do you want to enter data? type Yes/no")
    user = input()
    try:
      if user =="Yes":
        s = input("Enter Name,Age,Score: ").split(',')
      else:                         
        break
    except IndexError:
      print("Enter 3 values, Please do not skip any parameter!")
    lst.append(tuple(s))  

lst.sort(key= lambda x:(x[0],x[1],x[2]))  # here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
print(lst)