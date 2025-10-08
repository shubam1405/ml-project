import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")#os.getcwd() → Returns your current working directory, e.g.,
'''
"logs" → Folder name where you want to store log files.

os.path.join(...) → Combines them into a valid path for your OS

'''
os.makedirs(logs_dir, exist_ok=True)
'''
os.makedirs(path) → Creates the folder specified by path.

exist_ok=True → If the folder already exists, do nothing

'''
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)
