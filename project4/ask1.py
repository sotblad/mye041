import sys
import json
import time

def naive(q, disp):
	start_time = time.time()

	tmp = []
	query = queries_list[q]

	for i in range(0,len(transactions)):
		counter = 0
		checked = []
		for j in transactions[i]:
			if(j in query and j not in checked):
				counter += 1
				checked.append(j)
			if(counter == len(queries_list[q]) and i not in tmp):
				tmp.append(i)

	if(disp == 1):
		print("Naive Method result:")
		print(set(tmp))
	print("Naive Method computation time =", (time.time() - start_time), "seconds")

def signature(q, disp):
	start_time = time.time()

	sigfile = []
	for i in range(0,len(transactions_list)):
		bitTmpList = []
		sortedTx = sorted(transactions_list[i])
		bitTmpList = [0]*(sortedTx[len(sortedTx)-1]+1)
		for j in range(0,len(transactions_list[i])):
			bitTmpList[transactions_list[i][j]] = 1
		bitNum = ''.join(str(e) for e in bitTmpList[::-1])
		sigfile.append(bitNum)

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
		print(set(tmp))
	print("Signature File computation time =", (time.time() - start_time), "seconds")

def bitsliced(q, disp):
	start_time = time.time()

	writeBitSlice = ""

	txid = []
	for i in range(0,len(transactions)):
		for j in range(0,len(transactions[i])):
			if(transactions[i][j] not in txid):
				txid.append(transactions[i][j])

	bitslice = []

	dictionary = dict()

	for i in range(0,len(transactions_list)):
		for j in range(0,len(transactions_list[i])):
			if(transactions_list[i][j] not in dictionary):
				dictionary[transactions_list[i][j]] = []
			if(i not in dictionary.get(transactions_list[i][j])):
				dictionary[transactions_list[i][j]] = dictionary.get(transactions_list[i][j]) + [i]

	for i in sorted(dictionary):
		bitTmpList = []
		sortedTx = sorted(dictionary[i])
		bitTmpList = [0]*(sortedTx[len(sortedTx)-1]+1)
		for j in range(0,len(dictionary[i])):
			bitTmpList[dictionary[i][j]] = 1

		bitNum = ''.join(str(e) for e in bitTmpList[::-1])
		bitslice.append(bitNum)
		writeBitSlice += str(i) + ": " + str(int(bitNum,2)) + "\n"

	tmp = []
	
	andList = []
	for i in queries_list[q]:
		andList.append(int(bitslice[i],2))

	for i in range(0,len(andList)-1):
		if(i == 0):
			res = andList[i] & andList[i+1]
		else:
			res &= andList[i+1]

	lst = list(str(bin(res))[2:])
	lst.reverse()
	for i in range(0,len(lst)):
		if(int(lst[i]) == 1):
			tmp.append(i)

	f = open("bitslice.txt", "w")
	f.write(writeBitSlice)
	f.close()

	if(disp == 1):
		print("Bitsliced Signature File result:")
		print(set(tmp))
	print("Bitsliced Signature File computation time =", (time.time() - start_time), "seconds")

def inverted(q, disp):
	start_time = time.time()
	invfile = dict()

	for i in range(0,len(transactions_list)):
		for j in range(0,len(transactions_list[i])):
			if(transactions_list[i][j] not in invfile):
				invfile[transactions_list[i][j]] = []
			if(i not in invfile.get(transactions_list[i][j])):
				invfile[transactions_list[i][j]] = invfile.get(transactions_list[i][j]) + [i]

	writeInvFile = ""
	for i in range(0,len(invfile)):
		if(invfile.get(i)):
			writeInvFile += str(i) + ": " + str(invfile.get(i)) + "\n"
		
	f = open("invfile.txt", "w")
	f.write(writeInvFile)
	f.close()

	itList = []
	for i in queries_list[q]:
		itList.append(invfile[i])

	for i in range(0,len(itList)-1):
		if(i == 0):
			res = set(itList[i]) & set(itList[i+1])
		else:
			res &= set(itList[i+1])

	if(disp == 1):
		print("Inverted File result:")
		print(res)
	print("Inverted File Computation time =", (time.time() - start_time), "seconds")

if(len(sys.argv) <= 4 or len(sys.argv) > 5):
    print("Invalid Syntax\nPlease use: python3 ask1.py transactions.txt queries.txt qnum method")
    exit()
else:
    try:
        transactionsFile = open(sys.argv[1], "r") #transactions.txt
        transactions_list = [json.loads(s.rstrip()) for s in transactionsFile.readlines()]

        queries = open(sys.argv[2], "r") #queries.txt
        queries_list = [json.loads(s.rstrip()) for s in queries.readlines()]

        qnum = int(sys.argv[3])
        method = int(sys.argv[4])
    except:
        print("Could not read file/s\nPlease check the validity of your input files.")
        exit()

transactions = []
for i in range(0,len(transactions_list)):
	transactions.append(transactions_list[i])

#print(transactions[0])
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
