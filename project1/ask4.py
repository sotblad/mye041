string = ""
with open('R_sorted.tsv') as R, open('S_sorted.tsv') as S:
    R_line = R.readline().rstrip()
    S_line = S.readline().rstrip()
    tmp = None
    
    while R_line:
        while(R_line != "" and R_line.split('\t')[0] > S_line.split('\t')[0]):
            S_line = S.readline().rstrip()
            if(S_line == ""):
                break
        
        while(R_line != "" and R_line.split('\t')[0] < S_line.split('\t')[0]):
            if(tmp != R_line):
                string += R_line.split('\t')[0] + '\t' + R_line.split('\t')[1] + '\n'
                print(R_line.split('\t')[0], R_line.split('\t')[1])
            tmp = R_line
            R_line = R.readline().rstrip()
            pass
        
        if(R_line.split('\t')[0] == S_line.split('\t')[0]):
            if(R_line.split('\t')[1] != S_line.split('\t')[1]):
                if(R_line.split('\t')[1] < S_line.split('\t')[1]):
                    if(tmp != R_line):
                        string += R_line.split('\t')[0] + '\t' + R_line.split('\t')[1] + '\n'
                        print(R_line.split('\t')[0], R_line.split('\t')[1])
                    tmp = R_line
                    R_line = R.readline().rstrip()
                elif(R_line.split('\t')[1] > S_line.split('\t')[1]):
                    S_line = S.readline().rstrip()
            else:
                R_line = R.readline().rstrip()
                S_line = S.readline().rstrip()

        if(S_line == ""): #print rest of R
            while(R_line):
                if(tmp != R_line):
                    string += R_line.split('\t')[0] + '\t' + R_line.split('\t')[1] + '\n'
                    print(R_line.split('\t')[0], R_line.split('\t')[1])
                tmp = R_line
                R_line = R.readline().rstrip()

f = open("RdifferenceS.tsv", "w")
f.write(string)
f.close()
