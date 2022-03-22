 vals in queue as (heu,parent,node)
# vals in parent as (parent,node)


def explore(graph,val,pq,parent,beta): # add child node to the queue
    if(graph[val]==None):
        return

    for heu,name in graph[val]:
        node = (heu,val,name)
        pq.append(node)
        parent.append((val,name))      # set parent of each child node
    pq.sort()                           # sort priority queue in incr order of heuristic value
    while(len(pq)>beta):
        pq.pop(beta)        # restrict the number of elements in queue by beta

def get_steps(parent,goal):    # traverse from goal to init node to get path
    node = goal
    steps = []
    while(node!=None):
        steps.insert(0,node)    # since going backward each node inserted at 0 idx
        for p in parent:
            if(p[1]==node):
                node = p[0]     # set node to the parent of node
                break
    return steps

def beam_search(graph,init,goal,beta):
    pq = [(None,None,init)]     # priority queue of max length beta
    parent=[(None,init)]        # maintain parent of each node help to get path if found
    while(pq):                  # loop till priority queue is not empty
        val = pq.pop(0)[2]      # get node with min heuristic value
        if(val == goal):        # if node is goal node break and return steps
            steps = get_steps(parent,goal)
            return steps
        else:
            explore(graph,val,pq,parent,beta)   # explore child node and add them to pq
    return None


if(__name__=='__main__'):
    graph = {
        'A' : [(1,'B'),(3,'C')],
        'B' : [(2,'D'),(2,'E')],
        'C' : [(3,'F'),(0,'G')],
        'D' : None,
        'E' : None,
        'F' : None,
        'G' : None,
    }
    init = 'A'
    goal = 'G'

    beta = 2
    steps = beam_search(graph,init,goal,beta)
    if(steps == None):
        print('\nBeam Search unsuccessful for beta:',beta)
    else:
        print('Steps:')
        print(steps)


    beta = 3
    steps = beam_search(graph,init,goal,beta)
    if(steps == None):
        print('\nBeam Search unsuccessful for beta:',beta)
    else:
        print('\nSteps for beta',beta,':')
        print(steps)
