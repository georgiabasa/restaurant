import sqlite3
from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import ast
import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime, timedelta
from tkinter import Tk, Label, PhotoImage
from PIL import Image, ImageTk

#dimiourgia arxikou para8urou me epiloges signin kai signup
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)
        

img = PhotoImage(file='login.png')
Label(root,image=img, bg='white').place(x=50,y=100)

frame=Frame(root,width=850,height=350,bg='white').place(x=480,y=70)
heading=Label(frame,text="Welcome to our Restaurant", fg='#FF9C00',bg='white',font=('Microsoft YaHei UI Light',23,'bold')).place(x=450,y=10)


def on_enter(e, widget, default_text):
    widget.delete(0, 'end')

def on_leave(e, widget, default_text):
    if widget.get() == '':
        widget.insert(0, default_text)
        
#############################################################################################################################################################
#epilogi signin

def signin(): #pairnei username password
    username=user.get()
    password=code.get()
    #pairnei ton password tou sugkekrimenou user
    conn=sqlite3.connect("restaurant.db")
    c=conn.cursor()
    c.execute(''' SELECT Password FROM XRHSTHS WHERE Username=? ''', (username,))
    result = c.fetchone()
    conn.close()

    if result is not None: #an uparxei ontws o user stin vasi
        stored_password=result[0] #pairnei ton kwdiko tou

        if password==stored_password: #elegxos an password pou kataxwri8ike einai o swstos sumfwna me tin vasi
            #dimiourgia neou para8urou App
            root.destroy()
            screen=Tk()
            screen.title("App")
            screen.geometry('925x500+300+200')
            screen.config(bg="#FF9C00")
            screen.resizable(False,False)

            def make_reservation(diax): #koini sinartisi me orisma diax gia tis parapanw epiloges p xei o diax kata tin Make Reservation
        
                def check_availability():  #elegxos dia8esimotitas      
                    num=entry_num_people.get() #number_of_people
                    selected_date=cal.get_date() #epilegmeni imerominia apoo to calendar
                    arrival_time=entry_arrival_time.get() #arrival time
                    #prosarmogi sto format tis vasi gia arrival_datetime
                    selected_date=datetime.strptime(selected_date,"%Y-%m-%d").date()
                    arrival_time=datetime.strptime(arrival_time,"%H:%M").time()
                    arrival_datetime=datetime.combine(selected_date,arrival_time)

                    def timediff6(datetime1,datetime2): #sunartisi gia elegxo 6 wrwn diaforas meta3u 2 datetime (arrival epilogis kai arrival kratisewn idias meras) 
                        if datetime1 == '0000-00-00 00:00:00':
                            return True
                        else:
                            if isinstance(datetime1, str): #apofugi bug apo datetime type vasis
                                datetime1 = datetime.strptime(datetime1, "%Y-%m-%d %H:%M:%S")
                                    
                            time_diff=abs(datetime1-datetime2)
                            six_hours=timedelta(hours=6) #trapezia menoun desmevmena gia 6 wres kai mporei na kleistei to idio to argotero 6 wres prin 3ana
                            return time_diff>=six_hours
                        
                    def get_tables_capacity(capacity): #vriskei dedomena trapeziwn gia dwthen capacity
                        conn=sqlite3.connect("restaurant.db")
                        cursor=conn.cursor()
                        cursor.execute("SELECT ID,Position_X,Position_Y,ID_Xwrou FROM TRAPEZI WHERE Capacity=?", (capacity,))
                        result=cursor.fetchall()
                        conn.close()
                        return result

                    def table0(_x, _y, table_id,next_table_id,dep): #vazei ta trapezia ston xarti tis diepafis
                        _X=0
                        _Y=0
                        #print("dep",dep, "x",_x,"y",_y)
                        if dep==111:
                            _X=(int(_x)*10)+600
                            _Y=(int(_y)*10)+50

                        elif dep==222:
                            _X=(int(_x)*10)+780
                            _Y=(int(_y)*10)+50
                        #_x,_y einai oi suntetagmenes sti vasi, _X,_Y einai oi suntetagmenes sti grafiki diepafi gia logous morfopoiisis
                        Button(avail,width=2,bg='black',fg='white',border=5, command=lambda x=_x, y=_y, _id=table_id, next_id=next_table_id: reserve0(x,y,_id,next_id)).place(x=_X,y=_Y)
                            
                    def reserve0(_x,_y,table_id,next_table_id): # kaleitai molis patithei kapoio table gia pragmatopoiisi kratisis
                        #print("Reserving Table ", table_id)
                        name=entry_name.get() # pairnei onoma
                        mobnum=entry_mobnum.get() #pairnei mobilenum
                        if name!="" and mobnum!="xxxx-xxxxxxxxxx" and arrival_time!="" and num!="": #elegxos stoixeiwn
                            if validate_mobile_number(mobnum): #elegxos format mobnum
                                        #print("Reservation Made")
                                        #print("Number of People:", num)
                                        #print("Selected Date:", selected_date)
                                        #print("Arrival Time:", arrival_time)
                                        #print("Name:", name)
                                        #print("Mobile Number:", mobnum)
                                        #print("Table Location: x={}, y={}".format(_x,_y))
                                #eisagei sti vasi ta dedomena tis kratisis
                                conn0=sqlite3.connect("restaurant.db")
                                cursor0=conn0.cursor()
                                cursor0.execute('''INSERT INTO KRATHSH (Name,MobileNumber,Num_of_People,Arrival) VALUES(?,?,?,?)''',
                                                        (name,mobnum,num,arrival_datetime))
                                conn0.commit()
                                conn0.close()
                                #pairnei to id tou xristi kai to id tis kratisis p molis egine
                                conn0=sqlite3.connect("restaurant.db")
                                cursor0=conn0.cursor()
                                cursor0.execute("SELECT X.ID,MAX(K.ID) FROM XRHSTHS as X,KRATHSH as K WHERE Username=?", (username,))
                                id_s=cursor0.fetchall()
                                #print(id_s)
                                #sumfwna me ta id eisagei dedomena sti vasi sto KANEI kai sto AFORA
                                cursor0.execute('''INSERT INTO KANEI (ID_Xrhsth,ID_Krathshs) VALUES(?,?)''',
                                                        (id_s[0][0],id_s[0][1]))
                                cursor0.execute('''INSERT INTO AFORA (ID_Krathshs,ID_Trapeziou) VALUES (?,?)''',
                                                        (id_s[0][1],table_id))
                                if next_table_id: #an uparxei diplano trapezi to eisagei k afto sto AFORA
                                    cursor0.execute('''INSERT INTO AFORA (ID_Krathshs,ID_Trapeziou) VALUES (?,?)''',
                                                        (id_s[0][1],next_table_id))
                                conn0.commit()
                                conn0.close()

                                if diax: #an einai o diaxeiristis
                                    how=how_combo_box.get() #pairnei to how
                                    id_diax=id_diax_combo_box.get() #pairnei to poios diax
                                    conn0=sqlite3.connect("restaurant.db")
                                    cursor0=conn0.cursor()
                                    #vriskei to Fname tou pelati gia dwthen Lname=name_kratisis kai mobilenum=mobilenum_kratisis (o diax ta vazei einai stadar oi plirofories etsi na dinontai)
                                    cursor0.execute("SELECT Fname FROM PELATHS WHERE Lname=? AND MobileNum=?",
                                                         (name,mobnum))
                                    fname=cursor0.fetchone()
                                    #eisagei ta dedomena sto epikoinwnei poios diax me poion pelati pws kai gia poia kratisi
                                    cursor0.execute('''INSERT INTO EPIKOINWNEI (How,ID_Diaxeiristh,Fname_Pelath,Lname_Pelath,MobileNum_Pelath,ID_Krathshs) VALUES(?,?,?,?,?,?)''',
                                                         (how,id_diax,fname[0],name,mobnum,id_s[0][1]))
                                    conn0.commit()
                                    conn0.close()

                                messagebox.showinfo('Reserved', 'Sucessfully reserved. Thank you for choosing us!')
                                avail.destroy()
                                #message box gia antistoixa errors
                            else:
                                messagebox.showerror('Invalid', "Invalid mobile number format. Please enter a valid number in the format 0000-0000000000.")
                        else:
                            messagebox.showerror('Invalid', "Please fill all entries!")
                        
                    def get_arrival_for_table(result,capacity,next_table_id): #elegxei gia ta trapezia pou exoun kratisi idia mera tin diafora wras

                        conn=sqlite3.connect("restaurant.db")
                        cursor=conn.cursor()

                        for table in result:
                            #print("TABLE ID:", table[0])
                            cursor.execute("SELECT Arrival,ID_Trapeziou FROM KRATHSH, AFORA WHERE ID=ID_Krathshs AND ID_Trapeziou=?", (table[0],))
                            arrivals=cursor.fetchall()

                            table_available=True #arxika ola dia8esima
                                
                            for arrival in arrivals:
                                    ##print("Arrival in db:", arrival[0])
                                    ##print("Selected arrival", arrival_datetime)
                                if table[0]==arrival[1]:
                                    if not timediff6(arrival[0], arrival_datetime):
                                        #print("table", table[0], " is not available")
                                        table_available=False #opoio vriskei me diafora ligoteri twn 6 wrwn to kanei unavailable
                                        break
                            if table_available:
                                    ##print("Placing buttons for table:", table[0])
                                table0(table[1],table[2],table[0],next_table_id,table[3]) #osa einai available kaloun tin table0 kai topothetountai ston xarti
                                                
                        conn.close()

                    if(num!="" and arrival_time!=""): #elegxos valid stoixeiwn
                        res.destroy()
                        #dimiourgia neou para8urou gia ton xarti
                        avail=Tk()
                        avail.title("App")
                        avail.geometry('925x500+300+200')
                        avail.config(bg="#FF9C00")
                        avail.resizable(False,False)
                        num=int(num)
                        
                        if num==1 or num==2: #an number_of_people 1 i 2 tote psakse trapezi me capacity=2
                            capacity=2
                            result=get_tables_capacity(capacity)
                            if result:
                                get_arrival_for_table(result,capacity,0)
                            else: #an den uparxoun trapezia gia 2 tote psakse gia 4
                                capacity1=4
                                result1=get_tables_capacity(capacity1)
                                if result1:
                                    get_arrival_for_table(result1,capacity1,0)
                                else: #an den uparxoun trapezia gia 4 tote psakse gia 8
                                    capacity2=8
                                    result2=get_tables_capacity(capacity2)
                                    if result2:
                                        get_arrival_for_table(result2,capacity2,0)
                                    else: #alliws messagebox den uparxei trapezi
                                        messagebox.showinfo('Table not found', 'Unfortunately, there is no available table for your demands!')
                                        avail.destroy()
                                
                        elif num==3 or num==4: #an number_of_people 3 i 4 tote psakse trapezi me capacity=4
                            capacity=4
                            result=get_tables_capacity(capacity)
                            if result:
                                get_arrival_for_table(result,capacity,0)
                            else: #an den uparxoun trapezia gia 4 tote psakse gia 8
                                capacity1=8
                                result1=get_tables_capacity(capacity1)
                                if result1:
                                    get_arrival_for_table(result1,capacity1,0)
                                else: #alliws messagebox den uparxei trapezi
                                    messagebox.showinfo('Table not found', 'Unfortunately, there is no available table for your demands!')
                                    avail.destroy()
                                
                        elif num==5 or num==6 or num==7 or num==8: #an number_of_people 5,6,7 i 8 tote psakse trapezi me capacity=8
                            capacity=8
                            result=get_tables_capacity(capacity)
                            if result:
                                get_arrival_for_table(result,capacity,0)
                            else: #alliws messagebox den uparxei trapezi
                                messagebox.showinfo('Table not found', 'Unfortunately, there is no available table for your demands!')
                                avail.destroy()
                                
                        elif num>8: #an number_of_people>8 prepei na enwthoun trapezia
                            capacity=8
                            result=get_tables_capacity(capacity) #psakse trapezia gia 8 atoma
                            if result: #an uparxoun
                                conn8=sqlite3.connect("restaurant.db")
                                cursor8=conn8.cursor()
                                    
                                for table in result: #vres ta arrival time tous kai sugkrine ta me to dwthen
                                    cursor8.execute("SELECT Arrival,ID_Trapeziou FROM KRATHSH, AFORA WHERE ID=ID_Krathshs AND ID_Trapeziou=?", (table[0],))
                                    arrivals=cursor8.fetchall()

                                    table_available=all(timediff6(arrival[0],arrival_datetime) for arrival in arrivals) #elegxos gia diafora 6 wrwn

                                    if table_available: #an uparxoun diathesima pare ta x,y,xwro tous
                                        conn1=sqlite3.connect("restaurant.db")
                                        cursor1=conn1.cursor()
                                        cursor1.execute("SELECT Position_X,Position_Y,ID_Xwrou FROM TRAPEZI WHERE ID!=? AND Capacity=?", (table[0],capacity))
                                        tables_nearby=cursor1.fetchall()
                                        conn1.close()

                                        for table_nearby in tables_nearby: #gia afta twra psakse ola ta diplana tous +-4(x axis) kai +-4(y axis)
                                            conn2=sqlite3.connect("restaurant.db")
                                            cursor2=conn2.cursor()
                                            cursor2.execute("SELECT ID, Capacity, ID_Xwrou FROM TRAPEZI \
                                                            WHERE ((Position_X=? OR Position_X=?) AND Position_Y=?) \
                                                            OR ((Position_Y=? OR Position_Y=?) AND Position_X=?)",
                                                            (int(table_nearby[0])+4,int(table_nearby[0])-4,table_nearby[1],int(table_nearby[1])+4,int(table_nearby[1])-4,table_nearby[0]))
                                            next_tables=cursor2.fetchall()
                                            conn2.close()

                                            for next_table in next_tables: #gia ta diplana tous
                                                if(num<=(next_table[1]+capacity)): #elegxos capacity apo to 8ari + capacit dipla kaluptoun to number_of_people
                                                    conn5=sqlite3.connect("restaurant.db")
                                                    cursor5=conn5.cursor()
                                                    #vres arrival twn diplanwn
                                                    cursor5.execute("SELECT Arrival FROM KRATHSH, AFORA WHERE ID=ID_Krathshs AND ID_Trapeziou=?", (next_table[0],))
                                                    next_arrivals=cursor5.fetchall()
                                                    conn5.close()
                                                    #diplana pou exoun timediif 6 wres
                                                    next_table_available=all(timediff6(next_arrival[0],arrival_datetime) for next_arrival in next_arrivals)

                                                    if next_table_available: # an uparxoun tote vazei sto xwro ta 8aria me tin table0
                                                        table0(table_nearby[0],table_nearby[1],table[0],next_table[0],table_nearby[2])
                                conn8.close()
                                
                            else: #alliws messagebox den uparxei trapezi
                                messagebox.showinfo('Table not found', 'Unfortunately, there is no available table for your demands!')
                                avail.destroy()
                        #morfopoiisi para8urou me odigies gia tin epilogi trapeziou
                        Label(avail,text="Fill the boxes below!",fg='#fff',bg='#FF9C00',font=('Calibri(Body)',15)).place(x=170,y=50)
                        Label(avail,text="Indoors | Ground Floor",fg='#fff',bg='#FF9C00',font=('Calibri(Body)',12)).place(x=580,y=30)
                        Label(avail,text="Outdoors | First Floor",fg='#fff',bg='#FF9C00',font=('Calibri(Body)',12)).place(x=770,y=30)
                        Label(avail,text="Now choose one of the",fg='#fff',bg='#FF9C00',font=('Calibri(Body)',15)).place(x=170,y=220)
                        Label(avail,text="available tables and",fg='#fff',bg='#FF9C00',font=('Calibri(Body)',15)).place(x=170,y=250)
                        Label(avail,text="complete your reservation!",fg='#fff',bg='#FF9C00',font=('Calibri(Body)',15)).place(x=170,y=280)            
                        #entry name
                        Label(avail, text="Name:").place(x=200,y=100)
                        entry_name=tk.Entry(avail)
                        entry_name.place(x=200,y=120)

                        def validate_mobile_number(mobile_number): #elegxos format mobilenum
                            pattern = r'^\d{4}-\d{10}$'
                            return re.match(pattern, mobile_number)
                        #entry mobilenum
                        Label(avail, text="Mobile Number:").place(x=200,y=160)
                        entry_mobnum=tk.Entry(avail)
                        entry_mobnum.place(x=200,y=180)
                        entry_mobnum.insert(0,'xxxx-xxxxxxxxxx')
                        entry_mobnum.bind('<FocusIn>', lambda e: on_enter(e,entry_mobnum,'xxxx-xxxxxxxxxx'))
                        entry_mobnum.bind('<FocusOut>', lambda e: on_leave(e,entry_mobnum,'xxxx-xxxxxxxxxx'))

                        if diax: #an einai o diax dimiourgia how kai id_diax combo boxes
                            _how=["Face_to_face", "Phone"]
                            how_combo_box=ttk.Combobox(avail, values=_how)
                            how_combo_box.set("Select how")
                            how_combo_box.place(x=170, y=350)

                            _id_diax=["1111", "2222", "3333", "4444"]
                            id_diax_combo_box=ttk.Combobox(avail, values=_id_diax)
                            id_diax_combo_box.set("Select diax")
                            id_diax_combo_box.place(x=330, y=350)
                    else:
                        messagebox.showerror('Invalid', "Please fill all entries!")
                #dimiourgia neou window gia ta arxika stoixeia kai to imerologio
                res=tk.Toplevel(screen)
                res.title("Reservation Details")
                res.geometry('925x500+300+200')
                res.config(bg="#FF9C00")
                res.resizable(False,False)
                #entry number_of_people
                Label(res, text="Complete the reservation details", font=("Helvetica", 14)).place(x=300,y=50)
                Label(res, text="Number of People:").place(x=200, y=150)
                entry_num_people=tk.Entry(res)
                entry_num_people.place(x=200, y=170)
                #calendar me mi epileksimes imerominies p exoun perasei
                Label(res, text="Select Date:").place(x=400,y=150)
                cal=Calendar(res, selectmode="day", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day,
                                 mindate=datetime.now(), date_pattern="y-mm-dd")
                cal.place(x=400,y=180)
                #entry arrival time me dwthen to format
                Label(res, text="Arrival Time (HH:MM 00:00-24:00):").place(x=700,y=150)
                entry_arrival_time=tk.Entry(res)
                entry_arrival_time.place(x=700,y=170)
                #button gia ton elegxo gia dia8esimotita
                Button(res, text="Check for Availability", command=check_availability).place(x=750,y=420)

                res.mainloop()
