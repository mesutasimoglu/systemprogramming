import sqlite3



conn=sqlite3.connect("abcd.db")
c=conn.cursor()
class getir():



    def liste(self):
        c.execute("SELECT * FROM abcd  ORDER BY ID DESC")
        veriler=c.fetchall()

        if veriler:
            return veriler

    def listeYil(yil):

        c.execute("SELECT * FROM abcd WHERE strftime('%Y', tarih)="+"'"+yil+"'")
        veriler=c.fetchall()

        if veriler:
            return veriler

    def idGetir(gelen):

        c.execute("select ID FROM abcd where strftime('%H:%M:%S',tarih)="+"'"+gelen+"'" )
        veriler=c.fetchall()


        return veriler










