#!/usr/bin/env python3

import sys #pour les arguments
import time #pour date les sauvegardes
import datetime
import shutil #copy and del des fichiers
import os #Create dir and del
import tarfile
import paramiko
from scp import SCPClient
from datetime import timedelta
#etablissement de la connection en ssh entre la machine local et distante
def connect(vars):
	try:
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname=vars['ip_address'],username=vars['name'],password=vars['passw'])
		print('connect check')
		return (ssh_client)
	except:
		print('erreur dans la fonction connect')
#copie des back-up sur le serveur distant
def copy(handle_ssh, vars):
	try:
		scp = SCPClient(handle_ssh.get_transport())
		scp.put(vars['local_path'] + "/" + vars['namedir'],vars['remote_path'])
		print('copy check')
	except:
		print('erreur dans la fonction copy')
#supression de la 8eme plus vielle sauvegarde sur le serveur local et distant 
def delete(handle_ssh, vars):
	sftp = handle_ssh.open_sftp()
	try:
		for entry in sftp.listdir_attr(vars['remote_path']):
			timestamp = entry.st_mtime
			createtime = datetime.datetime.fromtimestamp(timestamp)
			now = datetime.datetime.now()
			delta = now - createtime
			if delta.days >= 7:
				filepath = vars['remote_path'] + '/' + entry.filename
				filepath2 = vars['local_path'] + '/' + entry.filename
				sftp.remove(filepath)
				os.remove(filepath2)
		print('delete check')
	except paramiko.ssh_exception.AuthenticationException:
		print('Authentication failed')
		exit (2)
	except:
		print('erreur dans la fonction delete')
