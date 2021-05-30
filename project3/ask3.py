import sys

def chunks(l, n):
    n = max(1, n)
    return ([l[x:x+n] for x in range(0, len(l), n)])

def dijkstra(graph, src, goal=-1):
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

        if goal != -1 and u == goal:
            return [prev, counter, distance]

        for v, w in graph[u][1]:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                
    return [prev, counter, {k: v for k, v in sorted(dist.items(), key=lambda item: item[1])}]

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
    print("Invalid Syntax\nPlease use: python ask2.py node1 node2 node3...")
    exit()
else:
    nList = list(map(int, sys.argv[1:len(sys.argv)]))

tmpList = []

for i in nList:
    tmpList.append(dijkstra(graph,i))

resultDict = {}
for i in range(0,len(graph)):
    lst = [i, []]
    for j in range(0,len(nList)):
        lst[1].append(tmpList[j][2][i])
    resultDict[lst[0]] = max(lst[1])

bestMeetingPoint = min(resultDict, key=resultDict.get)

print("best meeting point:", bestMeetingPoint)
print("Shortest path distance =", resultDict[bestMeetingPoint])
print("paths:")

for i in nList:
    S = []
    u = bestMeetingPoint
    path = dijkstra(graph, i, bestMeetingPoint)
    while(path[0][u] is not None):
        S.append(u)
        u = path[0][u]
    S.append(i)
    print([path[2], list(reversed(S))])
