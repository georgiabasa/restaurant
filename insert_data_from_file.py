import sqlite3

#insert admin as xrhsths
conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()
cursor.execute("INSERT INTO XRHSTHS (ID,Username,Password) VALUES (0,'admin','1234')")
conn.commit()
conn.close()

#insert xrhsth-pelath
file=open("xristis.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines:
    id,username,password,fname,lname,mobile,a_num,a_st,a_code=line.strip().split('\t')
    cursor.execute("INSERT INTO XRHSTHS (ID,Username,Password) VALUES (?,?,?)",
                   (id,username,password))
    cursor.execute("INSERT INTO PELATHS (ID_Xrhsth,Fname,Lname,MobileNum,Address_PostalCode,Address_Street,Address_Number) VALUES (?,?,?,?,?,?,?)",
                   (id,fname,lname,mobile,a_code,a_st,a_num))
conn.commit()
conn.close()


#insert diaxeiristh
file=open("diaxeiristis.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines:
    id_em, start_shift, end_shift, id=line.strip().split('\t')
    cursor.execute("INSERT INTO DIAXEIRISTHS (ID_Employee,Start_shift,End_shift,ID_Xrhsth) VALUES (?,?,?,?)",
                   (id_em, start_shift, end_shift, id))
conn.commit()
conn.close()

#insert xwros
file=open("xwros.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines:
    id_dep,indoors,floor=line.strip().split('\t')
    cursor.execute("INSERT INTO XWROS (ID_Department,Indoors,Floor) VALUES (?,?,?)",
                   (id_dep,indoors,floor))
conn.commit()
conn.close()

#insert protimhseis
file=open("protimhseis.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines:
    fav_des,fav_dr,id_pelath=line.strip().split('\t')
    cursor.execute("INSERT INTO PROTIMHSEIS (Favorite_Dessert,Favorite_Drink,ID_Pelath) VALUES (?,?,?)",
                   (fav_des,fav_dr,id_pelath))
conn.commit()
conn.close()

#insert allergies
file=open("allergies.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines:
    substance,id_pelath=line.strip().split('\t')
    cursor.execute("INSERT INTO ALLERGIA_PROTIMHSEIS (Substance,ID_Pelath) VALUES (?,?)",
                   (substance,id_pelath))
conn.commit()
conn.close()

#insert epikoinwnei
file=open("epikoinwnei.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines:
    how,id_d,fn_p,ln_p,mn_p,id_k=line.strip().split('\t')
    cursor.execute("INSERT INTO EPIKOINWNEI (How,ID_Diaxeiristh,Fname_Pelath,Lname_Pelath,MobileNum_Pelath,ID_Krathshs) VALUES (?,?,?,?,?,?)",
                   (how,id_d,fn_p,ln_p,mn_p,id_k))
    
conn.commit()
conn.close()

#insert not user
file=open("epikoinwnei.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines[:10]:
    how,id_d,fn_p,ln_p,mn_p,id_k=line.strip().split('\t')
    cursor.execute("INSERT INTO PELATHS (Fname,Lname,MobileNum) VALUES (?,?,?)",
                    (fn_p,ln_p,mn_p))
    
conn.commit()
conn.close()


#insert kratisi
file=open("kratisi.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines:
    id,name,mobnum,num_of_p,arrival,id_trap=line.strip().split('\t')
    cursor.execute("INSERT INTO KRATHSH (ID,Name,MobileNumber,Num_of_People,Arrival) VALUES (?,?,?,?,?)",
                   (id,name,mobnum,num_of_p,arrival))
    cursor.execute("INSERT INTO AFORA (ID_Krathshs,ID_Trapeziou) VALUES (?,?)",
                    (id,id_trap))
conn.commit()
conn.close()

#insert kanei
file=open("kanei.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines:
    id_xr,id_krat,date_res=line.strip().split('\t')
    cursor.execute("INSERT INTO KANEI (ID_Xrhsth,ID_Krathshs,Date_Reservation) VALUES (?,?,?)",
                   (id_xr,id_krat,date_res))
conn.commit()
conn.close()

#insert trapezi
file=open("trapezi.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines:
    id,capacity,pos_x,pos_y,id_dep=line.strip().split('\t')
    cursor.execute("INSERT INTO TRAPEZI (ID,Capacity,Position_X,Position_Y,ID_Xwrou) VALUES (?,?,?,?,?)",
                   (id,capacity,pos_x,pos_y,id_dep))
conn.commit()
conn.close()

#insert kritiki
file=open("kritiki.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines:
    barcode,rate,id_krat,comment=line.strip().split('\t')
    cursor.execute("INSERT INTO KRITIKH (Barcode,Rate,ID_Krathshs,Comment) VALUES (?,?,?,?)",
                   (barcode,rate,id_krat,comment))
conn.commit()
conn.close()

#insert grafei
file=open("grafei.txt", "r")
lines=file.readlines()

conn=sqlite3.connect("r0_noindex.db")
cursor=conn.cursor()

for line in lines:
    id_p,barcode,date_rev=line.strip().split('\t')
    cursor.execute("INSERT INTO GRAFEI (ID_Pelath,Barcode_Kritikhs,Date_Review) VALUES (?,?,?)",
                   (id_p,barcode,date_rev))
conn.commit()
conn.close()
