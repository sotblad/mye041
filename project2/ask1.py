import sys
import pymorton as pm

####start draw
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as patches

def drawPlot(lst):
    data = np.array(lst[1])
    x, y = list(zip(*data))

    #### Rectangle #####
    currentAxis = plt.gca()
    currentAxis.add_patch(
        patches.Rectangle(
            xy=(MBR(lst)[0], MBR(lst)[2]),
            width=MBR(lst)[1] - MBR(lst)[0],
            height=MBR(lst)[3] - MBR(lst)[2],
            linewidth=1,
            color='red',
            fill=False
        )
    )

    plt.scatter(x,y)
    plt.show()

####end draw

def MBR(points):
    x_low = min(point[0] for point in points[1])
    y_low = min(point[1] for point in points[1])
    x_high = max(point[0] for point in points[1])
    y_high = max(point[1] for point in points[1])

    return [x_low, x_high, y_low, y_high]
    
    
def MBR2(points):
    x_low = min(point[0] for point in points)
    y_low = min(point[2] for point in points)
    x_high = max(point[1] for point in points)
    y_high = max(point[3] for point in points)

    return [x_low, x_high, y_low, y_high]
    
def toNormalMBR(lst):
    tempList = []
    for i in range(0, len(lst)):
        tempList.append(lst[i])
    return MBR2(tempList)

def toNormalMBR2(lst):   ### FOR FINISHUP
    tempList = []
    for i in range(0, len(lst)):
        tempList.append(lst[i][2])
    return MBR2(tempList)
        
def calculateMBR(lst): # MBR gia kathe antikeimeno
    result = []
    for i in lst:
        result.append(MBR(i))
    
    return result
    
def calcZOrder(lst): # lst = calculateMBR output
    result = []
    for i in lst:
        x , y = ((i[0]+i[1])/2) , ((i[2]+i[3])/2)
        result.append([pm.interleave_latlng(x,y),i])
    
    return result # [center z-order, [id, MBR]]
    
def sortMBR(lst):
    MBRlist = calculateMBR(lst)
    ZorderList = calcZOrder(MBRlist)
    result = sorted(ZorderList, key=lambda x: x[0])
    return result
    
def createLeaves(lst):
    leaves = []
    leaf = []
    maxPerLeaf = 20
    clean = 0
    count = 0
    for i in range(0, len(lst)):
        leaf.append(lst[i][1])
        count += 1
        
        if(count == maxPerLeaf):
            count = 0;
            leaves.append(leaf)
            clean = 1
            
        if(i == len(lst)-1): # LAST LEAF
            if(len(leaf) < maxPerLeaf*0.4):
                theloume = int(maxPerLeaf*0.4-len(leaf))

                proigoumeno = leaves[len(leaves)-1][int(len(leaves[len(leaves)-1])-theloume):len(leaves[len(leaves)-1])]
                leaves[len(leaves)-1] = leaves[len(leaves)-1][0:int(len(leaves[len(leaves)-1])-theloume)]
                
                leaf = proigoumeno+leaf
                leaves.append(leaf)
            
        if(clean == 1):
            clean = 0
            leaf = []
    return leaves
    
def createTree(leaves):
    layer = []
    realLayer = []
    
    result = []
    for i in range(0, len(leaves)):
        result.append(toNormalMBR(leaves[i]))
        
    isnotleaf = 1
    count = 0
    maxPerLeaf = 20
    clean = 0
    realLayerFinal=[]
    for i in range(0, len(result)):
        layer.append([isnotleaf, i, result[i]]) # TODO: PAKETARE SE 20DES
        count += 1
        
        if(count == maxPerLeaf):
            count = 0;
            realLayer.append(layer)
            clean = 1
            
        if(i == len(result)-1): # LAST LEAF
            if(len(layer) < maxPerLeaf*0.4):
                theloume = int(maxPerLeaf*0.4-len(layer))

                proigoumeno = realLayer[len(realLayer)-1][int(len(realLayer[len(realLayer)-1])-theloume):len(realLayer[len(realLayer)-1])]
                realLayer[len(realLayer)-1] = realLayer[len(realLayer)-1][0:int(len(realLayer[len(realLayer)-1])-theloume)]
                
                layer = proigoumeno+layer
                realLayer.append(layer)
            
        if(clean == 1):
            clean = 0
            layer = []
        
    realLayerFinal.append(leaves)
    realLayerFinal.append(realLayer)

    return realLayerFinal
    
    
