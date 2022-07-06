class Config:
    SECRET_KEY = 'W0L3JWad!sakpwq'
class DevelopementConfig(Config):
    DEBUG = True
    # MYSQL_HOST='localhost'
    # MYSQL_USER='user_libreria_flask'
    # MYSQL_PASSWORD='12345678'
    # MYSQL_DB = 'libreria_flask'
config = {
    'development': DevelopementConfig,
    'default': DevelopementConfig
}
