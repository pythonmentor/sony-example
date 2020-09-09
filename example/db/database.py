from mysql.connector import connect 

import config

db = connect(
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=33306,
    database=config.DB_NAME,
    charset=config.DB_CHARSET
)