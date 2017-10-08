import pymysql
import dbconfig

connection = pymysql.connect(host='localhost',
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crypto_rsa"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crypto_rsa.rsa (
                id int NOT NULL AUTO_INCREMENT,
                name  VARCHAR(50),
                pub_key VARCHAR(1024),
                priv_key VARCHAR(1024),
                PRIMARY KEY (id
                )"""

        cursor.execute(sql);
    connection.commit()

finally:
    connection.close()