############diaxeirisths------------------------------------------------------------------------------------------------------------------------------------------------------
            if username=="admin": #an sundethike o diaxeiristis Welcome Admin
                Label(screen,text="Welcome Admin!",fg='#fff',bg='#FF9C00',font=('Calibri(Body)',50,'bold')).place(x=40,y=10)

                def fetch_data(query, params=None): #5 show kati opote afti sundeetai me ti vasi kai pairnei ta dedomena analoga me to query ki an uparxoun parametrous tis vazeii alliws None
                    conn=sqlite3.connect("restaurant.db")
                    cursor=conn.cursor()
                    if params:
                        cursor.execute(query,params)
                    else:
                        cursor.execute(query)
                    data=cursor.fetchall()
                    conn.close()
                    return data #epistrefei ta data

                def display_treeview(title,columns,data): #treeview gia parathuro me ta dedomena pou pire apo ti vasi dinontai titlos stiles kai dedomena
                    prov=Tk()
                    prov.title(title)
                    tree=ttk.Treeview(prov)
                    tree["columns"]=columns

                    for col in columns:
                        tree.column(col, anchor="center", width=200)
                        tree.heading(col, text=col, anchor="center")

                    for row in data:
                        tree.insert("", "end", values=row)

                    tree.pack(expand=True, fill="both")
                    prov.mainloop()

                def provoli_all(): #provoli olwn twn kratisewn
                    query="SELECT * FROM KRATHSH"
                    data=fetch_data(query)
                    columns=["ID","Name","Mobile Number","Number of People","Arrival"]
                    display_treeview("KRATHSEIS all", columns, data)

                def provoli_today(): #provoli twn simerinwn kratisewn
                    today_date=datetime.now().strftime("%Y-%m-%d")
                    query="SELECT * FROM KRATHSH WHERE DATE(Arrival)=?"
                    data=fetch_data(query, (today_date,))
                    columns=["ID","Name","Mobile Number","Number of People","Arrival"]
                    display_treeview("KRATHSEIS today", columns, data)

                def see_reviews(): #provoli tvn reviews ta3inomimena apo to ipsilotero rate
                    query="SELECT Fname, Lname, Rate, Comment, ID_Krathshs \
                            FROM KRITIKH, GRAFEI, PELATHS \
                            WHERE Barcode = Barcode_Kritikhs AND ID_Xrhsth=ID_Pelath \
                            ORDER BY Rate DESC"
                    data=fetch_data(query)
                    columns=["First Name","Last Name","Rate","Comment","ID Krathshs"]
                    display_treeview("REVIEWS", columns, data)

                def see_customer_user(): #provoli pelatwn-xrhstwn
                    query="SELECT Fname, Lname, Username, MobileNum, Address_PostalCode, Address_Street, Address_Number \
                            FROM PELATHS, XRHSTHS WHERE ID = ID_Xrhsth ORDER BY ID"
                    data=fetch_data(query)
                    columns=["First Name", "Last Name", "Username", "Mobile Number", "Address PostalCode", "Address Street", "Address Number"]
                    display_treeview("USERS", columns, data)

                def see_customer_non(): #provoli pelatwn-oxi xrhstwn
                    query="SELECT Fname, Lname, MobileNum FROM PELATHS WHERE ID_Xrhsth IS NULL ORDER BY Lname"
                    data=fetch_data(query)
                    columns=["First Name", "Last Name", "Mobile Number"]
                    display_treeview("NON USERS", columns, data)
                

                id_rev_list=[] #arxikopoiisi listas me tis kratiseis pou ginontai checked
                    
                def search_reservation(): #anazitisi kratisis
                    #Toplevel window
                    search_window=Toplevel(screen)
                    search_window.title("Search Reservation")
                    search_window.geometry('925x500+300+200')
                    search_window.config(bg="#FF9C00")
                    search_window.resizable(False,False)

                    def search(): #psaxnei gia dwthen onoma kai tilefwno krathshs ta dedomena tis sugkekrimenis krathsh
                        name = entry_name_res.get()
                        mn = entry_mn_res.get()
                        today_date = datetime.now().strftime("%Y-%m-%d") #simerini arrival
                        #pairnei ta data tis kratisis apo ti vasi
                        conn=sqlite3.connect("restaurant.db")
                        cursor=conn.cursor()
                        cursor.execute("SELECT Name,MobileNumber,Num_of_People ,ID_Trapeziou FROM KRATHSH, AFORA WHERE Name=? AND ID=ID_Krathshs AND DATE(Arrival)=? AND MobileNumber=?",
                                       (name,today_date,mn))
                        data=cursor.fetchall()
                        conn.close()
                        #neo para8uro treeview gia na tin emfanisei
                        prov=Tk()
                        prov.title("USERS")
                        tree=ttk.Treeview(prov)
                        columns=["Name", "MobileNum", "Num_of_People", "ID_Trapeziou"]
                        tree["columns"]=columns

                        for col in columns:
                            tree.column(col, anchor="center", width=150)
                            tree.heading(col, text=col, anchor="center")

                        for row in data:
                            tree.insert("", "end", values=row)

                        tree.pack(expand=True, fill="both")

                    def check_blacklist(): #i kratisei molis epivevai8ei ginetai checked
                        name = entry_name_res.get()
                        mn = entry_mn_res.get()
                        today_date = datetime.now().strftime("%Y-%m-%d")
                        #vriskei to id tis kratisis pou molis ir8e
                        conn=sqlite3.connect("restaurant.db")
                        cursor=conn.cursor()
                        cursor.execute("SELECT ID FROM KRATHSH, AFORA WHERE Name=? AND ID=ID_Krathshs AND DATE(Arrival)=? AND MobileNumber=?",
                                       (name,today_date,mn))
                        id_rev=cursor.fetchone()
                        conn.close()

                        if id_rev and id_rev[0] not in id_rev_list: #elegxos an exei idi checked px na ir8an kapoioi pio meta kai na tin janaepsa3e na min xreiazetai na 8umatai an tin ekane checked tin 3anakanei xwris provlima
                            id_rev_list.append(id_rev[0]) #pros8iki id_kratisis sti lista
                            messagebox.showinfo('Checked', 'Sucessfully checked!')
                            search_window.destroy()
                            protimiseis=Toplevel(screen) #neo para8uro gia osous einai xrhstes gia  protimiseis allergies kai fora episkepsis
                            protimiseis.title("Search Reservation")
                            protimiseis.geometry('925x500+300+200')
                            protimiseis.config(bg="#FF9C00")
                            protimiseis.resizable(False,False)

                            #vriskei id_xrhsth p ekane tin kratisi
                            conn=sqlite3.connect("restaurant.db")
                            cursor=conn.cursor()
                            cursor.execute("SELECT ID_Xrhsth FROM KRATHSH, KANEI WHERE Name=? AND ID=ID_Krathshs AND DATE(Arrival)=?",
                                           (name,today_date))
                            _id=cursor.fetchone()
                            conn.close()

                            if _id[0]!=0: #an einai ontws xristis k oxi o diax p exei kanei tin kratisi
                                conn=sqlite3.connect("restaurant.db")
                                cursor=conn.cursor()
                                #upologizei tis fores episkepsis
                                cursor.execute("SELECT count(*) FROM KANEI, KRATHSH WHERE ID_Xrhsth=? AND ID_Krathshs=ID AND DATE(Arrival)<=?",
                                               (_id[0],today_date))
                                visits=cursor.fetchone()
                                conn.close()
                                visits_str = str(visits[0])
                                Label(protimiseis, text="Customer visited restaurant "+visits_str+" times!").place(x=100,y=50) #tis vazei sto para8uro

                                #protimiseis xrhsth                      
                                conn=sqlite3.connect("restaurant.db")
                                cursor=conn.cursor()
                                cursor.execute("SELECT Favorite_Dessert,Favorite_Drink FROM KRATHSH, KANEI, PROTIMHSEIS WHERE Name=? AND ID=ID_Krathshs AND DATE(Arrival)=? AND ID_Xrhsth=ID_Pelath",
                                               (name,today_date))
                                data=cursor.fetchall()
                                conn.close()
                                #tis vazei sto para8uro
                                Label(protimiseis, text="Customers favorite dessert is "+data[0][0]+" and favorite drink is "+data[0][1]).place(x=100,y=150)
                                
                                #allergies
                                conn=sqlite3.connect("restaurant.db")
                                cursor=conn.cursor()
                                cursor.execute("SELECT Substance FROM ALLERGIA_PROTIMHSEIS WHERE ID_Pelath=?",
                                               (_id))
                                aller=cursor.fetchall()
                                conn.close()
                                #tis vazei sto para8uro
                                Label(protimiseis, text="Customer has allergies in ").place(x=100,y=250)
                                for i,item in enumerate(aller):
                                    Label(protimiseis, text=item).place(x=250+50*i,y=250)
                                #messagebox gia antistoixes periptwsei
                            else:
                                messagebox.showinfo("Non User", "This customer is not a user of App")
                        else:
                            messagebox.showerror("Error", "Reservation has already been checked!")

                    #morfopoiisi para8urou
                    #entry name kratisis
                    Label(search_window, text="Insert Name of Reservation :").place(x=200,y=100)
                    entry_name_res=tk.Entry(search_window, width=25)
                    entry_name_res.place(x=200,y=120)
                    #entry mobnum kratisis (gia mi xrhste voithaei na uparxei kai o ari8mos 3exwrizoun pateras gios me idio lastname
                    Label(search_window, text="Insert Mobile Number of Reservation :").place(x=400,y=100)
                    entry_mn_res=tk.Entry(search_window, width=25)
                    entry_mn_res.place(x=400,y=120)
                    #prwta epivevaiwnei tin kratisi me ta stoixeia p tou emfanizei i search kai meta tin kanei checked oti ir8e gia na mi mpei blacklist
                    #button pou kale tin search
                    Button(search_window,width=10,bg='black',fg='white',text="Search",border=5,command=search).place(x=225,y=150)
                    #button pou kalei tin check_blacklisted
                    Button(search_window,width=18,bg='black',fg='white',text="Check (no blacklisted)",border=5,command=check_blacklist).place(x=225,y=300)

                    search_window.mainloop()

                def get_blacklisted(): #blacklist function patietai sto telos tis imeras
                    conn=sqlite3.connect("restaurant.db")
                    cursor=conn.cursor()
                    today_date=datetime.now().strftime("%Y-%m-%d")
                    #print("id_rev_list:", id_rev_list)
                    #print("today_date:", today_date)
                    #pairnei oles tis simerines kratiseis 
                    cursor.execute("SELECT ID FROM KRATHSH WHERE date(Arrival)=?",
                                        (today_date,))
                    result=cursor.fetchall()
                    conn.close()
                    #print("result", result)
                    result_ids = [item[0] for item in result] 
                    blisted=[item for item in result_ids if item not in id_rev_list] #elegxos vazei oses kratiseis itan na er8oun alla den eginan checked stin blisted
                    #print("items in result not in id_rev_list", blisted)
                    if blisted: 
                        for _idblack in blisted: #gia ka8e blacklisted id_kratisis
                            try:
                                _idblack=int(_idblack)
                                #print("idb", _idblack)
                                #vriskei to id_xrhsth pou tin ekane
                                conn = sqlite3.connect("restaurant.db")
                                cursor = conn.cursor()
                                cursor.execute("SELECT ID_Xrhsth FROM KANEI WHERE ID_Krathshs=?",
                                                (_idblack,))
                                xblack=cursor.fetchone()
                                conn.close()
                                #print("xblack", xblack[0])
                                conn = sqlite3.connect("restaurant.db")
                                cursor = conn.cursor()
                                #vriskei onoma kai til krathshs gia tin periptwsi p egine mesw diax
                                cursor.execute("SELECT Name,MobileNumber FROM KRATHSH WHERE ID=?",
                                                    (_idblack,))
                                info=cursor.fetchone()
                                conn.close()

                                if xblack[0]!=0: #an einai xristis
                                    conn = sqlite3.connect("restaurant.db")
                                    cursor = conn.cursor()
                                    #update data kai ton vazei blacklisted mesw ID_Xrhsth
                                    cursor.execute("UPDATE PELATHS SET blacklisted = 1 WHERE ID_Xrhsth=?", (xblack[0],))
                                    conn.commit()
                                    conn.close()

                                else: #an egine apo ton diax
                                    conn = sqlite3.connect("restaurant.db")
                                    cursor = conn.cursor()
                                    #update data kai ton vazei blacklisted mesw Lname, MobileNum
                                    cursor.execute("UPDATE PELATHS SET blacklisted = 1 WHERE Lname=? AND MobileNum=?",
                                                   (info[0],info[1]))
                                    conn.commit()
                                    conn.close()
                                messagebox.showinfo("Blacklisted", "The customers who did not show up have been blacklisted!")
                                    
                            except sqlite3.Error as e:
                                print(f"Error updating ID {_idblack}: {e}")
                    else:
                        messagebox.showinfo("NO BLACKLIST","All customers showed up!")
                    

                def add_customer(): #prosthiki neou pelati pou den einai xrhsths sti vasi
                    #Toplevel window
                    add=Toplevel(screen)
                    add.title("Add Customer")
                    add.geometry('925x500+300+200')
                    add.config(bg="#FF9C00")
                    add.resizable(False,False)

                    def ins_add_customer(): #eisagei neo pelath oxi xrhsth sti vasi
                        fnamep=pname.get()
                        lnamep=plname.get()
                        mnump=pmnum.get()

                        if fnamep!="" and lnamep!="" and mnump!="": #elegxos an den einai kena to fromat den xreiazetai na elegx8ei gt o diax 3erei ti diadikasia pws na to valei
                            #eisagei sti vasei neo pelati ston PELATHS
                            conn=sqlite3.connect("restaurant.db")
                            cursor=conn.cursor()
                            cursor.execute('''INSERT INTO PELATHS (Fname,Lname,MobileNum) VALUES(?,?,?)''',
                                                            (fnamep,lnamep,mnump))
                            conn.commit()
                            conn.close()
                            messagebox.showinfo('Inserted', 'Sucessfully insertion of new Customer in database.')
                            add.destroy()
                            #antistoixo messagebox gia error
                        else:
                            messagebox.showerror("Error", "Must fill all the entries")
                    
                    #First Name entry
                    Label(add, text="First Name").place(x=200,y=100)
                    pname=tk.Entry(add, width=15)
                    pname.place(x=200,y=120)
                    #Last Name entry
                    Label(add, text="Last Name").place(x=350,y=100)
                    plname=tk.Entry(add, width=15)
                    plname.place(x=350,y=120)
                    #Mobile Number entry
                    Label(add, text="Mobile Number (xxxx-xxxxxxxxxx)").place(x=500,y=100)
                    pmnum=tk.Entry(add, width=20)
                    pmnum.place(x=500,y=120)
                    #button pou kalei tin ins_add_customer
                    Button(add, width=30,bg='black',fg='white',text='Insert non user into Database', border=5,command=ins_add_customer).place(x=600,y=200)
                
                #buttons gia oles tis dunatotites tou diaxeiristi pou perigrafikan parapanw
                Button(screen,width=32,pady=7,text='Search Reservation',bg='black',fg='white',border=0,command=search_reservation).place(x=140,y=150)
                Button(screen,width=32,pady=7,text='Make a Reservation',bg='black',fg='white',border=0,command=lambda diax=1: make_reservation(diax)).place(x=140,y=200)
                Button(screen,width=32,pady=7,text='See Reservations (all)',bg='black',fg='white',border=0,command=provoli_all).place(x=140,y=250)
                Button(screen,width=32,pady=7,text='See Reservations (today)',bg='black',fg='white',border=0,command=provoli_today).place(x=140,y=300)
                Button(screen,width=32,pady=7,text='Add Customer (non-user)',bg='black',fg='white',border=0,command=add_customer).place(x=540,y=150)
                Button(screen,width=32,pady=7,text='See Customers (non-user)',bg='black',fg='white',border=0,command=see_customer_non).place(x=540,y=200)
                Button(screen,width=32,pady=7,text='See Customers (user)',bg='black',fg='white',border=0,command=see_customer_user).place(x=540,y=250)
                Button(screen,width=32,pady=7,text='See Reviews',bg='black',fg='white',border=0,command=see_reviews).place(x=540,y=300)
                Button(screen,width=32,pady=7,text='Blacklist',bg='red',fg='white',border=0,command=get_blacklisted).place(x=700,y=100)

