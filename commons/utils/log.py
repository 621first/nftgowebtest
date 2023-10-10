'''
@filename: /log
@time: 2023/10/9 16:04
'''
import logging
import logging.handlers
import datetime

def get_logger():
	logger = logging.getLogger('mylogger')
	logger.setLevel(logging.DEBUG)

	rf_handler = logging.handlers.TimedRotatingFileHandler('./logs/all.log',when='midnight',interval=1,backupCount=0,atTime=datetime.time(0,0,0,0))
	rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

	f_handler = logging.FileHandler('./logs/error.log')
	f_handler.setLevel(logging.ERROR)
	f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

	logger.addHandler(rf_handler)
	logger.addHandler(f_handler)

	return logger