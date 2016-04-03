import sqlite3
import datetime
import time




conn=sqlite3.connect("abcd.db")
c=conn.cursor()

class ekle():

    def isles(params):
        conn=sqlite3.connect("abcd.db")
        c=conn.cursor()

        c.execute("INSERT INTO abcd(tarih,url) VALUES(?,?)",params)
        conn.commit()
c.close()
conn.close()



