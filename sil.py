import sqlite3


class sil():
    def liste(gelen):
        conn=sqlite3.connect("abcd.db")
        c=conn.cursor()
        c.execute("DELETE FROM abcd WHERE ID='%s';" % gelen)
        conn.commit()


