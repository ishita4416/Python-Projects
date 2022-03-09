import math

row = int(input())
col = int(input())

initial = []
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    initial.append(a)

#for i in range(row):
#   for j in range(row):
#       print(initial[i][j], end = " ")
#    print()

goal = []
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    goal.append(a)

summ = 0

def calc(a):
    global goal
    for i in range(row):
        for j in range(col):
            if a == goal[i][j]:
                return i,j

def euc():
    global goal
    global initial
    for i in range(row):
        for j in range(col):
            if initial[i][j] != 0:
                xg, yg = calc(initial[i][j])
                xi = i
                yi = j
                global summ 
                dist = math.sqrt(math.pow((xg-xi), 2) + math.pow((yg-yi),2))
                summ = summ + dist

    print(summ)
def manh():
    dist = 0
    global goal
    global initial 
    for i in range(row):
        for j in range(col):
            if initial[i][j] != 0:
                xg, yg = calc(initial[i][j])
                xi = i
                yi = j
                global summ
                dist = dist + abs(xg - xi) + abs(yg - yi)
               #summ = summ + dist
    print(dist)
euc()
manh()
                
        
