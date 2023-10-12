import os
import sys
import shutil
import paramiko
from datetime import datetime
import logging
import logging.handlers as handlers
import time
from config import *   #import credential from config file
import datetime as dt
import json

#print(hostname)
logger = logging.getLogger('file_transfer')
logger.setLevel(logging.INFO)
now = dt.datetime.utcnow() + dt.timedelta(hours=5, minutes=30)
print(now)
date_str = now.strftime("%m-%d-%Y")

## Here we define our formatter
formatter = logging.Formatter( now.strftime("%m-%d-%Y %H:%M:%S")+', %(name)s, %(levelname)s, %(message)s')
logpath = logpath + '/SFTP_logger_'+date_str+'.txt'
print(logpath)
logHandler = handlers.TimedRotatingFileHandler(logpath, when='M', interval=1, backupCount=0)
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
f = open(JSONpath)
data = json.load(f)
print('entering to Object creation')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
logger.info(data)

for j in data:
    list1data = j['inboxpath']
    fileoutpath = j['outboxpath']
    list1= os.listdir (list1data)
    print(list1)
    if len(list1):
        try:
            if key_filename:
                ssh.connect(hostname, username=username, key_filename=key_filename)
            elif password:
                ssh.connect(hostname, username=username, password=key_password)
            else:
                print("Either key_filename or password must be provided")
            sftp=ssh.connect(hostname, username=username, key_filename=key_filename)
            print('Connection established successfully. ')
            logger.info('Connection established successfully. ')
            sftp = ssh.open_sftp()
        except:
            print("Connection failure. ")
            e = sys.exc_info()
            print("Exception: {0}".format(e))
            logger.info("Exception: {0}".format(e))
        else:
            logger.info("SFTP job transfer started")
            arr = list1 
            print(arr)
            for i in arr:
                try:
                    print(i)
                    logger.info("processing for file===> "+list1data+"/"+i)
                    sftp.put(list1data+'/'+i,sftppath+'/'+i)
                    sftp=ssh.close()
                except:
                    e = sys.exc_info()
                    logger.info("File transfer - `"+i+"` failure.--> {0}".format(e))
                    print("File transfer - `"+i+"` failure.--> {0}".format(e))
                else:
                    logger.info('file uploaded successfully ='+i)
                    print('file uploaded=',i)
                    if not os.path.exists(fileoutpath):
                        os.makedirs(fileoutpath)
                    shutil.move(os.path.join(list1data+'/', i), os.path.join(fileoutpath+'/', i))
                    logger.info("File `"+i+"` moved successfully to "+fileoutpath)  


print('SFTP Job completed')
logger.info("SFTP Job completed at "+ now.strftime("%m-%d-%Y %H:%M:%S"))

