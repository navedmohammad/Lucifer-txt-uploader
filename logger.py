import logging   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
from logging.handlers import RotatingFileHandler   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
logging.basicConfig(   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    level=logging.ERROR,   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    format=   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    datefmt="%d-%b-%y %H:%M:%S",   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    handlers=[   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        RotatingFileHandler("Assist.txt", maxBytes=50000000, backupCount=10),   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        logging.StreamHandler(),   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    ],   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
)   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
logging.getLogger("pyrogram").setLevel(logging.WARNING)   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
logging = logging.getLogger()   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
