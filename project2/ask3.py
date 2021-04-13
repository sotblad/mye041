import sys
import json
import heapq
import math

def dist(q, point):
    if(point == 0 or q == 0):
        return float('inf')
        
    center = [(point[1][0]+point[1][1])/2, (point[1][2]+point[1][3])/2]
    
    dx = q[0] - center[0]
    dy = q[1] - center[1]
    distance = math.sqrt(dx**2 + dy**2)
    return distance

def bf_nn(q, node, k):
    queue = []
    Onn = 0

    for i in range(0,len(node[2])):
        heapq.heappush(queue,[dist(q, node[2][i]), node[0],node[2][i]])
        
    top = queue[0]
    found = []

    while(len(queue) != 0):  #and dist(q,top[2]) < dist(q, Onn)):
        queue = sorted(queue)
        queue.reverse()
        e = heapq.heappop(queue)
            
        if(e[1] == 1):
            n = Rtree[e[2][0]]
            for i in range(0,len(n[2])):
                if(dist(q,n[2][i]) < dist(q, Onn)):
                    heapq.heappush(queue,[dist(q, n[2][i]), n[0], n[2][i]])

        elif(e[1] == 0):
            o = e[2]
            if(e not in found):
                found.append(e)
                
            if(dist(q,o) < dist(q, Onn)):
                Onn = o

    return sorted(found)[0:k]
    

if(len(sys.argv) <= 3 or len(sys.argv) > 4):
    print("Invalid Syntax\nPlease use: python ask1.py 'Rtree file' 'queries file'")
    exit()
else:
    try:
        Rtree_file = open(sys.argv[1], "r") #coords.txt
        Rtree = json.loads(Rtree_file.read())

        NNqueries_file = open(sys.argv[2], "r") #offsets.txt
        NNqueries_list = [s.rstrip() for s in NNqueries_file.readlines()]
        
        k = int(sys.argv[3])
    except:
        print("Could not read file/s\nPlease check the validity of your input files.")
        exit()

NNqueries = []
for i in NNqueries_list:   ## turn strings to floats, put them inside a list
    NNqueries.append([float(x) for x in i.split()])

qoueue = []

for i in range(0,len(NNqueries)):
    qoueue = bf_nn(NNqueries[i], Rtree[527], k)
    print(i, end=": ")
    for j in range(0,len(qoueue)):
        if j < len(qoueue)-1:
            print(qoueue[j][2][0], end=", ")
        else:
            print(qoueue[j][2][0])
