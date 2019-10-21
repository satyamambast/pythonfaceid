import mysql.connector


class Ui_MainWindow(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",user="root",passwd="root", database="courier"        )
        self.mycursor = self.mydb.cursor()
        #self.mycursor.execute("SHOW DATABASES"