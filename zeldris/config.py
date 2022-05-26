from zeldris.sample_config import Config

class Development(Config):

    OWNER_ID = 1943696216  # your telegram ID

    OWNER_USERNAME = "lived_enough"  # your telegram username

    TOKEN = "5189246830:AAEVwFNM_4jtpYSrAw0ntw8oFfXJy0kYNsY"  # your bot token, as provided by the @botfather

    SQLALCHEMY_DATABASE_URI = 'postgres://cgomafmg:5jEV1G5O_eEMI9U2HZSd2mLCo9BnDfd2@heffalump.db.elephantsql.com/cgomafmg'  # sample db credentials

    MESSAGE_DUMP = '-1001706596784' # some group chat that your bot is a member of

    USE_MESSAGE_DUMP = True

    SUDO_USERS = [1943696216]  # List of id's for users which have sudo access to the bot.

    LOAD = []

    NO_LOAD = ['translation']

    MONGO_URI = mongodb+srv://vcbot:vcbot@cluster0.dnn8y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority""

    MONGO_PORT = 27017  # leave it as it is

    MONGO_DB = "Zeldris"
