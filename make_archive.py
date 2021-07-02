#!/usr/bin/env python3

import sys #pour les arguments
import time #pour date les sauvegardes
import datetime
import shutil #copy and del des fichiers
import os #Create dir and del
import tarfile
import paramiko
import subprocess
from scp import SCPClient
from datetime import timedelta

def create(vars):
	username = vars['bdd_user']
	try:
		with open(vars['bdd_path_to_save']+vars['bdd_save_name'],'w') as output:
			c = subprocess.Popen(["mysqldump -u "+ vars['bdd_user']+" -p"+ vars['bdd_pass']+" "+ vars['bdd']], stdout=output, shell=True)
		with tarfile.open (vars['local_path'] + "/" + vars['namedir'], 'w') as archive:
			for path_to_save in vars['save_path']:
				archive.add (path_to_save)
		print('archive.add check')
	except tarfile.CompressionError:
		print('tarfile.CompressionError')
		exit(0)
	except tarfile.TarError:
		print('tarfile.tarError')
		exit(1)
	except:
		print('erreur dans la fonction create')
