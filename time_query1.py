import sqlite3
from timeit import default_timer as timer

#1 SELECT Password FROM XRHSTHS WHERE Username=? --- 20db
print("DB 20")

conn=sqlite3.connect("r20_noindex.db")
cursor=conn.cursor()
start1=timer()
cursor.execute('''SELECT Password
                FROM XRHSTHS
                WHERE Username="brian_clark"''')
end1=timer()
data1=cursor.fetchone()
conn.close()
print(data1)
print("Time without index: ", end1-start1)
print("--------------------------------------------------")
conn=sqlite3.connect("r20_index.db")
cursor=conn.cursor()
start2=timer()
cursor.execute('''SELECT Password
                FROM XRHSTHS
                WHERE Username="brian_clark"''')
end2=timer()
data2=cursor.fetchone()
conn.close()
print(data2)
print("Time with index: ", end2-start2)
print("--------------------------------------------------")


#1 SELECT Password FROM XRHSTHS WHERE Username=? --- 1000db
print("DB 1000")

conn=sqlite3.connect("r1000_noindex.db")
cursor=conn.cursor()
start3=timer()
cursor.execute('''SELECT Password
                FROM XRHSTHS
                WHERE Username="liam_spence"''')
end3=timer()
data3=cursor.fetchone()
conn.close()
print(data3)
print("Time without index: ", end3-start3)
print("--------------------------------------------------")
conn=sqlite3.connect("r1000_index.db")
cursor=conn.cursor()
start4=timer()
cursor.execute('''SELECT Password
                FROM XRHSTHS
                WHERE Username="liam_spence"''')
end4=timer()
data4=cursor.fetchone()
conn.close()
print(data4)
print("Time with index: ", end4-start4)
print("--------------------------------------------------")

#1 SELECT Password FROM XRHSTHS WHERE Username=? --- 5000db
print("DB 5000")

conn=sqlite3.connect("r5000_noindex.db")
cursor=conn.cursor()
start5=timer()
cursor.execute('''SELECT Password
                FROM XRHSTHS
                WHERE Username="sgartellma"''')
end5=timer()
data5=cursor.fetchone()
conn.close()
print(data5)
print("Time without index: ", end5-start5)
print("--------------------------------------------------")
conn=sqlite3.connect("r5000_index.db")
cursor=conn.cursor()
start6=timer()
cursor.execute('''SELECT Password
                FROM XRHSTHS
                WHERE Username="sgartellma"''')
end6=timer()
data6=cursor.fetchone()
conn.close()
print(data6)
print("Time with index: ", end6-start6)
print("--------------------------------------------------")