#######xrhsths------------------------------------------------------------------------------------------------------------------------------------------------------                        
            else: #an den sundethike o diax, tote sundethike kapoios xrhsths Welcome Customer
                Label(screen,text="Welcome Customer!",fg='#fff',bg='#FF9C00',font=('Calibri(Body)',50,'bold')).place(x=40,y=10)

                def make_review(): #afinei kritiki
                    today_date = datetime.now().strftime("%Y-%m-%d") #simerini date gia na min emfanistoun kratiseis p den exoun lavei xwra akomh
                    #pairnei dedomena twn krathsewn apo ti vasi gia tis kratiseis p exoun lavei xwra idi
                    conn=sqlite3.connect("restaurant.db")
                    cursor=conn.cursor()
                    cursor.execute("SELECT Name, KR.Arrival FROM XRHSTHS as X, KANEI as K, KRATHSH as KR WHERE Username=? AND X.ID=K.ID_Xrhsth AND K.ID_Krathshs=KR.ID AND DATE(KR.Arrival)<?",
                                    (username,today_date))
                    data=cursor.fetchall()
                    conn.close()
                    #neo parathuro deixnei afta ta dedomena me treeview
                    rev=tk.Toplevel(screen)
                    rev.title("Review")
                    rev.geometry('925x500+300+200')
                    rev.config(bg="#FF9C00")
                    rev.resizable(False,False)

                    tree=ttk.Treeview(rev)
                    columns=["Name","Arrival"]
                    tree["columns"]=columns

                    for col in columns:
                        tree.column(col, anchor="center", width=100)
                        tree.heading(col, text=col, anchor="center")

                    for row in data:
                        tree.insert("", "end", values=row)

                    tree.pack(expand=True, fill="both")
                    

                    def vathmos(i_krat): #exei epilegx8ei h _i_krathsh gia review
                        #print("i_krat",i_krat)
                        #vriskei tis kratiseis tou xrhsth pou exoun idi ginei reviewed
                        conn0=sqlite3.connect("restaurant.db")
                        cursor0=conn0.cursor()
                        cursor0.execute("SELECT ID_Krathshs FROM GRAFEI,KRITIKH WHERE ID_Pelath=? AND Barcode_Kritikhs=Barcode", (x_id[0],))
                        reviewed_kratiseis=cursor0.fetchall()
                        conn0.close()
                        #pairnei to id_krat p xei kanei o xrhsths
                        conn0=sqlite3.connect("restaurant.db")
                        cursor0=conn0.cursor()
                        cursor0.execute("SELECT ID_Krathshs FROM KANEI WHERE ID_Xrhsth=?", (x_id[0],))
                        kratiseis=cursor0.fetchall()
                        conn0.close()
                        #print("krat=", kratiseis)
                        #print("rev krat=", reviewed_kratiseis)
                        #neo para8uro Toplevel
                        v=Toplevel(rev)
                        v.title("Review")
                        v.geometry('925x500+300+200')
                        v.config(bg="#FF9C00")
                        v.resizable(False,False)

                        def done(star,i): #edw kataxwreitai to rate=star gia ti i_kratisi tou xrhsth
                            #neo para8uro gia pros8iki comment
                            comm=Toplevel(v)
                            comm.title("Review")
                            comm.geometry('925x500+300+200')
                            comm.config(bg="#FF9C00")
                            comm.resizable(False,False)                          

                            def submit_comment(star,i): #edw eisagei tin review sti vasi
                                comment=entry_comm.get() #pairnei to comment
                                #print("len",len(kratiseis))
                                #print("star=",star)
                                #print("i=",i)
                                #enimerwnei an exei ginei idi kritiki gia tin sugkekrimeni krathsh
                                if 1 <= i <= len(kratiseis) and any(k[0] == kratiseis[i-1][0] for k in reviewed_kratiseis):
                                    messagebox.showerror("Error", "Already reviewed!")
                                else: #an den exei ginei
                                    if 1 <= i <= len(kratiseis):
                                        id_k = int(kratiseis[i-1][0]) #painrei to id_krat
                                    else:
                                        messagebox.showerror("Error", "Invalid index for kratiseis!")
                                    #eisagei ta dedomena sti vasi stin KRITIKH
                                    conn=sqlite3.connect("restaurant.db")
                                    cursor=conn.cursor()
                                    cursor.execute("INSERT INTO KRITIKH (Rate,ID_Krathshs,Comment) VALUES (?,?,?)",
                                                    (star,id_k,comment))
                                    conn.commit()
                                    conn.close()
                                    #pairnei to barcode tis sugkekrimenis kritikis
                                    conn=sqlite3.connect("restaurant.db")
                                    cursor=conn.cursor()
                                    cursor.execute("SELECT max(Barcode) FROM KRITIKH")
                                    barcode=cursor.fetchone()
                                    conn.commit()
                                    conn.close()
                                    #eisagei ta dedomena sti vasi sto GRAFEI
                                    conn=sqlite3.connect("restaurant.db")
                                    cursor=conn.cursor()
                                    cursor.execute("INSERT INTO GRAFEI (ID_Pelath,Barcode_Kritikhs) VALUES (?,?)",
                                                    (x_id[0],barcode[0]))
                                    conn.commit()
                                    conn.close()
                                    #comment entry
                                    entry_comm.delete(0,tk.END)
                                    messagebox.showinfo('Successful Reviw', 'Thank you for your review!')
                                    comm.destroy()
                                    v.destroy()
                                    rev.destroy()
                            #morfopoiisi para8urou gia comment
                            Label(comm, text="Leave a comment, if you want!").place(x=200,y=100)
                            entry_comm=Entry(comm,width=50)
                            entry_comm.place(x=200,y=150)
                            #button Finish Review kalei tin submit_comment(star,i)
                            Button(comm, text="Finish Review", command=lambda star=star, i=i: submit_comment(star,i)).place(x=200,y=250)

                        #morfopoiisi vathmologias para8urou
                        for j in range (1,6): #vazei ta 5 button gia ta rates 1,2,3,4,5 pou kaloun tin done(star,i)
                            Button(v,width=2, text=str(j), fg="black",bg='yellow',border=5, command=lambda star=j, i=i_krat: done(star,i)).place(x=100,y=40+j*60)

                        img_star = PhotoImage(file='star.png') #eikona asteriou
                        #dipla apo ka8e rate button vazei ton antistoixo ari8mo asteriwn
                        Label(v,image=img_star,border=0,bg='white').place(x=150,y=100)
                        for j in range (1,3):
                            Label(v,image=img_star,border=0,bg='white').place(x=110+j*40,y=160)
                        for j in range (1,4):
                            Label(v,image=img_star,border=0,bg='white').place(x=110+j*40,y=220)
                        for j in range (1,5):
                            Label(v,image=img_star,border=0,bg='white').place(x=110+j*40,y=280)
                        for j in range (1,6):
                            Label(v,image=img_star,border=0,bg='white').place(x=110+j*40,y=340)
                            
                        v.mainloop()
                        
                    #pairnei to id tou xrhsth p xei sunde8ei
                    conn0=sqlite3.connect("restaurant.db")
                    cursor0=conn0.cursor()
                    cursor0.execute("SELECT ID FROM XRHSTHS WHERE Username=?", (username,))
                    x_id=cursor0.fetchone()
                    conn0.close()
                    #metraei poses krathseis exei kanei o sugkekrimenos xrhsths
                    conn0=sqlite3.connect("restaurant.db")
                    cursor0=conn0.cursor()
                    cursor0.execute("SELECT count(ID_Krathshs) FROM KANEI, KRATHSH WHERE ID_Xrhsth=? AND ID_Krathshs=ID AND DATE(Arrival) < ? ",
                                    (x_id[0], today_date))
                    count=cursor0.fetchone()
                    conn0.close()
                    #print("count=", count[0])

                    if count[0]: #an uparxoun kratiseis p xoun proigithei
                        Label(rev, text="Choose which visit to review").place(x=200,y=1)
                        for i in range (1,count[0]+1): #dimiourgia button pou kalei tin vathmos(i) dipla apo ka8e kratisi
                            Button(rev, text="Reservation"+str(i), command=lambda i=i: vathmos(i)).place(x=200,y=1+i*20)
                    else: #alliws messagebox oti den uparxoun akoma kratiseis gia na ginei review
                        messagebox.showinfo('No Reservation', 'No reservation to review yet!')
                        


                def provoli(): #provoli kratisewn tou xrhsth (istoriko)
                    conn=sqlite3.connect("restaurant.db")
                    cursor=conn.cursor()
                    #pairnei ta dedomena twn krathsewn tou sugkekrimenou xrhsth
                    cursor.execute("SELECT KR.ID, Name, MobileNumber, Num_of_People, KR.Arrival FROM XRHSTHS as X, KANEI as K, KRATHSH as KR WHERE Username=? AND X.ID=K.ID_Xrhsth AND K.ID_Krathshs=KR.ID",
                                    (username,))
                    data=cursor.fetchall()
                    conn.close()
                    #neo para8uro treeview pou deixnei ta data
                    prov=Tk()
                    prov.title("KRATHSEIS")
                    tree=ttk.Treeview(prov)
                    columns=["ID", "Name", "MobileNumber", "NumberofPeople", "Arrival"]
                    tree["columns"]=columns

                    for col in columns:
                        tree.column(col, anchor="center", width=150)
                        tree.heading(col, text=col, anchor="center")

                    for row in data:
                        tree.insert("", "end", values=row)

                    tree.pack(expand=True, fill="both")

                    prov.mainloop()

                #buttons gia tin dunatotites tpu xrhsth pou perigrafikan parapanw
                Button(screen,width=32,pady=7,text='Make a Reservation',bg='black',fg='white',border=0,command=lambda diax=0: make_reservation(diax)).place(x=540,y=210)
                Button(screen,width=32,pady=7,text='Make a Reviw',bg='black',fg='white',border=0,command=make_review).place(x=540,y=260)
                Button(screen,width=32,pady=7,text='Show Reservation',bg='black',fg='white',border=0,command=provoli).place(x=540,y=310)

                screen.mainloop()
            #antistoixa messagebox gia errors
        else:
            messagebox.showerror("Invalid","Incorrect password")
    else:
        messagebox.showerror("Invalid","Invaled username")
