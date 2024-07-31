import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__))

env_file = "{}/../../envs/api.env".format(APP_ROOT)
load_dotenv(env_file)


print(os.getenv('DB_NAME'))
class Config:
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT', 5432)

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f'postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
