#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-
import requests

hash = "d557325707915c88d91c61103f5cab8dd39fd19a6e275652873e90934fbab745"
response = requests.get("http://localhost:5000/model/" + hash)
if response.status_code == 200:
	filename = response.headers["Content-Disposition"].split('"')[1]
	with open("/tmp/" + filename, "wb") as fp:
		fp.write(response.content)
		fp.close()
	print("Download successful.\nFilename:", filename)
