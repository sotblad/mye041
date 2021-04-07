
import sys
import pymorton as pm


####start draw
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as patches

def drawPlot(lst):
    data = np.array(lst)
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
    x_low = min(point[0] for point in points)
    y_low = min(point[1] for point in points)
    x_high = max(point[0] for point in points)
    y_high = max(point[1] for point in points)

    return [x_low, x_high, y_low, y_high]

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
        result.append([pm.interleave_latlng(x,y), [id, i]])
        id += 1
    
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
    for i in range(0, len(sortedMBR)):
        leaf.append(sortedMBR[i][1])
        count += 1
        
        if(count == maxPerLeaf):
            count = 0;
            leaves.append(leaf)
            clean = 1
            
        if(i == len(sortedMBR)-1): # LAST LEAF
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
    
def toNormalMBR(lst):
    tempList = []
    for i in range(0, len(lst)):
        tempList.append([lst[i][1][0], lst[i][1][2], lst[i][1][1], lst[i][1][3]])
    return MBR(tempList)
    
def createTree(leaves, res):
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
        
        
        
    realLayerFinal.append(realLayer)
    
    realLayerFinal.append(leaves)
        
    return realLayer


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


#test = 0
for i in offset_list:
    off = i.split(',')
    objTemp, flag = [], 0
    
    for j in range(int(off[1]), int(off[2])+1):
        if(j < len(coord_list)):
            objTemp.append([float(coord_list[j].split(',')[0]), float(coord_list[j].split(',')[1])])
            flag = 1
    if(flag): #and test < 2821):
        #test += 1
        objects.append(objTemp)
    print(objTemp)
    
#data = np.array([item for sublist in synt for item in sublist])

#print(sorted(calcZOrder(calculateMBR(objects)), key=lambda x: int(x[0])))

#drawPlot(objects[191])
#sortedMBR = sortMBR(objects)
#print(sortedMBR) # MBR gia kathe antikeimeno
    
#print(objects[1])
#print(len(leaves[len(leaves)-1]))
#print(len(leaf[num:len(leaf)]))
    
#drawPlot(objects[1000])

#print(len(createLeaves(sortedMBR)))
test = []
#print(len(objects) , "XAXAXA")
nodes = []
#Leaves = createLeaves(sortedMBR)
res = []
#print(createTree(Leaves, res))

#print([sortedMBR[1][1][1]]+[sortedMBR[0][1][1]])
caount = 0
#print(objects)
#print(Leaves)

#for i in range(0, len(Leaves)):
#    print(len(Leaves[i]))
 #   caount += len(Leaves[i])
   # print(Leaves[i])
    #test.append(i[0][0])
    
#print(sorted(test))
#print(len(objects))

#print(len(Leaves))
#print(caount)


#print(len(Leaves[len(Leaves)-2]))
#print(len(Leaves[len(Leaves)-1]))
