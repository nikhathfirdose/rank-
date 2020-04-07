#fibbonaci

def fib(num):
  f = 0
  s = 1
  res =[]
  for i in range(num):
    res.append(f)
    temp=f
    f =s
    s = temp+s
  return res






print(fib(21))