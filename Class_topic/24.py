import pymysql


HOST = 'localhost'
USERNAME = 'root'
PASSWORD ='123456'
DBNAME = 'test'

conn = pymysql.connect(HOST, USERNAME, PASSWORD, DBNAME)
cursor = conn.cursor()

#
# sqlQuery = """ CREATE TABLE users(
#     id INT(11) AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     email VARCHAR(100) NOT NULL
# )"""

sqlQuery = """ INSERT INTO users (id,name,email) VALUES ('4','RAJ','RAJ@GMAIL.COM)
"""
#
# cursor.execute(sqlQuery)
#
# conn.commit()
#
# conn.close()

try:
   # Execute the SQL command
   cursor.execute(sqlQuery)
   # Commit your changes in the database
   conn.commit()
except:
   # Rollback in case there is any error
   conn.rollback()

# disconnect from server
conn.close()
