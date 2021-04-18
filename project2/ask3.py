#Sotirios Panagiotou, 4456

import sys
import json
import heapq
import math

def dist(q, point):
    dx = q[0] - point[0]
    dy = q[1] - point[1]
    distance = math.sqrt(dx**2 + dy**2)
    return distance
    
def calc_dist(point, rectangle):
    rectangle = rectangle[1]
    left = point[0] < rectangle[0]
    right = point[0] > rectangle[1]
    bottom = point[1] < rectangle[2]
    top = point[1] > rectangle[3]
    
    if top and left:
        return dist(point, [rectangle[0], rectangle[3]])
    elif left and bottom:
        return dist(point, [rectangle[0], rectangle[2]])
    elif bottom and right:
        return dist(point, [rectangle[1], rectangle[2]])
    elif right and top:
        return dist(point, [rectangle[1], rectangle[3]])
    elif left:
        return rectangle[0] - point[0]
    elif right:
        return point[0] - rectangle[1]
    elif bottom:
        return rectangle[2] - point[1]
    elif top:
        return point[1] - rectangle[3]
    else:
        return 0

def bf_nn_search(q, R):
    Q = []
    counter = 0
    for i in range(0,len(R[len(R)-1][2])):
        heapq.heappush(Q,[calc_dist(q, R[len(R)-1][2][i]), R[len(R)-1][0],R[len(R)-1][2][i]])
        
    result = []
    while(len(Q) != 0 and counter < k):
        result.append(get_next_bf_nn_search(q,Q))
        counter += 1
    return result

def get_next_bf_nn_search(q, Q):
    while(len(Q) != 0):
        e = heapq.heappop(Q)
            
        if(e[1] == 1):
            n = Rtree[e[2][0]]
                
            for i in range(0,len(n[2])):
                heapq.heappush(Q,[calc_dist(q, n[2][i]), n[0], n[2][i]])
        elif(e[1] == 0):
            o = e[2]
            heapq.heappush(Q,[calc_dist(q, e[2]), 3, o])
        elif(e[1] == 3):
            return e
    

if(len(sys.argv) <= 3 or len(sys.argv) > 4):
    print("Invalid Syntax\nPlease use: python ask1.py 'Rtree file' 'queries file'")
    exit()
else:
    try:
        Rtree_file = open(sys.argv[1], "r") #Rtree.txt
        Rtree = json.loads(Rtree_file.read())

        NNqueries_file = open(sys.argv[2], "r") #NNqueries.txt
        NNqueries_list = [s.rstrip() for s in NNqueries_file.readlines()]
        
        k = int(sys.argv[3])
    except:
        print("Could not read file/s\nPlease check the validity of your input files.")
        exit()

NNqueries = []
for i in NNqueries_list:   ## turn strings to floats, put them inside a list
    NNqueries.append([float(x) for x in i.split()])


for i in range(0,len(NNqueries)):
    resultList = bf_nn_search(NNqueries[i],Rtree)
    print(i, end=": ")
    for j in range(0,len(resultList)):
        if j < len(resultList)-1:
            print(resultList[j][2][0], end=", ")
        else:
            print(resultList[j][2][0])
