#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-
from blockchain import BlockChain
from tclearn_core import *
import json

if __name__ == '__main__':
	# Create the blockchain and add the genesis block
	blockchain = BlockChain()

	# How many blocks should we add to the chain
	# after the genesis block
	num_of_blocks_to_add = 20

	# Add blocks to the chain
	for i in range(0, num_of_blocks_to_add):
		block_data = TCLearnData("XXX-%d" % (i + 1), 0, [0, 1, 2])
		new_block  = blockchain.create_block(block_data)
		print("Here is my new block:\n%s\n" % new_block)
		last_block = blockchain.append_block(new_block)
		# Tell everyone about it!
		print("Block #{} has been added to the blockchain!".format(last_block.get_index()))
		print("Hash: {}".format(last_block.get_hash()))
		print("Data:")
		data = json.loads(last_block.get_data())
		for k in data.keys():
			print("\t%s: %s" % (k, data[k]))
		print()
