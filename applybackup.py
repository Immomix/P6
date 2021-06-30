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


def extract():
	local_path = '/home/localuser/Saves/'

	try:
		with tarfile.open(local_path+"Sauvegardedu20210526.tar") as tar:   #remplacer le sauvegardedublablabla par le argv
			tar.extractall(local_path)
			print('extact check')
	except tarfile.ExtractError:
		print ('erreur')


def restoresql():
	local_path = '/home/localuser/Saves/'
	sql = 'dump.sql'
	save_path = 'var/www/backupsql/'
	bdd_user = 'wordpressuser'
	bdd_pass = 'toto'
	bdd = 'wordpress'

	try:
		k = subprocess.Popen(["mysql -u"+ bdd_user +" -p"+ bdd_pass +" "+ bdd +" < "+ local_path+save_path+sql], shell=True)
		print('restoresql check')
	except:
		print('nope')

def restorewordp():
	original = '/home/localuser/Saves/var/www/html/'
	target = '/var/www/'

	for files in os.listdir(target):
		i = os.path.join(target, files)
		try:
			shutil.rmtree(i)
			print('rm check')
		except Exception as e:
			print('cannot delete : ' + e)
	try:
		shutil.move(original, target)
		print('restorewordp check')
	except:
		print('erreur shutil.move')
