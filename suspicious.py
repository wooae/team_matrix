"""
Detecting Suspicious Activity in Bitcoin Blockchain
2016 Microsoft Beauty of Programming Competition
Team Matrix
"""

import numpy as np
import json

class Txn(object):
	"""
	Represents a transaction
	"""
	def __init__(self, tid, vin, vout, addrin, addrout, time):
		"""
		Initialize transaction id, value in, value out, address in, address out, and time
		"""
		self.tid = tid
		self.vin = vin
		self.vout = vout
		self.addrin = addrin
		self.addrout = addrout
		self.time = time

class Node(object):
	"""
	Represents a transaction to be placed in a linked list
	"""
	def __init__ (self, data, next_node):
		"""
		Initialize node with data and next node
		"""

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new):
		self.next_node = new

class TxnList(object):
	"""
	A Cluster is a set of Txns
	"""
	def __init__(self, head):
		"""
		Txns of a cluster are saved in a list, self.txns
		"""
		self.txns = txns

	def sortTxns(self):
		"""
		Returns list of transactions, sorted in ascending order by value in
		"""
		return sorted(txns, key=txns[1])

def getData(jname):
	"""
	Transform json data into Txn object format
	"""
	Jdata = json.loads(open(jname))
	new_txn = Txn()
	for txn in Jdata["vin"]:
		new_txn.addrin.append(Jdata["addr"])
	for txn in Jdata["vout"]:
		for i in Jdata["scriptPubKey"]:
			new_txn.addrout.append(Jdata["addresses"])
	new_txn.vin = Jdata["valueIn"]
	new_txn.vout = Jdata["valueOut"]
	new_txn.time = Jdata["time"]
	return new_txn


def findLoop(head):
	turtle = head
	hare = head

	while hare != None:
		turtle = turtle.next

		if hare.next != None:
			hare = hare.next.next
		else:
			return False

		if turtle == hare:
			return True

if __name__ == "__main__":
	with open("test.json") as jname
		new_txn = getData(jname)
	
