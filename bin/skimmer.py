#!/usr/bin/env python

import os
import sys
import pickle

def init():
	dict = {}
	for dirname, dirnames, filenames in os.walk('.'):
		for filename in filenames:
			dict[filename] = os.path.join(dirname, filename)
	return dict

def write_all(list):
	output = open('data.pkl', 'wb')
	pickle.dump(list, output)
	output.close()
	
def read_all():
	data_file = open('data.pkl', 'rb')
	data = pickle.load(data_file)
	data_file.close()
	return data

def get_file(filename):
	return read_all()[filename]

filename = sys.argv[1].strip()
if (filename == 'init_repo'):
	write_all(init())
else:
	os.system('vim ' + get_file(filename))
