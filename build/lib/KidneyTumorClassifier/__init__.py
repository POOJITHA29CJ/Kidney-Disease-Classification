import os
import sys
import logging # create custom logging
logging_str="[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[ #where the log messages are output.
        logging.FileHandler(log_filepath),#handler writes log messages to the specified file (running_logs.log).
        logging.StreamHandler(sys.stdout) #This handler outputs log messages to the console (standard output).
    ]
)
logger=logging.getLogger("KidneyLogger") # creates custom logger
