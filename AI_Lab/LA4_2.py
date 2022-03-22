#  printing state as below,block tuple
from copy import deepcopy as dc


class pair:
    def __init__(self, below, block):
        self.below = below
        self.block = block


def heuristic(state, goal):
    val = 0  # heuristic value to return at end
    for ps in state:  # loop through all pairs in state
        for pg in goal:  # loop through all pair in goal state
            if (ps.block == pg.block):
                if (ps.below == pg.below):  # if block on correct block +1 val
                    val += 1
                else:
                    val -= 1  # else -1 val
                break
    return val


def get_top_blocks(state):  # return name of block which can be moved
    top = ['A', 'B', 'C', 'D']
    for pair in state:
        if pair.below in top:
            top.remove(pair.below)
    return top


def update(state, entry):  # add new pos of block specified by entry and remove previous position
    for p in state:
        if (p.block == entry.block):
            state.remove(p)
            state.append(entry)
            return


def move(init, goal):  # produce steps and return one with more heuristic value the init state
    state = dc(init)
    heu = heuristic(init, goal)
    top = get_top_blocks(state)
    # n^2 moves n = len(top)
    for i in range(len(top)):
        for j in range(len(top)):
            if (i == j):  # place ith block on ground
                update(state, pair(None, top[i]))
                if (heuristic(state, goal) > heu):
                    return state
                state = dc(init)
            else:  # place the ith block on top of jth block
                update(state, pair(top[j], top[i]))
                if (heuristic(state, goal) > heu):
                    return state
                state = dc(init)
    return None  # if no better state found return none to show failure of simple hill climb


def print_state(state):  # print state array as list of tuple rather than user defined class pair
    for p in state:
        print((p.below, p.block), end=', ')
    print()


def solve(init, goal):  # try solving blocks world problem using simple hill climb 
    steps = 0
    state = dc(init)
    while (state != None):
        print_state(state)
        if (heuristic(state, goal) == len(state)):
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
