import sqlite3

conn=sqlite3.connect("r20_index.db")
cursor=conn.cursor()
cursor.execute('''CREATE INDEX ind1 on
                XRHSTHS(Username);''')
cursor.execute('''CREATE INDEX ind4 on
                KANEI(ID_Xrhsth);''')
cursor.execute('''CREATE INDEX ind5 on
                KRATHSH(Arrival);''')
conn.commit()
conn.close()


conn=sqlite3.connect("r1000_index.db")
cursor=conn.cursor()
cursor.execute('''CREATE INDEX ind1 on
                XRHSTHS(Username);''')
cursor.execute('''CREATE INDEX ind4 on
                KANEI(ID_Xrhsth);''')
cursor.execute('''CREATE INDEX ind5 on
                KRATHSH(Arrival);''')
conn.commit()
conn.close()

conn=sqlite3.connect("r5000_index.db")
cursor=conn.cursor()
cursor.execute('''CREATE INDEX ind1 on
                XRHSTHS(Username);''')
cursor.execute('''CREATE INDEX ind4 on
                KANEI(ID_Xrhsth);''')
cursor.execute('''CREATE INDEX ind5 on
                KRATHSH(Arrival);''')
conn.commit()
conn.close()
