string = ""
with open('R_sorted.tsv') as R, open('S_sorted.tsv') as S:
    R_line = R.readline().rstrip()
    S_line = S.readline().rstrip()
    tmp = None
    
    while R_line:
        if(R_line == "" or S_line == ""): break
        
        while(R_line.split('\t')[0] > S_line.split('\t')[0]):
            S_line = S.readline().rstrip()
            if(S_line == ""):
                break
        
        while(R_line != "" and R_line.split('\t')[0] < S_line.split('\t')[0]):
            R_line = R.readline().rstrip()
            pass
        
        if(R_line.split('\t')[0] == S_line.split('\t')[0]):
            while(R_line.split('\t')[0] == S_line.split('\t')[0]):
                if(R_line.split('\t')[1] < S_line.split('\t')[1]):
                    R_line = R.readline().rstrip()
                elif(R_line.split('\t')[1] > S_line.split('\t')[1]):
                    S_line = S.readline().rstrip()
                if(R_line.split('\t')[0] != S_line.split('\t')[0]): break
                if(R_line == "" and S_line == ""): break
                if(tmp != R_line and tmp != S_line):
                    if(R_line.split('\t')[1] == S_line.split('\t')[1]):
                        string += R_line.split('\t')[0] + '\t' + R_line.split('\t')[1] + '\n'
                        print(R_line.split('\t')[0], R_line.split('\t')[1])
                        tmp = R_line
                        S_line = S.readline().rstrip()
                else:
                    S_line = S.readline().rstrip()

f = open("RintersectionS.tsv", "w")
f.write(string)
f.close()
