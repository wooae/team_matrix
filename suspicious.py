"""
Detecting Suspicious Activity in Bitcoin Blockchain
2016 Microsoft Beauty of Programming Competition
Team Matrix
"""

import numpy as np

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

class Cluster(object):
	"""
	A Cluster is a set of Txns
	"""
	def __init__(self, txns):
		"""
		Txns of a cluster are saved in a list, self.txns
		"""
		self.txns = txns

	def sortTxns(self):
		"""
