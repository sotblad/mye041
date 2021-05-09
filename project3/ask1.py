import sys
import json

cnode_file = open("cal.cnode.txt", "r") #cal.cnode.txt
cnode = [list(map(float,s.split())) for s in cnode_file.readlines()]

cedge_file = open("cal.cedge.txt", "r") #cal.cedge.txt
cedge = [list(map(float,s.split())) for s in cedge_file.readlines()]

string = ""
for i in range(0,len(cnode)):
    temp = [int(cnode[i][0]), cnode[i][1], cnode[i][2]]
    for j in range(0,len(cedge)):
        if(i == cedge[j][1]):
            temp.extend([int(cedge[j][2]), cedge[j][3]])
        elif(i < cedge[j][1]):
            break
    string += ' '.join([str(v) for v in temp]) + "\n"
    
f = open("ask1out.txt", "w")
f.write(string)
f.close()
