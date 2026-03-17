import mysql.connector

class Mysql:
    @staticmethod
    def get_mysql_connection():
        cnx = mysql.connector.connect(user = 'root', database = 'digital_hunter')
        return cnx