from os import environ 

class Config:
    API_ID = environ.get("API_ID", "32969171")
    API_HASH = environ.get("API_HASH", "e4783320b4f0753baf9ade9dc56b775b")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8758810792:AAElWWkOmVcGfw7kDOmX1qjYtx3h6VqIZh8...") 
    BOT_SESSION = environ.get("BOT_SESSION", "your_session_string_here") 
    DATABASE_URL = "mongodb+srv://emirmashuk77:Emirmashuk7860@cluster0.zdfun6c.mongodb.net/forv2db?appName=Cluster0"
    DATABASE_NAME = "forv2db"
    
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
