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
		print "hash: " + jData["blockHash"]
		blockHashes.append(jData["blockHash"])
	print blockHashes
	return blockHashes

# def getTxnList(blockHashes):

"""
def getJsonData(startBlock, endBlock):
	for block in range (startBlock, endBlock + 1):
		blockHashURL = "api.g-coin.org/api/block-index/" + str(block)
		url = 
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		with open("jdata.json", "a") as myfile:
			myfile.write(data)
"""

if __name__ == "__main__":
	# Range 1:
	getHashData(104750, 104779)

	# Range 2:
	getHashData(153500, 153519)

	# Range 3:
	getHashData(413165, 413214)
