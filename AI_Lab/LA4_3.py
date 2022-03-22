#  printing state as below,block tuple
from copy import deepcopy as dc


class pair:
    def __init__(self, below, block):
        self.below = below
        self.block = block


def state_level_map(state):  # return the map of level vs list of block at that level (used to cal heuristic value)
    level_map = {-1: [None], 0: [], 1: [], 2: [], 3: []}
    for i in range(4):
        if (len(level_map[i - 1]) == 0):
            break
        for p in state:
            if p.below in level_map[i - 1]:
                level_map[i].append(p.block)
    return level_map


def get_below(state, block):  # in given state return the block below the specified block
    if (block == None):
        return None
    for p in state:
        if (p.block == block):
            return p.below


def heuristic(state,
              goal):  # calculate the heuristic value as +n : if block at correct pos with all below at correct and -n otherwise
    # n = no of block below

    state_level = state_level_map(state)
    goal_level = state_level_map(goal)
    val = 0
    for i in range(1, len(state)):  # iterate through 1 to n-1 (0 level doesn't affect val)
        if (len(state_level[i]) > 0 and len(goal_level[i]) > 0):
            for block in state_level[i]:
                if block in goal_level[i]:
                    bi = block
                    bg = bi
                    add = True
                    for k in range(i, 0, -1):
                        bi = get_below(state, bi)
                        bg = get_below(goal, bg)
                        if (bi != bg):
                            val -= i
                            add = False
                            break
                    if (add):
                        val += i
                else:
                    val -= i
        elif (len(state_level[i]) != 0):
            val -= i
        else:
            return val
    return val


def get_top_blocks(state):  # get block on top which can only move
    top = ['A', 'B', 'C', 'D']
    for pair in state:
        if pair.below in top:
            top.remove(pair.below)
    return top


def update(state, entry):  # add entry state to state array and remove prev state
    for p in state:
        if (p.block == entry.block):
            state.remove(p)
            state.append(entry)
            return


def move(init, goal):  # generate new moves and return one with better heuristic value
    state = dc(init)
    heu = heuristic(init, goal)
    top = get_top_blocks(state)
    # n^2 move n = len(top)
    for i in range(len(top)):
        for j in range(len(top)):  # place the ith block on top of jth block
            if (i == j):  # place ith block on ground
                update(state, pair(None, top[i]))
                if (heuristic(state, goal) > heu):
                    return state
                state = dc(init)
            else:
                update(state, pair(top[j], top[i]))
                if (heuristic(state, goal) > heu):
                    return state
                state = dc(init)
    return None  # return none to specify no better state found


def print_state(state):  # print state as tuple
    for p in state:
        print((p.below, p.block), end=', ')
    print()


def solve(init, goal):  # solve block world problem using the simple hill climb and given heuristic
    steps = 0
    state = dc(init)
    goal_heu = heuristic(goal, goal)
    while (state != None):
        print_state(state)
        if (heuristic(state, goal) == goal_heu):
            print('Hill Climb Successfull')
            print('Steps taken:', steps)
            return
        else:
            state = move(state, goal)
        steps += 1
    print('Hill Climb Unsuccessfull!')
    return


if (__name__ == '__main__'):
    init = [pair(None, 'B'), pair('B', 'C'), pair('C', 'D'), pair('D', 'A')]
    goal = [pair(None, 'A'), pair('A', 'B'), pair('B', 'C'), pair('C', 'D')]
    solve(init, goal)
