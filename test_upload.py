#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-
import requests

filename = "myfile.h5"
response = requests.post('http://localhost:5000/upload', files =
 { "the_file": (filename, open(filename, 'rb'), "application/octet-stream")})
if response.status_code == 200:
	print("Upload successful.\nHash:", response.content.decode("utf-8"))
