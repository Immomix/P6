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

try:
	if sys.argv[1] == 'restore':
		applybackup.extract()
		applybackup.restoresql()
		applybackup.restorewordp()
	else :
		print('argument inexistant où inconue')
except:
	print('invalid or missing arguments')
