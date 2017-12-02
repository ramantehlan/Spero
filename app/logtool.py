from flask import Flask, request
from datetime import datetime
import os.path
import os

class Log():
    
    def __init__(self, logfile = '/var/www/html/flask_template/urcpp.log'):
        self.logfile = logfile
    
    
    def writer(self, level, page, message):
        envK = "HTTP_X_PROXY_REMOTE_USER"
        username = request.environ.get(envK)
        # username = os.environ[envK]
        log = open(self.logfile, 'a')
        ip      = request.remote_addr
        date    = datetime.today()
        logInfo = '[{0}] [{1}] [{2}] [{3}] [{4}] {5} \n'.format(str(date), level, ip, username ,page,  message)
        print(logInfo)
        log.write(logInfo)
        log.close()
        
        

    
    
    
