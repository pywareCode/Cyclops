#Database
#By Tyler Spadgenske

import mysql.connector

conn = mysql.connector.connect(user='root', password='raspberry', database='ANDY')

cursor = conn.cursor()

query = ('SELECT id, object_name, script_path, image_path FROM objects')
cursor.execute(query)

for empid, object_name, image_path, file_path in cursor:
	print empid, object_name, image_path, file_path

cursor.close()
conn.close()
