#  printing state as below,block tuple
from copy import deepcopy as dc


class pair:
    def __init__(self, below, block):
        self.below = below
        self.block = block


def state_level_map(state):  # return the map of level vs list of block at that level (used to cal heuristic value)
    level_map = {-1: [None], 0: [], 1: [], 2: [], 3: []}
    for i in range(len(state)):
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
    for i in range(1, len(state)):
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

    top = ['A', 'B', 'C']
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


def move(init, goal):  # generate all possible moves and return one with best heuristic value
    state = dc(init)
    max_heu = heuristic(init, goal)
    ret_state = init
    top = get_top_blocks(state)
    # n^2 move n = len(top)
    for i in range(len(top)):
        for j in range(len(top)):  # place the ith block on top of jth block
            if (i == j):  # place ith block on ground
                update(state, pair(None, top[i]))
                h_val = heuristic(state, goal)
                if (h_val >= max_heu):
                    max_heu = h_val
                    ret_state = dc(state)
                state = dc(init)
            else:
                update(state, pair(top[j], top[i]))
                h_val = heuristic(state, goal)
                if (h_val >= max_heu):
                    max_heu = h_val
                    ret_state = dc(state)
                state = dc(init)
    if (ret_state == init):
        return None  # return None to show failue of Steepest Hill Climb
    return ret_state


def print_state(state):  # print state as tuple
    for p in state:
        print((p.below, p.block), end=', ')
    print()


def solve(init, goal):  # solve block world problem using the steepest hill climb and given heuristic
    steps = 0
    state = dc(init)
    goal_heu = heuristic(goal, goal)
    while (state != None):
        print_state(state)
        if (heuristic(state, goal) == goal_heu):
            print('Steepest Hill Climb Successfull')
            print('Steps taken:', steps)
            return
        else:
            state = move(state, goal)
        steps += 1
    print('Steepest Hill Climb Unsuccessfull!')
    return


if (__name__ == '__main__'):
    init = [pair(None, 'C'), pair('C', 'A'), pair(None, 'B')]
    goal = [pair(None, 'A'), pair('A', 'B'), pair('B', 'C')]
    solve(init, goal)
