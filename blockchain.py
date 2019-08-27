#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-
import hashlib, time, json

# Tiny blockchain code based on Gerald Nash's "Let’s Build the Tiniest Blockchain":
# https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
# © 2017 Gerald Nash

class Block:
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = str(data)
		self.previous_hash = previous_hash
		self.hash = self.hash_block()

	def hash_block(self):
		sha = hashlib.sha256()
		sha.update((str(self.index) +
				   str(self.timestamp) +
				   str(self.data) +
				   str(self.previous_hash)).encode("utf-8"))
		return sha.hexdigest()

	def get_index(self):
		return self.index

	def get_timestamp(self):
		return self.timestamp

	def get_hash(self):
		return self.hash

	def get_previous_hash(self):
		return self.previous_hash

	def get_data(self):
		return self.data

	def __str__(self):
		return json.dumps({"index": self.index,
		                   "timestamp": self.timestamp,
		                   "data": self.data,
		                   "previous_hash": self.previous_hash,
		                   "hash": self.hash})

class BlockChain:
	def __init__(self):
		self.blockchain = [self.create_genesis_block()]
		self.last_block = self.blockchain[0]

	def create_genesis_block(self):
		# Manually construct a block with
		# index zero and arbitrary previous hash
		ts = time.time()
		now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts)) + "%.6f" % (ts % 1)
		return Block(0, now, None, "0")

	def create_block(self, data):
		b_index = self.last_block.index + 1
		ts = time.time()
		b_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts)) + "%.6f" % (ts % 1)
		b_data = data
		b_previous_hash = self.last_block.hash
		return Block(b_index, b_timestamp, b_data, b_previous_hash)

	def append_block(self, new_block):
		if new_block.index != (self.last_block.index + 1):
			print("Error: invalid index")
			return
		if new_block.previous_hash != self.last_block.hash:
			print("Error: invalid hash")
			return
		self.blockchain.append(new_block)
		self.last_block = new_block
		return new_block

	def get_last_block(self):
		return self.last_block

