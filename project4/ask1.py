import sys
import json
import time

def naive(q, disp):
	start_time = time.time()
	tmpDict = {}
	tmp = []
	for i in range(0,len(queries_list[q])):
		for j in range(0,len(baseDict[queries_list[q][i]])):
			if(baseDict[queries_list[q][i]][j] not in tmpDict):
				tmpDict[baseDict[queries_list[q][i]][j]] = 0
			tmpDict[baseDict[queries_list[q][i]][j]] += 1
			if(tmpDict[baseDict[queries_list[q][i]][j]] == len(queries_list[q])):
				tmp.append(baseDict[queries_list[q][i]][j])
	if(disp == 1):
		print("Naive Method result:")
		print(tmp)
	print("Naive Method computation time =", (time.time() - start_time), "seconds")

def signature(q, disp):
	start_time = time.time()
	tmp = []
	bitTmpList = []
	sortedQuery = sorted(queries_list[q])
	bitTmpList = [0]*(sortedQuery[len(sortedQuery)-1]+1)
	for i in range(0,len(queries_list[q])):
		bitTmpList[queries_list[q][i]] = 1
	bitNum = ''.join(str(e) for e in bitTmpList[::-1])

	writeSigfile = ""
	for i in range(0,len(sigfile)):
		writeSigfile += str(int(sigfile[i],2)) + "\n"
		if((int(sigfile[i],2) & int(bitNum,2)) == int(bitNum,2)):
			tmp.append(i)
		
	f = open("sigfile.txt", "w")
	f.write(writeSigfile)
	f.close()

	if(disp == 1):
		print("Signature File result:")
		print(tmp)
	print("Signature File computation time =", (time.time() - start_time), "seconds")

def bitsliced(q, disp):
	start_time = time.time()
	if(disp == 1):
		print("Bitsliced Signature File result:")
	print("Bitsliced Signature File computation time =", (time.time() - start_time), "seconds")

def inverted(q, disp):
	start_time = time.time()
	if(disp == 1):
		print("Inverted File result:")
	print("Inverted File Computation time =", (time.time() - start_time), "seconds")

if(len(sys.argv) <= 4 or len(sys.argv) > 5):
    print("Invalid Syntax\nPlease use: python3 ask1.py transactions.txt queries.txt qnum method")
    exit()
else:
    try:
        transactions = open(sys.argv[1], "r") #transactions.txt
        transactions_list = [json.loads(s.rstrip()) for s in transactions.readlines()]

        queries = open(sys.argv[2], "r") #queries.txt
        queries_list = [json.loads(s.rstrip()) for s in queries.readlines()]

        qnum = int(sys.argv[3])
        method = int(sys.argv[4])
    except:
        print("Could not read file/s\nPlease check the validity of your input files.")
        exit()

baseDict = dict()

for i in range(0,len(transactions_list)):
	for j in range(0,len(transactions_list[i])):
		if(transactions_list[i][j] not in baseDict):
			baseDict[transactions_list[i][j]] = []
		if(i not in baseDict.get(transactions_list[i][j])):
			baseDict[transactions_list[i][j]] = baseDict.get(transactions_list[i][j]) + [i]

sigfile = []
for i in range(0,len(transactions_list)):
	bitTmpList = []
	sortedTx = sorted(transactions_list[i])
	bitTmpList = [0]*(sortedTx[len(sortedTx)-1]+1)
	for j in range(0,len(transactions_list[i])):
		bitTmpList[transactions_list[i][j]] = 1
	bitNum = ''.join(str(e) for e in bitTmpList[::-1])
	sigfile.append(bitNum)

#print(sigfile)


if(method == 0):
	naive(qnum,1)
elif(method == 1):
	signature(qnum,1)
elif(method == 2):
	bitsliced(qnum,1)
elif(method == 3):
	inverted(qnum,1)
elif(method == -1):
	dispFlag = 1
	if(qnum == -1):
		dispFlag = 0
	naive(qnum,dispFlag)
	signature(qnum,dispFlag)
	bitsliced(qnum,dispFlag)
	inverted(qnum,dispFlag)
