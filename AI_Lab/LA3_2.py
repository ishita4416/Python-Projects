import heapq
import copy
# taking the number of rows and columns as input from user
row = int(input())
col = int(input())

# taking the initial state as input from user
InitState = []
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    InitState.append(a)
# taking the goal state as input from the user
GoalState = []
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    GoalState.append(a)


# returns the indices for the position of misplaced tiles
def position_ij(child):
    for i in child:
        if 0 in i:
            ipos = child.index(i)

    if 0 in child[ipos]:
        jpos = child[ipos].index(0)

    return ipos, jpos


def MoveLeft(InitState, ipos, jpos):
    # used deepcopy to make a copy of the initial state such that it does not affect the original initial state
    t1 = copy.deepcopy(InitState)
    # taking the tile and that to its left and flipping them
    t1[ipos][jpos], t1[ipos][jpos - 1] = t1[ipos][jpos - 1], t1[ipos][jpos]
    return t1


def MoveRight(InitState, ipos, jpos):
    t1 = copy.deepcopy(InitState)
    # taking the tile and the one to its right and flipping them
    t1[ipos][jpos], t1[ipos][jpos + 1] = t1[ipos][jpos + 1], t1[ipos][jpos]
    return t1


def MoveTop(InitState, ipos, jpos):
    t1 = copy.deepcopy(InitState)
    # taking the tile and the one below and flipping them
    t1[ipos][jpos], t1[ipos - 1][jpos] = t1[ipos - 1][jpos], t1[ipos][jpos]
    return t1


def MoveBottom(InitState, ipos, jpos):
    t1 = copy.deepcopy(InitState)
    # taking the tile and the one above and flipping them
    t1[ipos][jpos], t1[ipos + 1][jpos] = t1[ipos + 1][jpos], t1[ipos][jpos]
    return t1


# check to see if the state achieved is equal to goal state
def compare(NewState, GoalState):
    for i in range(0, 3):
        for j in range(0, 3):
            if NewState[i][j] != GoalState[i][j]:
                return False
    return True

# function to display the states traversed
def display(temp):
    for i in range(0, 3):
        for j in range(0, 3):
            print(temp[i][j], end=" ")
        print()
    print()


# function to calculate the number of misplaced tiles at each step state
def MisPlacedTiles(NewState):
    c = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if NewState[i][j] != 0 and NewState[i][j] != GoalState[i][j]:
                c += 1
    return c


print("Initial State:")
display(InitState)
print("Goal State:")
display(GoalState)
print()

print("Starting Search:\n")
child_nodes = []
# Misplaced tiles from the initial state are pushed into the existing heap child nodes
# in such a way that the min heap property is maintained
heapq.heappush(child_nodes, (MisPlacedTiles(InitState), InitState))
visited = []
k = 0
# while there are misplaced tiles in the heap, the process is carried out
while child_nodes:
    k += 1
    # every misplaced node is visited
    front = heapq.heappop(child_nodes)
    visited.append(front[1])
    if compare(front[1], GoalState):
        display(front[1])
        print("Found Goal State")
        break
    ipos, jpos = position_ij(front[1])
    # for the first row and then similarly every other row, the position of 0 determines where it is shifted to
    # if the new tile hasn't been visited, it is added to the heap
    if ipos == 0:
        temp = MoveBottom(front[1], ipos, jpos)
        if temp not in visited:
            heapq.heappush(child_nodes, (MisPlacedTiles(temp), temp))
        if jpos == 0:
            temp2 = MoveRight(front[1], ipos, jpos)
            if temp2 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp2), temp2))
        elif jpos == 1:
            temp2 = MoveLeft(front[1], ipos, jpos)
            if temp2 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp2), temp2))
            temp3 = MoveRight(front[1], ipos, jpos)
            if temp3 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp3), temp3))
        else:
            temp2 = MoveLeft(front[1], ipos, jpos)
            if temp2 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp2), temp2))

    elif ipos == 1:
        temp = MoveTop(front[1], ipos, jpos)
        if temp not in visited:
            heapq.heappush(child_nodes, (MisPlacedTiles(temp), temp))
        if jpos == 0:
            temp2 = MoveBottom(front[1], ipos, jpos)
            if temp2 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp2), temp2))
            temp3 = MoveRight(front[1], ipos, jpos)
            if temp3 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp3), temp3))
        elif jpos == 1:
            temp2 = MoveLeft(front[1], ipos, jpos)
            if temp2 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp2), temp2))
            temp3 = MoveRight(front[1], ipos, jpos)
            if temp3 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp3), temp3))
            temp4 = MoveBottom(front[1], ipos, jpos)
            if temp4 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp4), temp4))
        else:
            temp2 = MoveLeft(front[1], ipos, jpos)
            if temp2 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp2), temp2))
            temp3 = MoveBottom(front[1], ipos, jpos)
            if temp3 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp3), temp3))

    elif ipos == 2:
        temp = MoveTop(front[1], ipos, jpos)
        if temp not in visited:
            heapq.heappush(child_nodes, (MisPlacedTiles(temp), temp))
        if jpos == 0:
            temp2 = MoveRight(front[1], ipos, jpos)
            if temp2 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp2), temp2))
        elif jpos == 1:
            temp2 = MoveLeft(front[1], ipos, jpos)
            if temp2 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp2), temp2))
            temp3 = MoveRight(front[1], ipos, jpos)
            if temp3 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp3), temp3))
        else:
            temp2 = MoveLeft(front[1], ipos, jpos)
            if temp2 not in visited:
                heapq.heappush(child_nodes, (MisPlacedTiles(temp2), temp2))
    display(front[1])
print("Total number of steps taken to solve:", k - 1)
