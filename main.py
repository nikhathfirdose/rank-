from itertools import product
A= [int(x) for x in input().split()]
B= [int(x) for x in input().split()]
result = list(product(A,B))
j = set(result)
for i in j:
    print(tuple(sorted(i)), end=" ")

#

from itertools import permutations
values = input().split(" ")
S = str(values[0])
k = int(values[1])
result = list(permutations(sorted(S),k))
for i in str(result):
    print("".join(i))

