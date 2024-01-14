import sqlite3

#insert afora
file=open("AFORA.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_index.db")
cursor=conn.cursor()

for line in lines:
    id_kr,id_tr=line.strip().split('\t')
    cursor.execute("INSERT INTO AFORA (ID_Krathshs,ID_Trapeziou) VALUES (?,?)",
                   (id_kr,id_tr))
conn.commit()
conn.close()

#insert allergies
file=open("ALLERGIA_PROTIMHSEIS.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    sub,id_p=line.strip().split('\t')
    cursor.execute("INSERT INTO ALLERGIA_PROTIMHSEIS (Substance,ID_Pelath) VALUES (?,?)",
                   (sub,id_p))
conn.commit()
conn.close()

#insert diax
file=open("DIAXEIRISTHS.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    id_em,start,end,id_x=line.strip().split('\t')
    cursor.execute("INSERT INTO DIAXEIRISTHS (ID_Employee,Start_shift,End_shift,ID_Xrhsth) VALUES (?,?,?,?)",
                   (id_em,start,end,id_x))
conn.commit()
conn.close()

#insert epikoinwnei
file=open("EPIKOINWNEI.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    how,id_d,fnp,lnp,mnp,id_kr=line.strip().split('\t')
    cursor.execute("INSERT INTO EPIKOINWNEI (How,ID_Diaxeiristh,Fname_Pelath,Lname_Pelath,MobileNum_Pelath,ID_Krathshs) VALUES (?,?,?,?,?,?)",
                   (how,id_d,fnp,lnp,mnp,id_kr))
conn.commit()
conn.close()

#insert grafei
file=open("GRAFEI.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    idp,bar_kr,date_rev=line.strip().split('\t')
    cursor.execute("INSERT INTO GRAFEI (ID_Pelath,Barcode_Kritikhs,Date_Review) VALUES (?,?,?)",
                   (idp,bar_kr,date_rev))
conn.commit()
conn.close()

#insert kanei
file=open("KANEI.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    idx,id_kr,date_res=line.strip().split('\t')
    cursor.execute("INSERT INTO KANEI (ID_Xrhsth,ID_Krathshs,Date_Reservation) VALUES (?,?,?)",
                   (idx,id_kr,date_res))
conn.commit()
conn.close()

#insert kratisi
file=open("KRATHSH.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    id,name,mn,people,arrival=line.strip().split('\t')
    cursor.execute("INSERT INTO KRATHSH (ID,Name,MobileNumber,Num_of_People,Arrival) VALUES (?,?,?,?,?)",
                   (id,name,mn,people,arrival))
conn.commit()
conn.close()

#insert kritiki
file=open("KRITIKH.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    bar,rate,id_kr,comm=line.strip().split('\t')
    cursor.execute("INSERT INTO KRITIKH (Barcode,Rate,ID_Krathshs,Comment) VALUES (?,?,?,?)",
                   (bar,rate,id_kr,comm))
conn.commit()
conn.close()

#insert protimiseis
file=open("PROTIMHSEIS.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    fav_des,fav_dr,idp=line.strip().split('\t')
    cursor.execute("INSERT INTO PROTIMHSEIS (Favorite_Dessert,Favorite_Drink,ID_Pelath) VALUES (?,?,?)",
                   (fav_des,fav_dr,idp))
conn.commit()
conn.close()

#insert trapezi
file=open("TRAPEZI.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    id,cap,px,py,id_x=line.strip().split('\t')
    cursor.execute("INSERT INTO TRAPEZI (ID,Capacity,Position_X,Position_Y,ID_Xwrou) VALUES (?,?,?,?,?)",
                   (id,cap,px,py,id_x))
conn.commit()
conn.close()

#insert xristis
file=open("XRHSTHS.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    id,username,password=line.strip().split('\t')
    cursor.execute("INSERT INTO XRHSTHS (ID,Username,Password) VALUES (?,?,?)",
                   (id,username,password))
conn.commit()
conn.close()

#insert xwros
file=open("XWROS.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    id_d,indoors,floor=line.strip().split('\t')
    cursor.execute("INSERT INTO XWROS (ID_Department,Indoors,Floor) VALUES (?,?,?)",
                   (id_d,indoors,floor))
conn.commit()
conn.close()

#insert pelatis
file=open("PELATHS.txt", "r")
lines=file.readlines()
conn=sqlite3.connect("r1_noindex.db")
cursor=conn.cursor()

for line in lines:
    idx,fname,lname,mn,acode,astreet,anumber,blacklisted=line.strip().split('\t')
    cursor.execute("INSERT INTO PELATHS (ID_Xrhsth,Fname,Lname,MobileNum,Address_PostalCode,Address_Street,Address_Number,Blacklisted) VALUES (?,?,?,?,?,?,?,?)",
                   (idx,fname,lname,mn,acode,astreet,anumber,blacklisted))
conn.commit()
conn.close()
