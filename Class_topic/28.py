
import pymysql
from datetime import datetime


class MysqlClass:

    def __init__(self, host, username, password, dbName):
        # self.host = host
        # self.username = username
        # self.password = password
        # self.dbName = dbName

        try:
            self.connection = pymysql.connect(host, username, password, dbName)
            #self.connection = pymysql.connect("localhost", "root", "123456", "python_testing")
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        except pymysql.Error, error:
            print(error)

    def __del__(self):

        if hasattr(self, 'connection'):
            self.connection.close()
        else:
            print("self has no connection attribute")

    def createTable(self):

        try:
#self.cursor.execute("DROP TABLE IF EXISTS users ")
            sqlQuery = """CREATE TABLE users (
                        id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        email VARCHAR(100) NOT NULL,
                        phone VARCHAR(20) NOT NULL,
                        created_at datetime NOT NULL,
                        is_active enum('0','1')
                        )"""
            self.cursor.execute(sqlQuery)
            print("Table created successfully.")

        except pymysql.Error, error:
            print('someting went wrong with your query')
            print(error)

        except TypeError, error:
            print (error)

        except ValueError, error:
            print (error)

    def createUser(self, *args):
        try:
            sqlQuery = "INSERT INTO users VALUES{0}".format(args)
            self.cursor.execute(sqlQuery)
            self.connection.commit()
            self.cursor.lastrowid
            print ("User created successfully and UserId is: {0}".format(self.cursor.lastrowid))
        except pymysql.Error, error:
            print (error)
            self.connection.rollback()

    def updateUser(self,value, condition=None):

        if condition:
            sqlQuery = "UPDATE users SET {0} WHERE {1}".format(value, condition)
        else:
            sqlQuery = "UPDATE users SET {0}".format(value)
        try:
            self.cursor.execute(sqlQuery)
            self.connection.commit()
            print("Record Updated successfully")

        except pymysql.Error, error:
            print("something went wrong!")
            print(error)
            self.connection.rollback()

    def deleteUser(self, condition=None):

        if condition:
            sqlQuery = 'DELETE FROM users WHERE {0}'.format(condition)
        else:
            sqlQuery = 'DELETE from users'
        try:
            self.cursor.execute(sqlQuery)
            self.connection.commit()
            print("Record deleted successfully")
        except pymysql.Error, error:
            print("Something went wrong while deleting record")
            print (error)
            self.connection.rollback()

    def fetchUsers(self):
        try:
            sqlQuery = "SELECT * FROM users"
            self.cursor.execute(sqlQuery)
            return self.cursor.fetchall()
        except pymysql.Error, error:
            print (error)

    def findByName(self,name):

        try:
            sqlQuery = "SELECT * from users WHERE name='{0}'".format(name)
            self.cursor.execute(sqlQuery)
            return self.cursor.fetchone()
        except pymysql.Error, error:
            print (error)

    def findById(self,id):

        try:
            sqlQuery = "SELECT * from users WHERE id={0}".format(id)
            self.cursor.execute(sqlQuery)
            return self.cursor.fetchone()
        except pymysql.Error, error:
            print (error)

    def findByEmail(self,email):
        try:
            sqlQuery = "SELECT * from users WHERE email='{0}'".format(email)
            self.cursor.execute(sqlQuery)
            return self.cursor.fetchone()
        except pymysql.Error, error:
            print (error)

mysql = MysqlClass('localhost','root','123456','python_testing')
mysql.createTable()
mysql.createUser(0,'xyz', 'xyz@gmail.com', '9986034800', str(datetime.now()), '1')

#mysql.updateUser('email="manas@gmail.com"', 'id=2' )

#mysql.deleteUser('id=1')

userList = mysql.fetchUsers()
#print (userList)
#
#print (userList)
# for rows in userList:
# print (rows)

#user = mysql.findByEmail('manas@gmail.com')
user = mysql.findById(3)
print (user)

