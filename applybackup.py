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
#import config.yaml

local_path = '/home/localuser/Saves/'
sql = 'dump.sql'
save_path = 'var/www/backupsql/'
bdd_user = 'wordpressuser'
bdd_pass = 'toto'
bdd = 'wordpress'


#extract
try:
	with tarfile.open(local_path+"Sauvegardedu20210526.tar") as tar:
		tar.extractall(local_path)
except tarfile.ExtractError:
	print ('erreur')


#restoresql
try:
	k = subprocess.Popen(["mysql -u"+ bdd_user +" -p"+ bdd_pass +" "+ bdd +" < "+ local_path+save_path+sql], shell=True)
except:
	print('nope')

#restorewordp

try 


#faire une fonction check_time pour valider l'argument

try:
	if sys.argv[?] is in os.lsitdir(local_path)
		#appliqué le backup du jour etc
	else
		print('file does not exist')

