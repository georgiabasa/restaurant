import sqlite3

conn=sqlite3.connect("r1_index.db")
conn.execute('''CREATE INDEX ind1 on
                XRHSTHS(Username);''')
conn.execute('''CREATE INDEX ind2 on
                KRATHSH(Arrival);''')
conn.execute('''CREATE INDEX ind3 on
                KRITIKH(Barcode);''')
conn.execute('''CREATE INDEX ind4 on
                GRAFEI(Barcode_Kritikhs);''')
conn.execute('''CREATE INDEX ind5 on
                GRAFEI(ID_Pelath);''')
conn.execute('''CREATE INDEX ind6 on
                PELATHS(ID_Xrhsth);''')
conn.execute('''CREATE INDEX ind7 on
                KRITIKH(Rate);''')
conn.execute('''CREATE INDEX ind8 on
                XRHSTHS(ID);''')
conn.execute('''CREATE INDEX ind9 on
                PELATHS(Lname);''')
conn.execute('''CREATE INDEX ind10 on
                KRATHSH(Name);''')
conn.execute('''CREATE INDEX ind11 on
                KRATHSH(ID);''')
conn.execute('''CREATE INDEX ind12 on
                KRATHSH(MobileNumber);''')
conn.execute('''CREATE INDEX ind13 on
                AFORA(ID_Krathshs);''')
conn.execute('''CREATE INDEX ind14 on
                KANEI(ID_Krathshs);''')
conn.execute('''CREATE INDEX ind15 on
                KANEI(ID_Xrhsth);''')
conn.execute('''CREATE INDEX ind16 on
                PROTIMHSEIS(ID_Pelath);''')
conn.execute('''CREATE INDEX ind17 on
                ALLERGIA_PROTIMHSEIS(ID_Pelath);''')
conn.execute('''CREATE INDEX ind18 on
                PELATHS(MobileNum);''')
conn.execute('''CREATE INDEX ind19 on
                TRAPEZI(Capacity);''')
conn.execute('''CREATE INDEX ind20 on
                AFORA(ID_Trapeziou);''')
conn.execute('''CREATE INDEX ind21 on
                TRAPEZI(ID);''')
conn.execute('''CREATE INDEX ind22 on
                TRAPEZI(Position_X);''')
conn.execute('''CREATE INDEX ind23 on
                TRAPEZI(Position_Y);''')
conn.close()
