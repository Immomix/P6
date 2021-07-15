#!/usr/bin/env python3

import sys
import time
import datetime
import shutil
import tarfile
import os
import paramiko
import subprocess
from scp import SCPClient
from datetime import timedelta


def extract(vars):
# rajouter date
	try:
		if sys.argv[3] in os.listdir(vars['local_path2']):
			with tarfile.open(vars['local_path2'] + sys.argv[3]) as tar:
				tar.extractall(vars['local_path2'])
				print('extract check')
		else:
			print('argv3 dosent exist')
			exit()
	except tarfile.ExtractError:
		print ('erreur')


def restoresql(vars):
#	local_path = '/home/localuser/Saves/'
#	sql = 'dump.sql'
#	sql_save_path = 'var/www/backupsql/'
#	bdd_user = 'wordpressuser'
#	bdd_pass = 'toto'
#	bdd = 'wordpress'

	try:
		k = subprocess.Popen(["mysql -u"+ vars['bdd_user'] +" -p"+ vars['bdd_pass'] +" "+ vars['bdd'] +" < "+ vars['local_path2']+vars['sql_save_path']+vars['sql']], shell=True)
		print('restoresql check')
	except:
		print('nope')

def restorewordp(vars):
#	original = '/home/localuser/Saves/var/www/html/'
#	target = '/var/www/'

	for files in os.listdir(vars['target']):
		i = os.path.join(vars['target'], files)
		try:
			shutil.rmtree(i)
			print('rm check')
		except Exception as e:
			print('cannot delete : ' + e)
	try:
		shutil.move(vars['original'], vars['target'])
		print('restorewordp check')
	except:
		print('erreur shutil.move')
