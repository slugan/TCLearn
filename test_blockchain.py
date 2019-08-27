#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-
from blockchain import BlockChain

# Create the blockchain and add the genesis block
blockchain = BlockChain()

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
	new_block  = blockchain.create_block("Hey! I'm block " + str(i + 1))
	last_block = blockchain.append_block(new_block)
	# Tell everyone about it!
	print("Block #{} has been added to the blockchain!".format(last_block.get_index()))
	print("Hash: {}".format(last_block.get_hash()))
	print("Data: {}\n".format(last_block.get_data()))
