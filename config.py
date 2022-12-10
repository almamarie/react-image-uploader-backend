import os
from urllib.parse import quote_plus
from settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER


SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))


DB_PATH = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
    DB_USER, DB_PASSWORD, quote_plus(DB_HOST), DB_NAME)
# DB_PATH = "postgres://marieloumar:c89V948PzuNvrh8nb6nLPdJfE8n9YuO5@dpg-cea7mr6n6mphc8sj172g-a.oregon-postgres.render.com/fileupload"
# DB_PATH = "postgres://marieloumar:c89V948PzuNvrh8nb6nLPdJfE8n9YuO5@dpg-cea7mr6n6mphc8sj172g-a/fileupload"

# postgres://marieloumar:c89V948PzuNvrh8nb6nLPdJfE8n9YuO5@dpg-cea7mr6n6mphc8sj172g-a.oregon-postgres.render.com/fileupload

# Enable debug mode.
DEBUG = True

# Connect to the database


SQLALCHEMY_DATABASE_URI = DB_PATH
