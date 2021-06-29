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
import applybackup

local_path = '/home/localuser/Saves/'
sql = 'dump.sql'
save_path = 'var/www/backupsql/'
bdd_user = 'wordpressuser'
bdd_pass = 'toto'
bdd = 'wordpress'

#if sys.argv[1] = 'restore':
applybackup.extract(local_path)
applybackup.restoresql(local_path, save_path, bdd, bdd_user, bdd_pass, sql)
applybackup.restorewordp()
#else :
#	print('argument inexistant où inconue')
#exit(0)

