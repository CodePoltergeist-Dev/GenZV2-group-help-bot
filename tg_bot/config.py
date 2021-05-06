class Config(object):
    LOGGER = True

class Development(Config):
    OWNER_ID = 1151079777  # my telegram ID
    OWNER_USERNAME = ""  # my telegram username
    API_KEY = ""  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']