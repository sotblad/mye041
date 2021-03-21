#Sotirios Panagiotou, 4456

string = ""
with open('R_sorted.tsv') as R, open('S_sorted.tsv') as S:
    R_line = R.readline().rstrip()
    S_line = S.readline().rstrip()
    buffer = []
    maxBuffer = 0
    tmp = None
    
    while R_line:
        if(tmp == R_line.split('\t')[0]):
            for i in buffer:
                string += R_line.split('\t')[0] + '\t' + R_line.split('\t')[1] + '\t' + i.split('\t')[1] + '\n'
                print(R_line.split('\t')[0], R_line.split('\t')[1], i.split('\t')[1])
            pass
        else:
            if(len(buffer) > maxBuffer):
                maxBuffer = len(buffer)
            buffer = []
        
        while(R_line.split('\t')[0] > S_line.split('\t')[0]):
            S_line = S.readline().rstrip()
            if(S_line == ""):
                break
        
        if(R_line.split('\t')[0] < S_line.split('\t')[0]):
            pass
        
        if(R_line.split('\t')[0] == S_line.split('\t')[0]):
            while(R_line.split('\t')[0] == S_line.split('\t')[0]):
                buffer.append(S_line)
                S_line = S.readline().rstrip()
            for i in buffer:
                string += R_line.split('\t')[0] + '\t' + R_line.split('\t')[1] + '\t' + i.split('\t')[1] + '\n'
                print(R_line.split('\t')[0], R_line.split('\t')[1], i.split('\t')[1])
            tmp = R_line.split('\t')[0]

        R_line = R.readline().rstrip()

f = open("RjoinS.tsv", "w")
f.write(string)
f.close()

print("Max buffer size:", maxBuffer)
