import sys
import pymorton as pm

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
        tempList.append(lst[i][1])
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
    id = 0
    for i in lst:
        x , y = ((i[0]+i[1])/2) , ((i[2]+i[3])/2)
        result.append([pm.interleave_latlng(y,x), [id, i]])
        id += 1
    
    return result # [center z-order, [id, MBR]]
    
def sortMBR(lst):
    MBRlist = calculateMBR(lst)
    ZorderList = calcZOrder(MBRlist)
    result = sorted(ZorderList, key=lambda x: x[0])
    return result
    
def create(leaves, mode): # 0 for leaves, 1 for level 1
    layer = []
    realLayer = []
    
    result = []
    if(mode == 1):
        for i in range(0, len(leaves)):
            result.append(toNormalMBR(leaves[i]))
    else:
        result = leaves
        
    isnotleaf = 1
    count = 0
    maxPerLeaf = 20
    clean = 0
    realLayerFinal=[]
    for i in range(0, len(result)):
        if(mode == 1):
            layer.append([isnotleaf, i, result[i]]) # TODO: PAKETARE SE 20DES
        else:
            layer.append(leaves[i][1])
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
        
    if(mode == 1):
        realLayerFinal.append(leaves)
        realLayerFinal.append(realLayer)

        return realLayerFinal
    else:
        return realLayer
    
    
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
            layer.append([isnotleaf, nodeNum+lst[len(lst)-1][len(lst[len(lst)-1])-1][len(lst[len(lst)-1][len(lst[len(lst)-1])-1])-1][1]+1, result[i]]) # TODO: PAKETARE SE 20DES
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
    string += "["
    nodeid = 0
    for i in range(0, len(fullTree)):
        for j in range(0, len(fullTree[i])):
            if(i == 0):
                isnonleaf = 0
                if(j != len(fullTree[i])-1):
                    string += str([isnonleaf, nodeId, fullTree[i][j]]) + ", \n"
                else:
                    string += str([isnonleaf, nodeId, fullTree[i][j]])
            else:
                isnonleaf = 1
                string += "[" + str(isnonleaf) + ", " + str(nodeId) + ", ["
                if(j != len(fullTree[i])-1):
                    for k in range(0, len(fullTree[i][j])):
                        if(k != len(fullTree[i][j])-1):
                            string += str([fullTree[i][j][k][1], fullTree[i][j][k][2]]) + ", "
                        else:
                            string += str([fullTree[i][j][k][1], fullTree[i][j][k][2]]) + "]],\n"
                else:
                    for k in range(0, len(fullTree[i][j])):
                        if(k != len(fullTree[i][j])-1):
                            string += str([fullTree[i][j][k][1], fullTree[i][j][k][2]]) + ", "
                        else:
                            string += str([fullTree[i][j][k][1], fullTree[i][j][k][2]]) + "]]"
            nodeId += 1
        if(i != len(fullTree)-1):
            string += ",\n"

    string += "]"
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

sortedMBR = sortMBR(objects)
leaves = create(sortedMBR, 0) #0 for Leaves
firstSecondLayer = create(leaves, 1) # 1 for 1st layer
fullTree = finishUp(firstSecondLayer) # continue

for i in range(0, len(fullTree)):
    print(len(fullTree[i]), ("nodes" if len(fullTree[i]) != 1 else "node"), "at level", i)

f = open("Rtree.txt", "w")
f.write(writeRtree(fullTree))
f.close()
