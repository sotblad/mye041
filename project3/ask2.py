import sys
import math

def chunks(l, n):
    n = max(1, n)
    return ([l[x:x+n] for x in range(0, len(l), n)])

def calcDist(nodeA, nodeB):
    return math.sqrt((cnode[nodeB][1]-cnode[nodeA][1])**2 + (cnode[nodeB][2]-cnode[nodeA][2])**2)

def dijkstra(graph, src, goal):
    counter = 0
    distance = 0
    prev = dict() 
    nodes = []
    for n in graph:
        nodes.append(n[0])
        nodes += [g[0] for g in graph[n[0]][1]]

    q = set(nodes)
    nodes = list(q)
    dist = dict()
    
    for n in nodes:
        dist[n] = float('inf')
        prev[n] = None

    dist[src] = 0

    while q:
        counter += 1
        u = min(q, key=dist.get)
        q.remove(u)

        distance = dist[u]

        if u == goal:
            return [prev, counter, distance]

        for v, w in graph[u][1]:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                
    return [prev, counter, distance]
    
def Astar(graph, src, goal):
    counter = 0
    distance = 0
    prev = dict() 
    nodes = []
    for n in graph:
        nodes.append(n[0])
        nodes += [g[0] for g in graph[n[0]][1]]

    q = set(nodes)
    nodes = list(q)
    dist = dict()
    distnc = dict()
    
    for n in nodes:
        dist[n] = float('inf')
        distnc[n] = float('inf')
        prev[n] = None

    dist[src] = 0
    distnc[src] = 0

    while q:
        counter += 1
        u = min(q, key=dist.get)
        q.remove(u)

        distance = distnc[u]

        if u == goal:
            return [prev, counter, distance]

        for v, w in graph[u][1]:
            alt = dist[u] + w + calcDist(v,goal) - calcDist(u,goal)
            if alt < dist[v]:
                distnc[v] = distnc[u] + w
                dist[v] = alt
                prev[v] = u
                
    return [prev, counter, distance]

cnode_file = open("cal.cnode.txt", "r") #cal.cnode.txt
cnode = [list(map(float,s.split())) for s in cnode_file.readlines()]

cedge_file = open("cal.cedge.txt", "r") #cal.cedge.txt
cedge = [list(map(float,s.split())) for s in cedge_file.readlines()]

string = ""
diction = {}
for i in range(0,len(cedge)):
    if(cedge[i][1] not in diction):
        diction[cedge[i][1]] = []
    if(cedge[i][2] not in diction):
        diction[cedge[i][2]] = []
    diction[cedge[i][1]] = diction.get(cedge[i][1]) + [int(cedge[i][2]), cedge[i][3]]
    diction[cedge[i][2]] = diction.get(cedge[i][2]) + [int(cedge[i][1]), cedge[i][3]]
    
graph = []
for i in range(0,len(diction)):
    tempList = diction.get(i)
    splitList = chunks(tempList,2)
    inList = [i]
    pointsList = []
    for j in range(0,len(splitList)):
        pointsList.append([int(splitList[j][0]), splitList[j][1]])
    inList.append(pointsList)
    graph.append(inList)

if(len(sys.argv) <= 2 or len(sys.argv) > 3):
    print("Invalid Syntax\nPlease use: python ask2.py 'source node id' 'target node id'")
    exit()
else:
    sourceNode = int(sys.argv[1])
    targetNode = int(sys.argv[2])
 
## Dijkstra
S = []
u = targetNode  

print("Dijkstra:")
path = dijkstra(graph,sourceNode,targetNode)
while(path[0][u] is not None):
    S.append(u)
    u = path[0][u]
S.append(sourceNode)
print("Shortest path length =", len(S))
print("Shortest path distance =", path[2])
print("Shortest path =" , list(reversed(S)))
print("number of visited nodes =", path[1], "\n")

## A Star
S = []
u = targetNode

print("Astar:")
path = Astar(graph, sourceNode, targetNode)
while(path[0][u] is not None):
    S.append(u)
    u = path[0][u]
S.append(sourceNode)
print("Shortest path length =", len(S))
print("Shortest path distance =", path[2])
print("Shortest path =" , list(reversed(S)))
print("number of visited nodes =", path[1])
