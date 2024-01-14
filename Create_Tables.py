import sqlite3

#Σύνδεση με τη Βάση Δεδομένων
conn = sqlite3.connect('DB_5000.db') #να προσαρμοστεί αν χρειάζεται
cursor = conn.cursor()

# Δημιουργια πινάκων
create_tables_query = """
CREATE TABLE IF NOT EXISTS "XRHSTHS" (
	"ID" 	   INTEGER			PRIMARY KEY AUTOINCREMENT,
	"Username" VARCHAR(20)		NOT NULL,
	"Password" VARCHAR(20)		NOT NULL
);

CREATE TABLE IF NOT EXISTS "DIAXEIRISTHS" (
	"ID_Employee" INTEGER		NOT NULL,
	"Start_shift" datetime	    NOT NULL	DEFAULT	'0000-00-00 00:00:00',
	"End_shift"   datetime		NOT NULL	DEFAULT	'0000-00-00 00:00:00',
	"ID_Xrhsth"   INTEGER		NOT NULL,
	PRIMARY KEY ("ID_Employee"),
	FOREIGN KEY ("ID_Xrhsth") REFERENCES "XRHSTHS" ("ID")
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "PELATHS" (
	"ID_Xrhsth" INTEGER			DEFAULT NULL,
	"Fname" 	VARCHAR(20)		NOT	NULL,
	"Lname" 	VARCHAR(20)		NOT	NULL,
	"MobileNum" VARCHAR(15)		NOT	NULL	DEFAULT '0000-0000000000',
	"Address_PostalCode" INTEGER		    DEFAULT NULL,
	"Address_Street" 	 VARCHAR(50)		DEFAULT NULL,
	"Address_Number" 	 INTEGER			DEFAULT NULL,
	"Blacklisted" 	BOOLEAN	    NOT NULL	DEFAULT '0',
	PRIMARY KEY ("Fname","Lname","MobileNum")
	FOREIGN KEY ("ID_Xrhsth") REFERENCES "XRHSTHS" ("ID")
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "XWROS" (
	"ID_Department" INTEGER		NOT NULL,
	"Indoors"       BOOLEAN	    NOT NULL,
	"Floor"         INTEGER		NOT NULL,
	PRIMARY KEY ("ID_Department")
);

CREATE TABLE IF NOT EXISTS "TRAPEZI" (
	"ID"            INTEGER		NOT NULL,
	"Capacity" 		INTEGER		NOT NULL,
	"Position_X"    INTEGER							NOT NULL,
	"Position_Y"    INTEGER							NOT NULL,
	"ID_Xwrou"      INTEGER							NOT NULL,
	PRIMARY KEY ("ID"),
	FOREIGN KEY ("ID_Xwrou") REFERENCES "XWROS" ("ID_Department")
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "KRATHSH" (
	"ID"         INTEGER			PRIMARY KEY AUTOINCREMENT,
	"Name"       VARCHAR(40)		NOT NULL ,
	"MobileNumber" VARCHAR(15)		NOT NULL	DEFAULT '0000-0000000000',
	"Num_of_People" INTEGER			NOT NULL,
	"Arrival"      datetime		    NOT NULL	DEFAULT	(strftime('%Y-%m-%d %H:%M:%S', 'now'))
);

CREATE TABLE IF NOT EXISTS "AFORA" (
	"ID_Krathshs"	INTEGER			NOT NULL,
	"ID_Trapeziou"	INTEGER			NOT NULL,
	PRIMARY KEY ("ID_Krathshs", "ID_Trapeziou"),
	FOREIGN KEY ("ID_Krathshs") REFERENCES "KRATHSH" ("ID")
			ON UPDATE CASCADE
			ON DELETE CASCADE,
	FOREIGN KEY ("ID_Trapeziou") REFERENCES "TRAPEZI" ("ID")
			ON UPDATE CASCADE
			ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "KRITIKH" (
	"Barcode" INTEGER								PRIMARY KEY AUTOINCREMENT,
	"Rate"    INTEGER		NOT NULL,
	"ID_Krathshs" INTEGER							NOT NULL,
	"Comment"     VARCHAR(255)						DEFAULT NULL,
	FOREIGN KEY ("ID_Krathshs") REFERENCES "KRATHSH" ("ID")
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "PROTIMHSEIS" (
	"Favorite_Dessert"  VARCHAR(20) 	NOT NULL,
	"Favorite_Drink" VARCHAR(20) 	NOT NULL,
	"ID_Pelath"      INTEGER		NOT NULL,
	PRIMARY KEY ("ID_Pelath"),
	FOREIGN KEY ("ID_Pelath") REFERENCES "PELATHS" ("ID_Xrhsth")
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "ALLERGIA_PROTIMHSEIS" (
	"Substance" VARCHAR(20) 	NOT NULL,
	"ID_Pelath" INTEGER		    NOT NULL,
	PRIMARY KEY ("Substance", "ID_Pelath"),
	FOREIGN KEY ("ID_Pelath") REFERENCES "PROTIMHSEIS" ("ID_Pelath")
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "EPIKOINWNEI" (
	"How" TEXT CHECK(How IN ('Phone', 'Face_to_face'))	NOT NULL,
	"ID_Diaxeiristh" INTEGER							NOT NULL,
	"Fname_Pelath"   VARCHAR(20)		                NOT	NULL,
	"Lname_Pelath"   VARCHAR(20)						NOT	NULL,
	"MobileNum_Pelath" VARCHAR(15)						NOT NULL	DEFAULT '0000-0000000000',
	"ID_Krathshs"	  INTEGER							NOT NULL,
	PRIMARY KEY ("ID_Krathshs"),
	FOREIGN KEY ("ID_Diaxeiristh") REFERENCES "DIAXEIRISTHS" ("ID_Employee")
            ON UPDATE CASCADE
            ON DELETE CASCADE,
	FOREIGN KEY ("Fname_Pelath") REFERENCES "PELATHS" ("Fname")
            ON UPDATE CASCADE
            ON DELETE CASCADE,
	FOREIGN KEY ("Lname_Pelath") REFERENCES "PELATHS" ("Lname")
            ON UPDATE CASCADE
            ON DELETE CASCADE,
	FOREIGN KEY ("MobileNum_Pelath") REFERENCES "PELATHS" ("MobileNum")
            ON UPDATE CASCADE
            ON DELETE CASCADE,
	FOREIGN KEY ("ID_Krathshs") REFERENCES "KRATHSH" ("ID")
			ON UPDATE CASCADE
			ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "GRAFEI" (
	"ID_Pelath" 	   INTEGER 	NOT NULL,
	"Barcode_Kritikhs" INTEGER 	NOT NULL,
	"Date_Review"      datetime	NOT NULL	DEFAULT	(strftime('%Y-%m-%d %H:%M:%S', 'now')),
	PRIMARY KEY ("ID_Pelath", "Barcode_Kritikhs"),
	FOREIGN KEY ("ID_Pelath") REFERENCES "PELATHS" ("ID_Xrhsth")
            ON UPDATE CASCADE
            ON DELETE CASCADE,
	FOREIGN KEY ("Barcode_Kritikhs") REFERENCES "KRITIKH" ("Barcode")
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "KANEI" (
	"ID_Xrhsth"   INTEGER		NOT NULL,
	"ID_Krathshs" INTEGER		NOT NULL,
	"Date_Reservation" datetime	NOT NULL	DEFAULT	(strftime('%Y-%m-%d %H:%M:%S', 'now')),
	PRIMARY KEY ("ID_Xrhsth", "ID_Krathshs"),
	FOREIGN KEY ("ID_Xrhsth") REFERENCES "XRHSTHS" ("ID")
            ON UPDATE CASCADE
            ON DELETE CASCADE,
	FOREIGN KEY ("ID_Krathshs") REFERENCES "KRATHSH" ("ID")
            ON UPDATE CASCADE
            ON DELETE CASCADE
);
"""

# Εκτέλεση του παραπάνω κώδικα για τη δημιουργια πινάκων
cursor.executescript(create_tables_query)

# Commit και κλείσιμο της σύνδεσης
conn.commit()
conn.close()
