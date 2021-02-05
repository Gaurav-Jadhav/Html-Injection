import time, logging

def create_log(log_dest,msg):
        FORMAT = '%(current_time)s %(message)s'
        logging.basicConfig(filename=log_dest, format=FORMAT)
        d= {"current_time": "[       " + str(time.strftime("%c")) + "        ] : "}
        logger = logging.getLogger('tcpserver')
        logger.warning(msg, extra=d)

#create_log(log_dest,"add to log")

