from peewee import MySQLDatabase

import my_config


db = MySQLDatabase(
    database=my_config.MYSQL_DATABASE,
    host=my_config.MYSQL_HOST,
    user=my_config.MYSQL_USER,
    password=my_config.MYSQL_PASSWORD
)


