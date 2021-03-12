string = ""
with open('R_sorted.tsv') as R, open('S_sorted.tsv') as S:
    R_line = R.readline().rstrip()
    S_line = S.readline().rstrip()
    tmp = None
    
    while R_line:
        while(R_line != "" and R_line.split('\t')[0] < S_line.split('\t')[0]):
            if(tmp != R_line):
                print(R_line.split('\t')[0], R_line.split('\t')[1])
            tmp = R_line
            R_line = R.readline().rstrip()
            pass
    
        while(S_line != "" and R_line.split('\t')[0] > S_line.split('\t')[0]):
            if(tmp != S_line):
                print(S_line.split('\t')[0], S_line.split('\t')[1])
            tmp = S_line
            S_line = S.readline().rstrip()
    
        if(R_line.split('\t')[0] == S_line.split('\t')[0]):
            while(R_line.split('\t')[0] == S_line.split('\t')[0]):
                if(R_line.split('\t')[1] < S_line.split('\t')[1]):
                    if(tmp != R_line):
                        print(R_line.split('\t')[0], R_line.split('\t')[1])
                    tmp = R_line
                    R_line = R.readline().rstrip()
                else:
                    if(tmp != S_line):
                        print(S_line.split('\t')[0], S_line.split('\t')[1])
                    tmp = S_line
                    S_line = S.readline().rstrip()
            if(R_line.split('\t')[0] < S_line.split('\t')[0]):
                if(tmp != R_line and R_line != ""):
                    print(R_line.split('\t')[0], R_line.split('\t')[1])
                tmp = R_line
        
        if(R_line == ""): #print rest of S
            while(S_line):
                if(tmp != S_line):
                    print(S_line.split('\t')[0], S_line.split('\t')[1])
                tmp = S_line
                S_line = S.readline().rstrip()
        elif(S_line == ""): #print rest of R
            while(R_line):
                if(tmp != R_line):
                    print(R_line.split('\t')[0], R_line.split('\t')[1])
                tmp = R_line
                R_line = R.readline().rstrip()

f = open("RunionS.tsv", "w")
f.write(string)
f.close()
