# A-0, S-1, G-3, C-4, B- 2
# A- S,G; S-A,B,C; B- S,G; G-A,B,C; C-S,G
graph = [
    [1, 3],
    [0, 2, 4],
    [1, 3],
    [0, 2, 4],
    [1, 3]
]
# cost representing the weight of each edge
cost = {
    (0, 1): 1,
    (1, 0): 1,
    (0, 3): 10,
    (3, 0): 10,
    (1, 4): 15,
    (4, 1): 15,
    (3, 4): 5,
    (4, 3): 5,
    (2, 3): 5,
    (3, 2): 5,
    (1, 2): 5,
    (2, 1): 5,
}


# function for Uniform Cost Search- similar to Dijkstra Algorithm but with initial and goal node
# a visited queue is maintained to keep check on all the nodes already traversed considering they have
# the minimum cost between them
# all paths from initial to goal state are traversed using a tree and minimum one is selected
def ucs(goal, start):
    answer = []
    queue = []
    for i in range(len(goal)):
        answer.append(10 ** 2)
    queue.append([0, start])
    visited = {}
    count = 0
    while len(queue) > 0:
        queue = sorted(queue)
        p = queue[-1]
        del queue[-1]
        p[0] *= -1
        if p[1] in goal:
            index = goal.index(p[1])
            if answer[index] == 10 ** 2:
                count += 1
            if answer[index] > p[0]:  # max ans
                answer[index] = p[0]
            del queue[-1]
            queue = sorted(queue)
            if count == len(goal):
                return answer
        if p[1] not in visited:  # update path cost
            for i in range(len(graph[p[1]])):
                queue.append([(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])
        visited[p[1]] = 1
    return answer


goal = []
goal.append(3)
answer = ucs(goal, 0)
print("Min cost from A to G is = ", answer[0])
