import urllib, json
import sys

def getHashData(startBlock, endBlock):
	"""
	Take a start and end range of blocks and return the corresponding block hashes as a list
	"""

	blockHashes = []
	for block in range (startBlock, endBlock + 1):
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
		myfile = open("jdata.json", "a")
		myfile.write(str(jData))


if __name__ == "__main__":
	# Range 1:
	blockHashes = getHashData(104750, 104751)
	txnList = getTxnList(blockHashes)
	getTxnData(txnList)

"""
	# Range 2:
	getHashData(153500, 153519)

	# Range 3:
	getHashData(413165, 413214)
"""
