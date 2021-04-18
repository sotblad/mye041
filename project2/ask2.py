#Sotirios Panagiotou, 4456

import sys
import json

def search(node,query):
    success = []
    for j in range(0,len(node[2])):
        intersection = [max(query[0], node[2][j][1][0]), max(node[2][j][1][2],query[1]), min(query[2], node[2][j][1][1]), min(query[3],node[2][j][1][3])]
        if(intersection[0] <= intersection[2] and intersection[1] <= intersection[3]):
            if(node[0] == 0):
                success.append(str(node[2][j][0]))
            else:
                test = search(Rtree[node[2][j][0]],intersection)
                if(len(test) != 0):
                    for i in test:
                        success.append(i)
    return success

if(len(sys.argv) <= 2 or len(sys.argv) > 3):
    print("Invalid Syntax\nPlease use: python ask1.py 'Rtree file' 'queries file'")
    exit()
else:
    try:
        Rtree_file = open(sys.argv[1], "r") #Rtree.txt
        Rtree = json.loads(Rtree_file.read())

        queries_file = open(sys.argv[2], "r") #Rqueries.txt
        queries_list = [s.rstrip() for s in queries_file.readlines()]
    except:
        print("Could not read file/s\nPlease check the validity of your input files.")
        exit()

queries = []
for i in queries_list:   ## turn strings to floats, put them inside a list
    queries.append([float(x) for x in i.split()])

for i in range(0,len(queries)):
    result = search(Rtree[527], queries[i])
    print(str(i) + " ("+str(len(result))+"): " + ', '.join(result) + ' ')
