


import re
import os
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv

load_dotenv()




id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


      
# Owner Information
API_ID = int(environ.get("API_ID", "22287041"))
API_HASH = environ.get("API_HASH", "c149386dcd58a40fa9fe60e632e161d4")
ADMINS = int(environ.get("ADMINS", "6141937812"))

# Database Information
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://djtecno3:WCisaeUZZNlnsxCC@cluster0.lgs6ieg.mongodb.net/?retryWrites=true&w=majority")
CDB_NAME = environ.get("CDB_NAME", "Cluster0")
DB_URI = environ.get("DB_URI", "mongodb+srv://rr3936764:jTgBEOHznYnWkR02@cluster0.nfwem9w.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "Cluster0")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "")
BOT_USERNAME = environ.get("BOT_USERNAME", "FileXPandaWep_bot") # your bot username without @
PICS = (environ.get('PICS', 'https://graph.org/file/b3125068739885e7109db.jpg https://graph.org/file/b3125068739885e7109db.jpg')).split() # Bot Start Picture

# Auto Delete Information
AUTO_DELETE = int(environ.get("AUTO_DELETE", "10")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "600")) # Time in Seconds


# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002017045810"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002066950447')).split()]



# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)



# File Stream Config
class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'filetolinkvjbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002017045810'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://exceptional-brittaney-bissness-13593939.koyeb.app/"
    else:
        URL = "https://exceptional-brittaney-bissness-13593939.koyeb.app/"



