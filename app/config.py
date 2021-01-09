import os


class Configuration(object):
    DEBUG = True
    SECRET_KEY = os.environ['SECRET_KEY']

