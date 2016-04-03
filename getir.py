import sqlite3
import datetime
import  time


conn=sqlite3.connect("abcd.db")
c=conn.cursor()
class getir():



    def liste(self):
        c.execute("SELECT * FROM abcd")
        veriler=c.fetchall()

        if veriler:
            return veriler

    def listeYil(yil):

        c.execute("SELECT * FROM abcd WHERE strftime('%Y', tarih)="+"'"+yil+"'")
        veriler=c.fetchall()

        if veriler:
            return veriler




