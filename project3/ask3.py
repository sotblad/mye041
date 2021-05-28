import sys
import math

def chunks(l, n):
    n = max(1, n)
    return ([l[x:x+n] for x in range(0, len(l), n)])

def calcDist(nodeA, nodeB):
    return math.sqrt((cnode[nodeB][1]-cnode[nodeA][1])**2 + (cnode[nodeB][2]-cnode[nodeA][2])**2)

def gamma(gammaList):
    maximum = -1
    maxIndex = 0
    for i in range(0,len(gammaList)):
        if(gammaList[i] > maximum):
            maximum = gammaList[i]
            maxIndex = i

    return [maximum,i]

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

if(len(sys.argv) <= 2):
    print("Invalid Syntax\nPlease use: python ask3.py node1 node2 ..")
    exit()
else:
    nList = list(map(int, sys.argv[1:len(sys.argv)]))
    print(nList)



ntikt = dict()
finished = 0
nodis = []
nodist = []
curr = 6

for i in nList:
    nodis.append([i])
    nodist.append(0)

print(nodist)
print(dijkstra(graph,6,1)[2])

while(finished != 1):
    gama = gamma(nodist)
    print("GAMMA", gama)
    for i in range(0,len(nodis)):
        mina = 9999999999999999
        minIndex = -1

        for j in chunks(diction[nodis[i][len(nodis[i])-1]],2):
            if(j[0] in nodis[i]):
                continue
            DIK = dijkstra(graph,nodis[i][0],j[1])
            if(DIK[2] < mina):
                mina = DIK[2]
                minIndex = j[0]
        existsCount = 0
        for j in nodis:
            if(minIndex in j):
                existsCount += 1
        if(existsCount == len(nodis)-1):
            finished = 1



        nodis[i].append(minIndex)
        ntikt[nodis[i][len(nodis[i])-1]] = minIndex
        nodist[i] += mina

    #    print("DIJKSTRA", dijkstra(graph,nodis[i][0],nodis[i][len(nodis[i])-1])[2])
    print(nodist)
    print(nodis)
