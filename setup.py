import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="vrishank")

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE data2")
mycursor.execute("use data2")
mycursor.execute("CREATE TABLE gmail_id(gmail VARCHAR(255))")
mycursor.execute("CREATE TABLE hoteld(username VARCHAR(255),pincode VARCHAR(255),date1 VARCHAR(255),date2 VARCHAR(255))")
mycursor.execute("CREATE TABLE userdata(username VARCHAR(255), address VARCHAR(255))")
mycursor.execute("CREATE TABLE valet(username VARCHAR(255),pincode VARCHAR(255),PAC VARCHAR(255),time VARCHAR(255))")
print("all database and tables are created")


###all modules download command prompt commands
#pip install secure-smtplib
#pip install pillow
#pip install mysql.connector
##tkinter,winsound,random,webbrowser are inbuilt
#use ctrle+H in main.oy or VARP Project to replace database password
