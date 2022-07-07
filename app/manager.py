import os
from flask import current_app


# from module_1 import iniciar_app
# from module_2 import iniciar_app2 
from module_3 import create_app 
from config import config

class Config(object):
# CRITICAL CONFIG VALUE: This tells Flask-Collect where to put our static files!
# Standard practice is to use a folder named "static" that resides in the top-level of the project directory.
# You are not bound to this location, however; you may use basically any directory that you wish.
    # COLLECT_STATIC_ROOT = os.path.dirname(__file__) + '/static'
    # COLLECT_STORAGE = 'flask_collect.storage.file'
    DEBUG = True

app = create_app(Config)



if __name__ == "__main__":
    app.run()