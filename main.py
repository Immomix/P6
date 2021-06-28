#!/usr/bin/env python3

import ssh_func
import make_archive
import yaml
import sys
import time
import datetime
import os.path
import pathlib

def read_yaml(file):
	with open(file) as f:
		return yaml.safe_load(f)

file = pathlib.Path(sys.argv[1])

if file.exists ():
	vars = read_yaml(sys.argv[1])
else:
	exit(5)

#action#vars = read_yaml(sys.argv[1])

vars['dailydir'] = time.strftime("%Y%m%d")
vars['namedir'] = "Sauvegardedu" + vars['dailydir'] + ".tar"

make_archive.create(vars)
ssh = ssh_func.connect(vars)
ssh_func.copy(ssh, vars)
ssh_func.delete(ssh, vars)