def finishUp(lst):
    result = []
    
    counter = 0
    nodeNum = 0
    while(len(lst[len(lst)-1]) != 1):
        layer = []
        realLayer = []
        isnotleaf = 1
        count = 0
        maxPerLeaf = 20
        clean = 0
        realLayerFinal=[]
        
        result = []
        for i in range(0, len(lst[len(lst)-1])):
            result.append(toNormalMBR2(lst[len(lst)-1][i]))

        for i in range(0, len(result)):
            layer.append([isnotleaf, nodeNum, result[i]]) # TODO: PAKETARE SE 20DES
            count += 1
            if(count == maxPerLeaf):
                count = 0;
                realLayer.append(layer)
                clean = 1
                
            if(i == len(result)-1): # LAST LEAF
                if(len(layer) < maxPerLeaf*0.4):
                    theloume = int(maxPerLeaf*0.4-len(layer))
                    
                    if(len(realLayer) != 0):
                        proigoumeno = realLayer[len(realLayer)-1][int(len(realLayer[len(realLayer)-1])-theloume):len(realLayer[len(realLayer)-1])]
                        realLayer[len(realLayer)-1] = realLayer[len(realLayer)-1][0:int(len(realLayer[len(realLayer)-1])-theloume)]
                        
                        layer = proigoumeno+layer
                    realLayer.append(layer)
                    
            if(clean == 1):
                clean = 0
                layer = []
            nodeNum += 1
        nodeNum = 0
        realLayerFinal.append(realLayer)
        counter += 1
        
        lst.append(realLayerFinal[0])
    
    return lst
    
def writeRtree(fullTree):
    string = ""

    nodeId = 0
    string += "[["
    nodeid = 0
    for i in range(0, len(fullTree)):
        for j in range(0, len(fullTree[i])):
            if(i == 0):
                isnonleaf = 0
                if(j != len(fullTree[i])-1):
                    string += str([isnonleaf, nodeId, fullTree[i][j]]) + ", "
                else:
                    string += str([isnonleaf, nodeId, fullTree[i][j]])
            else:
                string += "[" + str(isnonleaf) + ", " + str(nodeId) + ", ["
                isnonleaf = 1
                if(j != len(fullTree[i])-1):
                    for k in range(0, len(fullTree[i][j])):
                        if(k != len(fullTree[i][j])-1):
                            string += str([nodeid, fullTree[i][j][k][2]]) + ", "
                        else:
                            string += str([nodeid, fullTree[i][j][k][2]])
                        nodeid += 1
                    string += "],"
                else:
                    for k in range(0, len(fullTree[i][j])):
                        if(k != len(fullTree[i][j])-1):
                            string += str([nodeid, fullTree[i][j][k][2]]) + ", "
                        else:
                            string += str([nodeid, fullTree[i][j][k][2]])
                        nodeid += 1
                    string += "]"
                string += "]"
            nodeId += 1
        if(i != len(fullTree)-1):
            string += "],\n["

    string += "]]"
    return string


if(len(sys.argv) <= 2 or len(sys.argv) > 3):
    print("Invalid Syntax\nPlease use: python ask1.py 'coords file' 'offsets file'")
    exit()
else:
    try:
        coords = open(sys.argv[1], "r") #coords.txt
        coord_list = [s.rstrip() for s in coords.readlines()]

        offset = open(sys.argv[2], "r") #offsets.txt
        offset_list = [s.rstrip() for s in offset.readlines()]
    except:
        print("Could not read file/s\nPlease check the validity of your input files.")
        exit()

objects = []

for i in offset_list:
    off = i.split(',')
    objTemp, flag = [], 0
    
    for j in range(int(off[1]), int(off[2])+1):
        if(j < len(coord_list)):
            objTemp.append([float(coord_list[j].split(',')[0]), float(coord_list[j].split(',')[1])])
            flag = 1
    if(flag):
        objects.append([int(i.split(',')[0]), objTemp])
    
#######✅ OBJECTS CREATION
#######✅ MBR SINGLE CALCULATION
#######✅ MBR MULTIPLE CALCULATION
#######✅ calcZOrder    -- TODO: CHECK IF ID IS NEEDED
#######✅ sortMBR FULL method

#drawPlot(objects[1000])

sortedMBR = sortMBR(objects)

leaves = createLeaves(sortedMBR)
firstSecondLayer = createTree(leaves)

fullTree = finishUp(firstSecondLayer)

for i in range(0, len(fullTree)):
    print(len(fullTree[i]), ("nodes" if len(fullTree[i]) != 1 else "node"), "at level", i)
    
print(fullTree[2][0][0])

f = open("Rtree.txt", "w")
f.write(writeRtree(fullTree))
f.close()
