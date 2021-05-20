import sys
import math

def chunks(l, n):
    n = max(1, n)
    return ([l[x:x+n] for x in range(0, len(l), n)])

def dist(nodeA, nodeB):
    return math.sqrt((data[nodeB][1]-data[nodeA][1])**2 + (data[nodeB][2]-data[nodeA][2])**2)

def dijkstra(graph, src, goal):
    global counter
    nodes = []
    tmpDict = {}
    for n in graph:
        nodes.append(n[0])
        nodes += [g[0] for g in graph[n[0]][1]]

    q = set(nodes)
    nodes = list(q)
    dist = dict()
    prev = dict()
    for n in nodes:
        dist[n] = float('inf')
        prev[n] = None

    dist[src] = 0

    while q:
        counter += 1
        u = min(q, key=dist.get)
        q.remove(u)

        if u == goal:
            return tmpDict

        for v, w in graph[u][1]:
            alt = dist[u] + w
            if alt < dist[v]:
                tmpDict[u] = dist[u]
                tmpDict[v] = alt
                dist[v] = alt
                prev[v] = u
                
    return tmpDict
    
def Astar(graph, src, goal):
    print("ASTARRRR")
    return tmpDict



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
    
counter = 0
print("~~~~~~~~~~~~~")
tmpDict = dijkstra(graph,sourceNode,targetNode)

for key, value in dict(sorted(tmpDict.items(), key=lambda item: item[1])).items() :
    print("dist: " + str(value) + " to: " + str(key))
    if(key == targetNode):
        break
print("Dijkstra iterations:", counter)
print("~~~~~~~~~~~~~")


Astar(graph, sourceNode, targetNode)
