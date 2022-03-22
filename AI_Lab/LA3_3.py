import copy


# finds the position of the blank tile
def findBlank(state):
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == 0:
                return i, j


# function to check if the Goal state has been achieved by comparing it with Initial state
# heuristic taken to be the number of misplaced tiles
def check(state, goal):
    if state == goal:
        return 0
    else:
        dist = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] != 0 and state[i][j] != goal[i][j]:
                    dist += 1
        return dist


def moveLeft(state, z):
    state[z[0]][z[1]], state[z[0]][z[1] - 1] = state[z[0]][z[1] - 1], state[z[0]][z[1]]
    return state


def moveRight(state, z):
    state[z[0]][z[1]], state[z[0]][z[1] + 1] = state[z[0]][z[1] + 1], state[z[0]][z[1]]
    return state


def moveUp(state, z):
    state[z[0]][z[1]], state[z[0] - 1][z[1]] = state[z[0] - 1][z[1]], state[z[0]][z[1]]
    return state


def moveDown(state, z):
    state[z[0]][z[1]], state[z[0] + 1][z[1]] = state[z[0] + 1][z[1]], state[z[0]][z[1]]
    return state

# used to display the intermediate states till Initial state and goal state are same
def display(temp):
    for i in range(0, 3):
        for j in range(0, 3):
            print(temp[i][j], end=" ")
        print()
    print()


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

print('Initial State:')
display(InitState)
print('Goal State:')
display(GoalState)

q = []
# appending to the copy of the Initial state the heuristic, if Initial state is not equal to the goal state
q.append((copy.deepcopy(InitState), check(InitState, GoalState)))
k = 0

while q[0][0] != GoalState:
    z = findBlank(q[0][0])
    t = up = down = right = left = 1000
    # at every intermediary step, we first deep copy the previous intermediary step
    # and then move it according to the heuristic till the intermediary step becomes equal to the goal state
    if z[0] > 0:
        up = check(moveUp(copy.deepcopy(q[0][0]), findBlank(q[0][0])), GoalState)
    if z[1] > 0:
        left = check(moveLeft(copy.deepcopy(q[0][0]), findBlank(q[0][0])), GoalState)
    if z[0] < 2:
        down = check(moveDown(copy.deepcopy(q[0][0]), findBlank(q[0][0])), GoalState)
    if z[1] < 2:
        right = check(moveRight(copy.deepcopy(q[0][0]), findBlank(q[0][0])), GoalState)
    t = min(up, right, left, down)
    # if the misplaced tile is greater than the minimum of the up,down,left,right variables 
    # and is equal to any one of them, move it in the direction indicated, pop it from the q
    # and add on to the number of steps taken as intermediary step increases
    if q[0][1] > t == up:
        q.append((moveUp(copy.deepcopy(q[0][0]), z), t))
        q.pop(0)
        display(q[0][0])
        k += 1
    elif q[0][1] > t == left:
        q.append((moveLeft(copy.deepcopy(q[0][0]), z), t))
        q.pop(0)
        display(q[0][0])
        k += 1
    elif q[0][1] > t == down:
        q.append((moveDown(copy.deepcopy(q[0][0]), z), t))
        q.pop(0)
        display(q[0][0])
        k += 1
    elif q[0][1] > t == right:
        q.append((moveRight(copy.deepcopy(q[0][0]), z), t))
        q.pop(0)
        display(q[0][0])
        k += 1
    if q[0][0] == GoalState:
        print('Found Goal State :')
print("Total number of steps taken to solve:", k)