#username entry
user = Entry(frame,width=25,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=550,y=100)
user.insert(0,'Username')
user.bind('<FocusIn>', lambda e: on_enter(e,user,'Username'))
user.bind('<FocusOut>', lambda e: on_leave(e,user,'Username'))
Frame(frame,width=203,heigh=2,bg='black').place(x=550,y=124)
#password entry
code = Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=550,y=160)
code.insert(0,'Password')
code.bind('<FocusIn>', lambda e: on_enter(e,code,'Password'))
code.bind('<FocusOut>', lambda e: on_leave(e,code,'Password'))
Frame(frame,width=206,heigh=2,bg='black').place(x=550,y=184)

#############################################################################################################################################################
#epilogi signup

def signup():
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg="#fff")
    window.resizable(False,False)

    def validate_mobile_number(mobile_number): #sunartisi pou ellegxei to format tou mobile number
        pattern = r'^\d{4}-\d{10}$'
        return re.match(pattern, mobile_number)
    
    def signUp(): #kaleitai patwntas to next (elegxos an o xristis uparxei id kai an password=confirm password)
        username=user.get()
        password=code.get()
        conf_password=conf_code.get()

        if username!="Username":
            conn3=sqlite3.connect("restaurant.db")
            c3=conn3.cursor()
            c3.execute('''SELECT Username from XRHSTHS''')
            users=c3.fetchall()
            conn3.close()

            if (username,) not in users: #elegxos an uparxei idi o xristis
                if password==conf_password: #elegxos an tairiazoun oi duo passwords
                    window.destroy()
                    screen1=Tk()
                    screen1.title("SignUp")
                    screen1.geometry('925x500+300+200')
                    screen1.config(bg="#FF9C00")
                    Label(screen1,text="Please complete the form below",bg='#FF9C00',font=('Microsoft YaHei UI Light',23,'bold')).place(x=220,y=10)

                    #### Fname Entry
                    fname = Entry(screen1,width=25,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',11))
                    fname.place(x=350,y=100)
                    fname.insert(0,'First Name')
                    fname.bind('<FocusIn>', lambda e: on_enter(e,fname,'First Name'))
                    fname.bind('<FocusOut>', lambda e: on_leave(e,fname,'First Name'))
                    Frame(screen1,width=203,heigh=2,bg='black').place(x=350,y=124)

                    #### Lname Entry
                    lname = Entry(screen1,width=25,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',11))
                    lname.place(x=350,y=180)
                    lname.insert(0,'Last Name')
                    lname.bind('<FocusIn>', lambda e: on_enter(e,lname,'Last Name'))
                    lname.bind('<FocusOut>', lambda e: on_leave(e,lname,'Last Name'))
                    Frame(screen1,width=203,heigh=2,bg='black').place(x=350,y=204)

                    #### MobileNum Entry
                    mn = Entry(screen1,width=36,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',11))
                    mn.place(x=320,y=260)
                    mn.insert(0,'Mobile Number (format 0000-0000000000)')
                    mn.bind('<FocusIn>', lambda e: on_enter(e,mn,'Mobile Number (format 0000-0000000000)'))
                    mn.bind('<FocusOut>', lambda e: on_leave(e,mn,'Mobile Number (format 0000-0000000000)'))

                    Frame(screen1,width=290,heigh=2,bg='black').place(x=321,y=284)

                    #### Address Entries
                    ad_num = Entry(screen1,width=8,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',11))
                    ad_num.place(x=250,y=340)
                    ad_num.insert(0,'Number')
                    ad_num.bind('<FocusIn>', lambda e: on_enter(e,ad_num,'Number'))
                    ad_num.bind('<FocusOut>', lambda e: on_leave(e,ad_num,'Number'))
                    Frame(screen1,width=66,heigh=2,bg='black').place(x=251,y=364)

                    ad_st = Entry(screen1,width=25,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',11))
                    ad_st.place(x=350,y=340)
                    ad_st.insert(0,'Street')
                    ad_st.bind('<FocusIn>', lambda e: on_enter(e,ad_st,'Street'))
                    ad_st.bind('<FocusOut>', lambda e: on_leave(e,ad_st,'Street'))
                    Frame(screen1,width=202,heigh=2,bg='black').place(x=351,y=364)
                    
                    ad_code = Entry(screen1,width=15,fg='black',border=1,bg='white',font=('Microsoft YaHei UI Light',11))
                    ad_code.place(x=600,y=340)
                    ad_code.insert(0,'PostCode')
                    ad_code.bind('<FocusIn>', lambda e: on_enter(e,ad_code,'PostCode'))
                    ad_code.bind('<FocusOut>', lambda e: on_leave(e,ad_code,'PostCode'))
                    Frame(screen1,width=123,heigh=2,bg='black').place(x=601,y=364)

                    def insData(): #pairnei ta fname,lname,mobilenumber,address
                        Fname=fname.get()
                        Lname=lname.get()
                        MobileNum=mn.get()
                        Ad_num=ad_num.get()
                        Ad_code=ad_code.get()
                        Ad_st=ad_st.get()

                        #elegxei an einai valid ta stoixeia ki oxi kena
                        if Fname!="First Name" and Lname!="Last Name" and MobileNum!="Mobile Number" and Ad_num!="Number" and Ad_code!="PostCode" and Ad_st!="Street":
                            if validate_mobile_number(MobileNum): #elegxei format tou mobilenum
                                #eisagei sti vasi username,password sto xristi
                                conn2=sqlite3.connect("restaurant.db")
                                conn2.execute('''INSERT INTO XRHSTHS (Username, Password) VALUES(?,?)''', (username,password))
                                conn2.commit()
                                conn2.close()
                
                                #pairnei to id xrhsth gia na eisagei ta dedomena gi afton ton xristi ston pelati
                                conn1=sqlite3.connect("restaurant.db")
                                c=conn1.cursor()
                                c.execute('''select ID from XRHSTHS WHERE Username=?''', (username,))
                                data=c.fetchone()
                                conn1.close()
                                #eisagei ta dedomena tou xrhsth ston pelath
                                conn2=sqlite3.connect("restaurant.db")
                                conn2.execute('''INSERT INTO PELATHS (ID_Xrhsth,Fname,Lname,MobileNum,Address_Number,Address_PostalCode, Address_Street) VALUES(?,?,?,?,?,?,?)''',
                                              (data[0],Fname,Lname,MobileNum,Ad_num,Ad_code,Ad_st))
                                conn2.commit()
                                conn2.close()

                                #neo parathuro gia epilogi protimisewn
                                screen1.destroy()
                                screen2=Tk()
                                screen2.title("Preferences")
                                screen2.geometry('925x500+300+200')
                                screen2.config(bg="#FF9C00")

                                Label(screen2,text="Let's get to know you better",bg='#FF9C00',font=('Microsoft YaHei UI Light',23,'bold')).place(x=220,y=10)

                                def save_preferences(): #pairnei to agapimeno poto kai gluko kai tis allergies kai ta eisagei sti vasi
                                    drink=drink_combo_box.get()
                                    dessert=dessert_combo_box.get()
                                    #print("Selected Dessert: ", dessert)
                                    #print(f"Selected Drink: ", drink)
                                    
                                    if drink=="Select a drink" or dessert=="Select a dessert": #elegxos an exoun ontws epileksei apo ta boxes
                                        messagebox.showerror("Missing details", "Please select your favorite drink and dessert")

                                    else:#an ola kala tote ta eisagei sti vasi stis PROTIMHSEIS
                                        conn3=sqlite3.connect("restaurant.db")
                                        conn3.execute('''INSERT INTO PROTIMHSEIS (Favorite_Dessert, Favorite_Drink, ID_Pelath) VALUES(?,?,?)''', (dessert,drink, data[0]))
                                        conn3.commit()
                                        conn3.close()
                                    
                                    
                                        allergies_str=allergies_entry.get()
                                        if allergies_str=="Enter allergies (if any)":#an kamia allergia vazei None
                                            conn6 = sqlite3.connect("restaurant.db")
                                            conn6.execute('''INSERT INTO ALLERGIA_PROTIMHSEIS (Substance, ID_Pelath) VALUES(?, ?)''', ("None", data[0]))
                                            conn6.commit()
                                            conn6.close()

                                            
                                        else:#alliws xwrizei tis pollaples allergies (me space h komma) kai ta kataxwrei ston pinaka ALLERGIS_PROTIMHSEIS ws pleiotima
                                            allergies=re.split(r'[,\s]+', allergies_str)
                                            allergies=[value for value in allergies if value]
                                            conn4=sqlite3.connect("restaurant.db")
                                            for allergy in allergies:
                                                conn4.execute('''INSERT INTO ALLERGIA_PROTIMHSEIS (Substance, ID_Pelath) VALUES(?,?)''', (allergy, data[0]))
                                            conn4.commit()
                                            conn4.close()
      
                                        messagebox.showinfo('Signup', 'Sucessfully sign up')
                                        screen2.destroy()  

                                    
                                #combo box gia agapimeno poto
                                drinks=["Select a drink", "Wine", "Beer", "Tea", "Champagne"]
                                drink_combo_box=ttk.Combobox(screen2, values=drinks)
                                drink_combo_box.set("Select a drink")
                                drink_combo_box.place(x=120, y=100)
                                #combo box gia agapimeno gluko
                                desserts = ["Select a dessert", "Cake", "Ice Cream", "Brownies", "Cheesecake"]
                                dessert_combo_box=ttk.Combobox(screen2, values=desserts)
                                dessert_combo_box.set("Select a dessert")
                                dessert_combo_box.place(x=380, y=100)

                                #entry gia na grapsei tis allergies tou
                                allergies_entry=Entry(screen2)
                                allergies_entry.place(x=120, y=250)
                                allergies_entry.insert(0, "Enter allergies (if any)")
                                allergies_entry.bind('<FocusIn>', lambda e: on_enter(e,allergies_entry,'Enter allergies (if any)'))
                                allergies_entry.bind('<FocusOut>', lambda e: on_leave(e,allergies_entry,'Enter allergies (if any)'))
                                Button(screen2,width=39,pady=7,text='Save Preferences',bg='white',fg='#FF9C00',border=0,command=save_preferences).place(x=380,y=250)

                                screen2.mainloop()
                                #antistoixa errors gia ka8e periptwsi p enimerwnoun ton xristi me messageboxes
                            else:
                                messagebox.showerror('Invalid', "Invalid mobile number format. Please enter a valid number in the format 0000-0000000000.")
                        else:
                            messagebox.showerror('Invalid', "Please fill all entries!")
                        
                    Button(screen1,width=28,pady=7,text='SignUp',bg='#fff',fg='black',border=0,command=insData).place(x=350,y=420)
                    screen1.mainloop()

                elif password!=conf_password:
                    messagebox.showerror('Invalid', "Both password should match")

            else:
                messagebox.showerror('Invalid', "This user already exists")

        else:
            messagebox.showerror('Invalid', "Missing Username")

    #arxiko window signup morfopoiisi
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)
    frame=Frame(window,width=350,height=390,bg='white')
    frame.place(x=480,y=50)
    heading=Label(frame,text="Sign up",fg='#FF9C00',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)
    #username entry
    user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind("<FocusIn>",lambda e: on_enter(e,user,'Username'))
    user.bind("<FocusOut>",lambda e: on_leave(e,user,'Username'))
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    #password entry
    code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind("<FocusIn>",lambda e: on_enter(e,code,'Password'))
    code.bind("<FocusOut>",lambda e: on_leave(e,code,'Password'))
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    #confirm password entry
    conf_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    conf_code.place(x=30,y=220)
    conf_code.insert(0,'Confirm Password')
    conf_code.bind("<FocusIn>",lambda e: on_enter(e,conf_code,'Confirm Password'))
    conf_code.bind("<FocusOut>",lambda e: on_leave(e,conf_code,'Confirm Password'))
    #button next
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
    Button(frame,width=39,pady=7,text='Next',bg='#FF9C00',fg='white',border=0,command=signUp).place(x=35,y=280)
    window.mainloop()
#arxiko window morfopoisi SignIn kai SignUp 
Button(frame,width=32,pady=7,text='Sign in',bg='#FF9C00',fg='white',border=0,command=signin).place(x=540,y=220)
label=Label(frame,text="Don't have an account?", fg='black',bg='white', font=('Microsoft YaHei UI Light',9))
label.place(x=550,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#FF9C00',command=signup) #allagi kersora se xeraki opws stis efarmoges
sign_up.place(x=700,y=270)

root.mainloop()
