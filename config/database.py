import logging
from masoniteorm.connections import ConnectionResolver

DATABASES = {
    "default": "sqlite",
    "sqlite": {
        "driver": "sqlite",
        "database": "aeon.sqlite3",
        "log_queries": True,
    },
}

DB = ConnectionResolver().set_connection_details(DATABASES)
DB.morph_map({})
logger = logging.getLogger('masoniteorm.connection.queries')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)
