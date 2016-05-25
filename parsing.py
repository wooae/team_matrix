import urllib, json
import sys

def getHashData(startBlock, endBlock):
	"""
	Take a start and end range of blocks and return the corresponding block hashes as a list
	"""

	blockHashes = []
	for block in range (startBlock, endBlock + 1):
		print "block: " + str(block)
		blockHashURL = "http://api.g-coin.org/api/block-index/" + str(block)
		response = urllib.urlopen(blockHashURL)
		jData = json.loads(response.read())
#		print "hash: " + jData["blockHash"]
		blockHashes.append(jData["blockHash"])
#		print blockHashes
	return blockHashes

def getTxnList(blockHashes):
	"""
	Find all transactions associated with block hashes
	"""

	txnList = []
	for blockHash in blockHashes:
		blockURL = "http://api.g-coin.org/api/block/" + str(blockHash)
		response = urllib.urlopen(blockURL)
		jData = json.loads(response.read())
		for txn in jData["tx"]:
			txnList.append(txn)
			print "transaction: " + txn
	return txnList


def getTxnData(txnList):
	for txn in txnList:
		txnURL = "http://api.g-coin.org/api/tx/" + str(txn)
		response = urllib.urlopen(txnURL)
		jData = json.loads(response.read())
		numAddrIn = 0
		addrIn = []
		valIn = []
		for addr in jData["vin"]:
			if 'addr' not in addr:
				continue
			else:
				numAddrIn += 1
				addrIn.append(addr["addr"])
				valIn.append(addr["value"])
		numAddrOut = 0
		addrOut = []
		valOut = []
		for addr in jData["vout"]:
			print "vouts"
			if 'scriptPubKey' not in addr:
				continue
			else:
				numAddrOut += 1
				for a in addr["scriptPubKey"]:
					if a == "addresses":
						addrOut.append(addr["scriptPubKey"][a])
					if a == "value":
						valOut.append(addr["scriptPubKey"][a])

		if 'valueIn' not in jData:
			continue
		if 'valueOut' not in jData:
			continue
		myfile = open("data.txt", "a")
		line = str(jData["time"]) + " " + str(jData["valueIn"]) + " " + str(numAddrIn) + " " + str(numAddrOut) + "\n"
		myfile.write(line)

		# addresses In
		for addr in addrIn:
			myfile.write(str(addr) + " ")
		myfile.write("\n")

		# values In
		for val in valIn:
			myfile.write(str(val) + " ")
		myfile.write("\n")

		# addresses Out
		for addr in addrOut:
			myfile.write(str(addr) + " ")
		myfile.write("\n")

		# values Out
		for val in valOut:
			myfile.write(str(val) + " ")
		myfile.write("\n")
		

if __name__ == "__main__":
	"""
	# test
	blockHashes = getHashData(104750, 104755)
	txnList = getTxnList(blockHashes)
	getTxnData(txnList)

	"""
	# Range 1:
	blockHashes = getHashData(104750, 104779)
	txnList = getTxnList(blockHashes)
	getTxnData(txnList)

	# Range 2:
	blockHashes2 = getHashData(153500, 153519)
	txnList2 = getTxnList(blockHashes2)
	getTxnData(txnList2)

	# Range 3:
	blockHashes3 = getHashData(413165, 413214)
	txnList3 = getTxnList(blockHashes3)
	getTxnData(txnList3)
