string = ""
with open('R_sorted.tsv') as R, open('S_sorted.tsv') as S:
    R_lines = R.read().split('\n')[:-1]
    S_lines = S.read().split('\n')[:-1]
    pointer = 0
    mark = -1 #not set
    tmp = None
    
    for i, line in enumerate(R_lines):
        R = line.split("\t");
        
        
        if(R[0] < S_lines[pointer].split("\t")[0]):
            print(R[0], R[1])
            pass
        while(R[0] > S_lines[pointer].split("\t")[0]):
            print(S_lines[pointer].split("\t")[0], S_lines[pointer].split("\t")[1])
            if(R == S_lines[pointer+1].split("\t")):
                pointer += 1
            if(S_lines[pointer].split("\t")[0] != S_lines[pointer+1].split("\t")[0]):
                if(R[0] <= S_lines[pointer].split("\t")[0]):
                    print(R[0],R[1])
            pointer += 1
        
        if(R[0] == S_lines[pointer].split("\t")[0]):
            while(R[0] == S_lines[pointer].split("\t")[0]):
                if(R[1] <= S_lines[pointer].split("\t")[1]):
                    print(R[0], R[1])
                    break
                if(R[1] > S_lines[pointer].split("\t")[1]):
                    string = string + R[0] + "\t" + R[1] + "\t" + S_lines[pointer].split("\t")[1] + "\n"
                    print(R[0], S_lines[pointer].split("\t")[1])
                    
                    if(R == S_lines[pointer+1].split("\t")):
                        pointer += 1
                    if(S_lines[pointer].split("\t")[0] != S_lines[pointer+1].split("\t")[0]):
                        print(R[0],R[1])
                    pointer += 1


f = open("RunionS.tsv", "w")
f.write(string)
f.close()
