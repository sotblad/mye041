import sys
import json
import time

def naive(q):
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
	print("Naive Method result:")
	print(tmp)
	print("Naive Method computation time =", (time.time() - start_time), "seconds")

def signature(q):
	start_time = time.time()
	print("Signature File result:")
	print("Signature File computation time =", (time.time() - start_time), "seconds")

def bitsliced(q):
	start_time = time.time()
	print("Bitsliced Signature File result:")
	print("Bitsliced Signature File computation time =", (time.time() - start_time), "seconds")

def inverted(q):
	start_time = time.time()
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

if(method == 0):
	naive(qnum)
elif(method == 1):
	signature(qnum)
elif(method == 2):
	bitsliced(qnum)
elif(method == 3):
	inverted(qnum)
elif(method == -1):
	naive(qnum)
	signature(qnum)
	bitsliced(qnum)
	inverted(qnum)
