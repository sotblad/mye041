def mergeSort(list):
    i = 0
    j = 0
    k = 0
    if len(list) > 1:
        mid = len(list)//2
        L = list[:mid]
        R = list[mid:]
        mergeSort(L)
        mergeSort(R)

        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
                list[k] = L[i]
                i = i + 1
            else:
                list[k] = R[j]
                if(L[i][0] == R[j][0]):
                    list[k] = (R[j][0], int(L[i][1])+int(R[j][1]))
                    L[i] = ("", 0)
                    R[j] = ("", 0)
                j = j + 1
            k = k + 1
        while i < len(L):
            list[k] = L[i]
            i = i + 1
            k = k + 1
        
        while j < len(R):
            list[k] = R[j]
            j = j + 1
            k = k + 1

with open('R.tsv') as R:
    R_lines = R.readline().rstrip()

    string = ""
    newlist = []
    while(R_lines):
        R_lines = R_lines.split('\t')
        newlist.append(tuple(R_lines))
        R_lines = R.readline().rstrip()
    
    
    mergeSort(newlist)
    newlist = [i for i in newlist if i != ("", 0)]

    for i in newlist:
        string += i[0] + '\t' + str(i[1]) + '\n'
        print(i[0], i[1])

f = open("Rgroupby.tsv", "w")
f.write(string)
f.close()
