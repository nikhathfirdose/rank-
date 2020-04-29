#17Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100


def deposit():
  netAmt, netWithdraw = 0,0
  while True:
    s = input("want to enter? type yes/no ")
    if s == "no":
      break
    elif s == "yes":
      yes = input("Enter D for deposit and W to withdraw ")
      details = yes.split(" ")
      if details[0] == "D":
           netAmt+=int(details[1])
      elif details[0] == "W":
          netWithdraw+=int(details[1])
      else:
          pass

        
          
  result = netAmt - netWithdraw
  return result

print(deposit())


  

