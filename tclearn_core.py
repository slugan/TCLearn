#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-
import json

class TCLearnData:
	def __init__(self, model_hash, user_id = 0, consortium = None):
		self.model_hash = model_hash
		self.user_id    = user_id
		self.consortium = consortium

	def get_model_hash(self):
		return self.model_hash

	def get_user_id(self):
		return self.user_id

	def get_consortium(self):
		return self.consortium

	def __str__(self):
		return json.dumps({"model_hash": self.model_hash,
		                   "user_id"   : self.user_id,
		                   "consortium": self.consortium})

