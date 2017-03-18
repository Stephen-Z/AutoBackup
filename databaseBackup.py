# -*- coding: utf-8 -*-
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from configobj import ConfigObj
import os
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


baseCFG=ConfigObj("./config.cfg")
dbuser=baseCFG["baseConfig"]["dbusername"]
dbpasswd=baseCFG["baseConfig"]["dbpassword"]
dbName=baseCFG["baseConfig"]["dbName"]
fileInfo=baseCFG["baseConfig"]["resultFileLocation"]+"/"
interval=baseCFG["baseConfig"]["interval"]


def checkFolder():
    currentDate=time.strftime("%Y-%m-%d")
    storeLocation=fileInfo+currentDate+'/'
    if not os.path.exists(storeLocation):
        try:
            os.mkdir(storeLocation)
        except:
            traceback.print_stack()
    return storeLocation



def autoBackup():
    print "Start backup the database."
    storeInfo=checkFolder()+dbName+'.sql'
    try:
        #tmpTime=time.strftime("%Y-%m-%d")
        tmp=os.system("mysqldump -u {0} -p{1} --databases {2} --result-file={3}".format(dbuser,dbpasswd,dbName,storeInfo))
        #print tmp
    except Exception as e:
        traceback.print_stack()
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
        print "Occured some error when trying to Backup the database....{0}\n\n".format(currentTime)
    else:
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
        print "Backup completed!!!=====>{0}".format(currentTime)
        print "Next backup will Start after "+interval+" minutes."
        print('Press Ctrl+{0} to exit\n\n'.format('Break' if os.name == 'nt' else 'C'))

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(autoBackup, 'interval', minutes=int(interval))
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass