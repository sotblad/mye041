#Sotirios Panagiotou, 4456

import sys
import json
import time

def mergeInter(lst1,lst2):
	result = []
	t1 = 0
	t2 = 0

	while(len(lst1) > t1 and len(lst2) > t2):
		if(lst1[t1] and lst2[t2]):
			if(lst1[t1] < lst2[t2]):
				t1 += 1
			elif(lst1[t1] > lst2[t2]):
				t2 += 1
			else:
				result.append(lst1[t1])
				t1 += 1
				t2 += 1

	return result

def naive(q, disp):
	domi = []
	for i in transactions:
		domi.append(i)

	start_time = time.time()

	tmp = []
	todoQueries = []
	if(q != -1):
		query = queries_list[q]
		todoQueries.append(query)
	else:
		for i in queries_list:
			todoQueries.append(i)

	for k in range(0,len(todoQueries)):
		for i in range(0,len(domi)):
			inter = set(domi[i]).intersection(todoQueries[k])
			if(len(inter) == len(todoQueries[k])):
				tmp.append(i)

	if(disp == 1 and q != -1):
		print("Naive Method result:")
		print(set(tmp))
	print("Naive Method computation time =", (time.time() - start_time), "seconds")

def signature(q, disp):

	sigfile = []
	for i in range(0,len(transactions_list)):
		bitTmpList = []
		sortedTx = sorted(transactions_list[i])
		bitTmpList = [0]*(sortedTx[len(sortedTx)-1]+1)
		for j in range(0,len(transactions_list[i])):
			bitTmpList[transactions_list[i][j]] = 1
		bitNum = ''.join(str(e) for e in bitTmpList[::-1])
		sigfile.append(bitNum)

	start_time = time.time()

	todoQueries = []
	if(q != -1):
		query = queries_list[q]
		todoQueries.append(query)
	else:
		for i in queries_list:
			todoQueries.append(i)

	for k in range(0,len(todoQueries)):
		tmp = []
		bitTmpList = []
		sortedQuery = sorted(todoQueries[k])
		bitTmpList = [0]*(sortedQuery[len(sortedQuery)-1]+1)
		for i in range(0,len(todoQueries[k])):
			bitTmpList[todoQueries[k][i]] = 1
		bitNum = ''.join(str(e) for e in bitTmpList[::-1])

		for i in range(0,len(sigfile)):
				if((int(sigfile[i],2) & int(bitNum,2)) == int(bitNum,2)):
					tmp.append(i)

	if(disp == 1 and q != -1):
		print("Signature File result:")
		print(set(tmp))
	print("Signature File computation time =", (time.time() - start_time), "seconds")

	writeSigfile = ""
	for i in range(0,len(sigfile)):
		writeSigfile += str(int(sigfile[i],2)) + "\n"

	f = open("sigfile.txt", "w")
	f.write(writeSigfile)
	f.close()

def bitsliced(q, disp):

	writeBitSlice = ""
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

	start_time = time.time()

	todoQueries = []
	if(q != -1):
		query = queries_list[q]
		todoQueries.append(query)
	else:
		for i in queries_list:
			todoQueries.append(i)

	for k in range(0,len(todoQueries)):
		tmp = []
		andList = []
		for i in todoQueries[k]:
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

	if(disp == 1 and q != -1):
		print("Bitsliced Signature File result:")
		print(set(tmp))
	print("Bitsliced Signature File computation time =", (time.time() - start_time), "seconds")

	f = open("bitslice.txt", "w")
	f.write(writeBitSlice)
	f.close()

def inverted(q, disp):

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

	start_time = time.time()

	todoQueries = []
	if(q != -1):
		query = queries_list[q]
		todoQueries.append(query)
	else:
		for i in queries_list:
			todoQueries.append(i)

	for k in range(0,len(todoQueries)):
		itList = []
		for i in todoQueries[k]:
			itList.append(invfile[i])

		for i in range(0,len(itList)-1):
			if(i == 0):
				res = set(itList[i]) & set(itList[i+1]) # mergeInter(itList[i],itList[i+1])
			else:
				res &= set(itList[i+1]) # mergeInter(res,itList[i+1])

	if(disp == 1 and q != -1):
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
        if(qnum < -1 or method < -1):
	        exit()
    except:
        print("Something went wrong.\nPlease recheck the inputs entered.")
        exit()

transactions = []
for i in range(0,len(transactions_list)):
	transactions.append(transactions_list[i])

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
