#!/usr/bin/env python3

import ssh_func
import make_archive
import applybackup
import yaml
import sys
import time
import datetime
import os.path
import pathlib
#definition du config.yaml et utilisation des information dedans pour utilisé les variables
def read_yaml(file):
	with open(file) as f:
		return yaml.safe_load(f)

file = pathlib.Path(sys.argv[1])

if file.exists ():
	vars = read_yaml(sys.argv[1])
else:
	exit(1)
#variable pour nommer les backup effectué à la date du jour
vars['dailydir'] = time.strftime("%Y%m%d")
vars['namedir'] = "Sauvegardedu" + vars['dailydir'] + ".tar"

#check si un 2eme argument existe et si il est différent de "restore"
#pour appliquer une restoration
#si il n'y as pas de 2eme argument mais que le 1er est bon, creation de backup
if len(sys.argv) > 2:
	if sys.argv[2] == 'restore':
		applybackup.extract(vars)
		applybackup.restoresql(vars)
		applybackup.restorewordp(vars)
	else :
		print('Le 2eme argument est inconue')
		exit(2)
elif len(sys.argv) >= 1:
	make_archive.create(vars)
	ssh = ssh_func.connect(vars)
	ssh_func.copy(ssh, vars)
	ssh_func.delete(ssh, vars)

else:
	print('Le 1er argument est inconnue où est absent')
	exit(3)
