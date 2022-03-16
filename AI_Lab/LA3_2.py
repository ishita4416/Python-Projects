import heapq
import copy

InitState = [
    [2, 0, 3],
    [1, 8, 4],
    [7, 6, 5]
]
GoalState = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

def position_ij(child):
    for i in child:
        if 0 in i:
            ipos = child.index(i)
    
    if 0 in child[ipos]:
        jpos = child[ipos].index(0)

    return ipos, jpos

def MoveLeft(InitState, ipos, jpos):
    t1 = copy.deepcopy(InitState)
    t1[ipos][jpos], t1[ipos][jpos-1] = t1[ipos][jpos-1], t1[ipos][jpos]
    return t1

def MoveRight(InitState, ipos, jpos):
    t1 = copy.deepcopy(InitState)
    t1[ipos][jpos], t1[ipos][jpos+1] = t1[ipos][jpos+1], t1[ipos][jpos]
    return t1

def MoveTop(InitState, ipos, jpos):
    t1 = copy.deepcopy(InitState)
    t1[ipos][jpos], t1[ipos-1][jpos] = t1[ipos-1][jpos], t1[ipos][jpos]
    return t1

def MoveBottom(InitState, ipos, jpos):
    t1 = copy.deepcopy(InitState)
    t1[ipos][jpos], t1[ipos+1][jpos] = t1[ipos+1][jpos], t1[ipos][jpos] 
    return t1

def compare(NewState, GoalState):
    for i in range(0, 3):
        for j in range(0, 3):
            if NewState[i][j] != GoalState[i][j]:
                return False
    return True

def display(temp):
    for i in range(0, 3):
        for j in range(0, 3):
            print(temp[i][j], end=" ")
        print()
    print()

def find(i, j, key):
    if GoalState[i][j] == key:
        return i, j
    else:
        for i in GoalState:
            if key in i:
                ipos = GoalState.index(i)
        if key in GoalState[ipos]:
            jpos = GoalState[ipos].index(key)
        return ipos, jpos

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
heapq.heappush(child_nodes, (MisPlacedTiles(InitState), InitState))
visited = []
k = 0
while child_nodes:
   k += 1
   front = heapq.heappop(child_nodes)
   visited.append(front[1])
   if compare(front[1], GoalState):
       display(front[1])
       print("Found Goal State")
       break
   ipos, jpos = position_ij(front[1])
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
print("Total number of steps taken to solve:", k-1)
