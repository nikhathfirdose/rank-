#20 Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class Divisible:
    def by_seven(self, n):
        for number in range(0,n + 1):
            if number % 7 == 0: yield number


divisible = Divisible()
generar = divisible.by_seven(49)
for number in generar:
    print(number)

#21A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
import  math

x,y = 0,0
while True:
    s = input("enter ").split()
    if not s:
        break
    if s[0]=='UP':                  # s[0] indicates command
        y+=int(s[1])                # s[1] indicates unit of move
    if s[0]=='DOWN':
        y-=int(s[1])
    if s[0]=='LEFT':
        x-=int(s[1])
    if s[0]=='RIGHT':
        x+=int(s[1])
                                    # N**P means N^P
dist = round(math.sqrt(x**2 + y**2))  # euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
print(dist)