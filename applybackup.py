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

#extraction des back-ups taré dans le repertoire courant (local_path2)
def extract(vars):
	chosen_backup = vars['backupname'] + vars['date'] + ".tar"
	try:
		if chosen_backup in os.listdir(vars['local_path2']):
			with tarfile.open(vars['local_path2'] + chosen_backup) as tar:
	def is_within_directory(directory, target):
		
		abs_directory = os.path.abspath(directory)
		abs_target = os.path.abspath(target)
	
		prefix = os.path.commonprefix([abs_directory, abs_target])
		
		return prefix == abs_directory
	
	def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
	
		for member in tar.getmembers():
			member_path = os.path.join(path, member.name)
			if not is_within_directory(path, member_path):
				raise Exception("Attempted Path Traversal in Tar File")
	
		tar.extractall(path, members, numeric_owner=numeric_owner) 
		
	
	safe_extract(tar, vars["local_path2"])
				print('extract check')
		else:
			print('choosen_back does not exist')
			exit(9)
	except tarfile.ExtractError:
		print ('tarfile.extractError in applybackup')

#application du backup sql 
def restoresql(vars):
	try:
		k = subprocess.Popen(["mysql -u"+ vars['bdd_user'] +" -p"+ vars['bdd_pass'] +" "+ vars['bdd'] +" < "+ vars['local_path2']+vars['sql_save_path']+vars['sql']], shell=True)
		print('restore sql check')
	except:
		print('restore sql error')
#application du back-up wordpress + suppression 
def restorewordp(vars):
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
