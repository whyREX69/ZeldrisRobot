class Config(object):

    LOGGER = True

    # REQUIRED

    TOKEN = "5189246830:AAEVwFNM_4jtpYSrAw0ntw8oFfXJy0kYNsY"  # Take from @BotFather

    OWNER_ID = (

        "1943696216"  # If you dont know, run the bot and do /id in your private chat with it

    )

    OWNER_USERNAME = "lived_enough"

    API_HASH = f08f8caff5aac56229e9f02bd67e48ea  # for purge stuffs

    API_ID = 12388301

    # RECOMMENDED

    SQLALCHEMY_DATABASE_URI = "postgres://cgomafmg:5jEV1G5O_eEMI9U2HZSd2mLCo9BnDfd2@heffalump.db.elephantsql.com/cgomafmg"  # needed for any database modules

    MESSAGE_DUMP = -1001706596784  # needed to make sure 'save from' messages persist

    REDIS_URL = "redis://something@nothing/anything:10002"  # needed for afk module, get from redislab

    LOAD = []

    NO_LOAD = []

    WEBHOOK = False

    URL = None

    MONGO_URI = "mongodb+srv://vcbot:vcbot@cluster0.dnn8y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    MONGO_PORT = 27017  # leave it as it is

    MONGO_DB = "vcbot"

    # OPTIONAL

    DEV_USERS = (

        [1943696216]

    )  # List of id's (not usernames) for users which have sudo access to the bot.

    SUPPORT_USERS = (

        [1943696216]

    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.

    WHITELIST_USERS = (

        [1943696216]

    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.

    WHITELIST_CHATS = []

    BLACKLIST_CHATS = []

    DONATION_LINK = None  # EG, paypal

    CERT_PATH = None

    PORT = 5000

    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands

    STRICT_GBAN = True

    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!

    BAN_STICKER = None  # banhammer marie sticker

    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /

    CUSTOM_CMD = False  # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!

    API_OPENWEATHER = f075d4857f24108b2020060f402924eb  # OpenWeather API

    SPAMWATCH_API = aCOc7Ah6AEU2uI6nGgHPMc20M5SFMQAF06PObKEM2YgKor0KuijUVA_kbZumOIqT  # Your SpamWatch token

    WALL_API = None

    SPAMMERS = None

class Production(Config):

    LOGGER = False

class Development(Config):

    LOGGER = True

