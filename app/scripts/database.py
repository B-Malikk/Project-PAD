import mysql.connector
import random

mydb = mysql.connector.connect(
  host="oege.ie.hva.nl",
  user="visserb24",
  password="6Cn328HQUSNPsp",
  database="zvisserb24"
)

mycursor = mydb.cursor()
pasnummer = "56 f5 45 6r"
print(pasnummer)
mycursor.execute("INSERT INTO `User` (`nummer`, `inklokken`, `tijd`) VALUES ('56 f5 45 6r', TRUE, current_time)")
mydb.commit()
mycursor.execute("SELECT (`id`,`nummer`, `inklokken`) FROM `User` ORDER BY `id` LIMIT 1")
user = mycursor.fetchall()
user = str(''.join(map(str, user)))

print(user)