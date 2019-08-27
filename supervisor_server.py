#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-
import flask, tempfile, os
from offchain_storage import Storage

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

storage = Storage("supervisor.db")
app = flask.Flask(__name__)

@app.route('/')
def index():
	resp = flask.Response("<html><body><h1>Welcome to the Supervisor!</h1></body></html>\n")
	return resp

@app.route('/model/<model_hash>')
def model(model_hash = None):
	model_hash =  flask.escape(model_hash)
	data = storage.get(model_hash)
	resp = flask.Response(data)
	resp.headers["Content-Disposition"] = 'attachment; filename="model.h5"'
	resp.headers["Content-Type"] = "application/octet-stream"
	return resp

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if flask.request.method == 'GET':
		return '''<html><body><form method="post" enctype="multipart/form-data">
    <input type="file" name="the_file">
    <input type="submit" value="Upload File" name="submit"></form></html>\n'''
	elif flask.request.method == 'POST':
		tmp_fd, tmp_fn = tempfile.mkstemp(dir = "/tmp", prefix = "supervisor.")
		flask.request.files["the_file"].save(tmp_fn)
		data = os.read(tmp_fd, 1 << 28)
		digest = storage.put(data)
		os.close(tmp_fd)
		os.remove(tmp_fn)
		return digest

if __name__ == '__main__':
	app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
	app.run("0.0.0.0", 5000)
