import math

#   taking the number of rows and columns as input from user
row = int(input())
col = int(input())

#   taking the initial state as a matrix input
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

#   taking the goal state as a matrix input
goal = []
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    goal.append(a)

summ = 0

#   searching for every element from the initial state one by one in the goal state and returning its coordinates to the calling function
def calc(a):
    global goal
    for i in range(row):
        for j in range(col):
            if a == goal[i][j]:
                return i,j

#   Function to find the Euclidean distance
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
    print("The Euclidean distance is: ", summ)

#   Function to find the Manhattan distance
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
    print("The Manhattan distance is: ", dist)
  
#   Function to find the Minkowski distance
def minkowski():
    dist = 0
    order = int(input())
    global goal
    global initial
    for i in range(row):
        for j in range(col):
            if initial[i][j] != 0:
                xg, yg = calc(initial[i][j])
                xi = i
                yi = j
                dist = dist + pow(abs((yg - yi)**order) + abs((xg - xi)**order), 1/order)
    print("The Minkowski distance is: ", dist)

    
euc()
manh()
minkowski()             
        
