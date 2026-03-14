from os import environ 

class Config:
    API_ID = environ.get("API_ID", "32969171")
    API_HASH = environ.get("API_HASH", "e4783320b4f0753baf9ade9dc56b775b")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8758810792:AAElWWkOmVcGfw7kDOmX1qjYtx3h6VqIZh8...") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQH3EdMAD5TQsgVGILK5YgStXjQO0hkRtYBd3W543CLsxV-lYc4G3-DM8ZoKZXyp1A2ci-e1Hgg7MVovb9DAaxofMVyynpuVvKU4kL7KxAm2h8q7ZlV72zZaRy7LBREvz0rYVXYuuhrTQNXyBa72Hokid6QJk_mkHtjHssMUQEohB1Pe6UhxDA1_G2iDbQ8O97rs5aaGN87Eu9uZkIhSFmoeUfJk5DoQfn7jV1I2qVHr3brXRcO75_MV4ATTZUFCdPOiNQUomvJHO3A5csapVRIpcQFhMYFIFEaZXdn1QPiyfs9sgxXaREbdT7UWISIRKJCD5xD4kPW5XBtrEY3c02EgXQAAAAGT5Gn-AA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
