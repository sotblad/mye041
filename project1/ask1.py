string = ""
with open('R_sorted.tsv') as R, open('S_sorted.tsv') as S:
    R_lines = R.read().split('\n')[:-1]
    S_lines = S.read().split('\n')[:-1]
    pointer = 0
    mark = -1 #not set

    for i, line in enumerate(R_lines):
        R = line.split("\t");
        
        if(mark == -1): #not set
            if(R[0] < S_lines[pointer].split("\t")[0]):
                pass
            while(R[0] > S_lines[pointer].split("\t")[0]):
                pointer += 1
            mark = pointer

        if(R[0] == S_lines[pointer].split("\t")[0]):
            while(R[0] == S_lines[pointer].split("\t")[0]):
                string = string + R[0] + "\t" + R[1] + "\t" + S_lines[pointer].split("\t")[1] + "\n"
                print(R[0], R[1], S_lines[pointer].split("\t")[1])
                pointer += 1
            pointer = mark

        if(i+1 < len(R_lines)):
            if(R[0] != R_lines[i+1].split("\t")[0]):
                pointer = mark
                mark = -1

f = open("RjoinS.tsv", "w")
f.write(string)
f.close()
