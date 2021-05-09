import sys
import json

cnode_file = open("cal.cnode.txt", "r") #cal.cnode.txt
cnode = [list(map(float,s.split())) for s in cnode_file.readlines()]

cedge_file = open("cal.cedge.txt", "r") #cal.cedge.txt
cedge = [list(map(float,s.split())) for s in cedge_file.readlines()]

string = ""
dict = {}
for i in range(0,len(cedge)):
    if(cedge[i][1] not in dict):
        dict[cedge[i][1]] = []
    if(cedge[i][2] not in dict):
        dict[cedge[i][2]] = []
    dict[cedge[i][1]] = dict.get(cedge[i][1]) + [int(cedge[i][2]), cedge[i][3]]
    dict[cedge[i][2]] = dict.get(cedge[i][2]) + [int(cedge[i][1]), cedge[i][3]]

for i in range(0,len(cnode)):
    temp = [int(cnode[i][0]), cnode[i][1], cnode[i][2]]
    for j in range(0,len(dict.get(i))):
        temp.extend([dict.get(i)[j]])
    string += ' '.join([str(v) for v in temp]) + "\n"

f = open("ask1out.txt", "w")
f.write(string)
f.close()
