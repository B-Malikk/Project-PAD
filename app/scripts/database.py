import mysql.connector
import random

mydb = mysql.connector.connect(
  host="oege.ie.hva.nl",
  user="visserb24",
  password="6Cn328HQUSNPsp",
  database="zvisserb24"
)

mycursor = mydb.cursor()
pasnummer = random.randint(3, 9)
print pasnummer

def PasCheck(pasnummer):
  mycursor.execute("select * from `User` where VALUES(pasnummer)")

def Inchecken(pasnummer):
  mycursor.execute("INSERT INTO `User` (`number`) VALUES (pasnummer)")
  mydb.commit()

def Uitchecken(pasnummer):
  mycursor.execute("DELETE FROM `User` [WHERE condition pasnummer]")
  mydb.commit()


PasCheck()

print(mycursor.rowcount, "record inserted.")
