import mysql.connector
from mysql.connector import errorcode
class DAO:
    """
    Connection to database
    """
    def __init__(self):
        self.user='admin'
        self.password='K64m1fhwDhQO'
        self.database='mydb'
        self.host='database-1.cbyvojjyxfwg.us-east-1.rds.amazonaws.com'
    def connectDB(self):
        cnx = mysql.connector.connect(user=self.user, password = self.password, database=self.database, host=self.host)
        return cnx