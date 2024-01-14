import sqlite3
from datetime import datetime, timedelta

#Συνάρτηση για εκτέλεση query και προβολή του αποτελέσματος
def execute_query_and_print(query):
    # Σύνδεση με τη Βάση Δεδομένων
    conn = sqlite3.connect('r2_noindex.db') #μετονομασία αν χρειάζεται
    cursor = conn.cursor()

    # Εκτέλεση του query
    cursor.execute(query)

    # Λήψη και εκτύπωση αποτελέσματος
    result = cursor.fetchall()
    print(f"{result}\n")

    # Κλείσιμο της σύνδεσης
    conn.close()

#Queries σχετικά με TRAPEZI-----------------------------------------------------------------------------------------------------

#1.Διαθεσιμότητα συγκεκριμένου τραπεζιού, σε συγκεκριμένη μέρα και ώρα (εμφανίζεται όταν αυτό είναι διαθέσιμο)				  
table_availability = """
SELECT T.ID, T.Capacity, T.ID_Xwrou
FROM TRAPEZI AS T
WHERE T.ID = 11 AND T.ID NOT IN (SELECT ID_Trapeziou 
                                FROM TRAPEZI AS T 
                                JOIN AFORA AS A ON T.ID = A.ID_Trapeziou 
                                JOIN KRATHSH AS K ON K.ID = A.ID_Krathshs
                                WHERE Arrival BETWEEN datetime('2024-01-05 14:00:00', '-1 hours') AND datetime('2024-01-05 14:00:00', '+1 hours')
                                );
"""
#Εκτέλεση query και εκτύπωση
print(f"1.Διαθεσιμότητα συγκεκριμένου τραπεζιού, σε συγκεκριμένη μέρα και ώρα (εμφανίζεται όταν αυτό είναι διαθέσιμο):")
execute_query_and_print(table_availability)


#2.Εμφάνιση όλων των διαθέσιμων τραπεζιών, σε συγκεκριμένη μέρα και ώρα								
query2 = """
SELECT T.ID AS TableID, T.Capacity, X.ID_Department
FROM XWROS AS X JOIN TRAPEZI AS T ON X.ID_Department = T.ID_Xwrou
WHERE T.ID NOT IN (SELECT ID_Trapeziou 
                    FROM TRAPEZI AS T
                    JOIN AFORA AS A ON T.ID = A.ID_Trapeziou 
                    JOIN KRATHSH AS K ON K.ID = A.ID_Krathshs
                    WHERE Arrival BETWEEN datetime('2024-01-05 19:00:00', '-1 hours') AND datetime('2024-01-05 19:00:00', '+1 hours')
                    );
"""
#Εκτέλεση query και εκτύπωση
print(f"2.Εμφάνιση όλων των διαθέσιμων τραπεζιών, σε συγκεκριμένη μέρα και ώρα:")
execute_query_and_print(query2)


#3.Εμφάνιση διαθέσιμων τραπεζιών, σε συγκεκριμένη μέρα και ώρα, σε συγκεκριμένο χώρο
query3 = """
SELECT T.ID AS TableID, T.Capacity, X.ID_Department
FROM XWROS AS X JOIN TRAPEZI AS T ON X.ID_Department = T.ID_Xwrou
WHERE ID_Department = 111 AND T.ID NOT IN (SELECT ID_Trapeziou 
                                            FROM TRAPEZI AS T
                                            JOIN AFORA AS A ON T.ID = A.ID_Trapeziou 
                                            JOIN KRATHSH AS K ON K.ID = A.ID_Krathshs
                                            WHERE Arrival BETWEEN datetime('2024-01-05 19:00:00', '-1 hours') AND datetime('2024-01-05 19:00:00', '+1 hours')
                                            );
"""
#Εκτέλεση query και εκτύπωση
print(f"3.Εμφάνιση διαθέσιμων τραπεζιών, σε συγκεκριμένη μέρα και ώρα, σε συγκεκριμένο χώρο:")
execute_query_and_print(query3)


#4.Εμφάνιση διαθέσιμων τραπεζιών, σε συγκεκριμένη μέρα και ώρα, με συγκεκριμένη χωρητικότητα
query4 = """
SELECT T.ID AS TableID, T.Capacity, X.ID_Department
FROM XWROS AS X JOIN TRAPEZI AS T ON X.ID_Department = T.ID_Xwrou
WHERE Capacity = 2 AND T.ID NOT IN (SELECT ID_Trapeziou 
                                    FROM TRAPEZI AS T
                                    JOIN AFORA AS A ON T.ID = A.ID_Trapeziou 
                                    JOIN KRATHSH AS K ON K.ID = A.ID_Krathshs
                                    WHERE Arrival BETWEEN datetime('2024-01-05 19:00:00', '-1 hours') AND datetime('2024-01-05 19:00:00', '+1 hours')
);
"""
#Εκτέλεση query και εκτύπωση
print(f"4.Εμφάνιση διαθέσιμων τραπεζιών, σε συγκεκριμένη μέρα και ώρα, με συγκεκριμένη χωρητικότητα:")
execute_query_and_print(query4)


#5.Εμφάνιση διαθέσιμων τραπεζιών, σε συγκεκριμένη μέρα και ώρα, σε συγκεκριμένο χώρο, με συγκεκριμένη χωρητικότητα
query5 = """
SELECT T.ID AS TableID, T.Capacity, X.ID_Department
FROM XWROS AS X JOIN TRAPEZI AS T ON X.ID_Department = T.ID_Xwrou
WHERE Capacity = 2 AND ID_Department = 111 AND T.ID NOT IN (SELECT ID_Trapeziou 
                                                            FROM TRAPEZI AS T
                                                            JOIN AFORA AS A ON T.ID = A.ID_Trapeziou 
                                                            JOIN KRATHSH AS K ON K.ID = A.ID_Krathshs
                                                            WHERE Arrival BETWEEN datetime('2024-01-05 19:00:00', '-1 hours') AND datetime('2024-01-05 19:00:00', '+1 hours')
                                                            );
"""
#Εκτέλεση query και εκτύπωση
print(f"5.Εμφάνιση διαθέσιμων τραπεζιών, σε συγκεκριμένη μέρα και ώρα, σε συγκεκριμένο χώρο, με συγκεκριμένη χωρητικότητα:")
execute_query_and_print(query5)
#Τέλος διαθεσιμότητας-----------------------------------------------------------------------------------------------------------

#6.Εμφάνιση δεσμευμένων τραπεζιών, σε συγκεκριμένη μέρα και ώρα
query6 = """
SELECT T.ID_Xwrou, A.ID_Trapeziou, T.Capacity, A.ID_Krathshs, K.Name, K.MobileNumber, K.Num_of_People, K.Arrival
FROM TRAPEZI AS T 
    JOIN AFORA AS A ON T.ID = A.ID_Trapeziou 
    JOIN KRATHSH AS K ON K.ID = A.ID_Krathshs
WHERE Arrival BETWEEN datetime('2024-01-05 14:00:00', '-1 hours') AND datetime('2024-01-05 14:00:00', '+1 hours')
"""
#Εκτέλεση query και εκτύπωση
print(f"6.Εμφάνιση δεσμευμένων τραπεζιών, σε συγκεκριμένη μέρα και ώρα:")
execute_query_and_print(query6)


#7.Ταξινόμηση τραπεζιών, με κριτήριο το πλήθος των κρατήσεων (Δημοφιλέστερα τραπέζια)
query7 = """
SELECT T.ID AS TableID, T.Capacity, T.ID_Xwrou, count(K.ID) AS Num_of_Reservations
FROM TRAPEZI AS T 
    JOIN AFORA AS A ON T.ID = A.ID_Trapeziou 
    JOIN KRATHSH AS K ON K.ID = A.ID_Krathshs 
GROUP BY T.ID, T.Capacity
ORDER BY Num_of_Reservations DESC
"""
#Εκτέλεση query και εκτύπωση
print(f"7.Ταξινόμηση τραπεζιών, με κριτήριο το πλήθος των κρατήσεων (Δημοφιλέστερα τραπέζια):")
execute_query_and_print(query7)


#8.Υπολογισμός συνολικής χωρητικότητας
query8 = """
SELECT sum(Capacity) AS Total_Capacity
FROM TRAPEZI
"""
#Εκτέλεση query και εκτύπωση
print(f"8.Υπολογισμός συνολικής χωρητικότητας:")
execute_query_and_print(query8)


#9.Υπολογισμός πλήθους διαθέσιμων θέσεων, σε συγκεκριμένη μέρα και ώρα (στα διαθέσιμα τραπέζια)
query9 = """
SELECT (SELECT sum(Capacity)
        FROM TRAPEZI 
        WHERE ID NOT IN(SELECT ID_Trapeziou 
                        FROM TRAPEZI AS T JOIN AFORA AS A ON T.ID=A.ID_Trapeziou JOIN KRATHSH AS K ON K.ID=A.ID_Krathshs
                        WHERE Arrival BETWEEN datetime('2024-01-05 19:00:00', '-1 hours') AND datetime('2024-01-05 19:00:00', '+1 hours')
                        )
        ) AS Total_Available_Capacity
"""
#Εκτέλεση query και εκτύπωση
print(f"9.Υπολογισμός πλήθους διαθέσιμων θέσεων, σε συγκεκριμένη μέρα και ώρα (στα διαθέσιμα τραπέζια):")
execute_query_and_print(query9)


#10.Μέγιστο πλήθος πελατών που μπορούν να εξυπηρετηθούν σε μία ημέρα (Προϋποθέσεις: δεσμευμένα όλα τα τραπέζια κάθε στιγμή, διάρκεια κράτησης 2hours)
query10 = """
WITH RECURSIVE TimeSlots AS (
  SELECT time('13:00:00') AS StartTime,
		 time('13:00:00', '+2 hours') AS EndTime

  UNION ALL

  SELECT EndTime AS StartTime,
		 time(EndTime, '+2 hours') AS EndTime
  FROM TimeSlots
  WHERE EndTime < '23:00:00'
),

	--Πλήθος Timeslots
TotalCounts AS (SELECT count(*) AS NumTimeSlots
				FROM TimeSlots
				)
				
	--Συνολικά ανά Timeslot
SELECT StartTime, EndTime, 
		sum(Capacity) AS Total_people 
FROM TimeSlots JOIN TRAPEZI
GROUP BY StartTime, EndTime

UNION ALL

	 --Συνολικά ανά μέρα
SELECT '#' AS StartTime, 'TOTAL' AS EndTime,
		 sum(T.Capacity) * TC.NumTimeSlots AS Total_People
FROM TRAPEZI AS T, TotalCounts AS TC;
"""
#Εκτέλεση query και εκτύπωση
print(f"10.Μέγιστο πλήθος πελατών που μπορούν να εξυπηρετηθούν σε μία ημέρα (Προϋποθέσεις: δεσμευμένα όλα τα τραπέζια κάθε στιγμή, διάρκεια κράτησης 2hours):")
execute_query_and_print(query10)


#11.Υπολογισμός μέγιστων δυνατών εσόδων, σε μία μέρα, για γεμάτο εστιατόριο (Προϋποθέσεις: δεσμευμένα όλα τα τραπέζια κάθε στιγμή, διάρκεια κράτησης 2hours, min κατανάλωση 20€)
query11 = """
WITH RECURSIVE TimeSlots AS (
  SELECT time('13:00:00') AS StartTime,
		 time('13:00:00', '+2 hours') AS EndTime

  UNION ALL

  SELECT EndTime AS StartTime,
		 time(EndTime, '+2 hours') AS EndTime
  FROM TimeSlots
  WHERE EndTime < '23:00:00'
),

	--Πλήθος Timeslots
TotalCounts AS (SELECT count(*) AS NumTimeSlots
				FROM TimeSlots
				)

	--Συνολικά ανά Timeslot
SELECT StartTime, EndTime, 
		sum(Capacity) AS Total_people, 
		sum(Capacity) * 20 AS Total_income
FROM TimeSlots JOIN TRAPEZI
GROUP BY StartTime, EndTime

UNION ALL

	--Συνολικά ανά μέρα
SELECT '#' AS StartTime, 'TOTAL' AS EndTime, 
		 sum(T.Capacity) * TC.NumTimeSlots AS Total_People,
		(sum(T.Capacity) * 20) * TC.NumTimeSlots AS Total_income
FROM TRAPEZI AS T, TotalCounts AS TC;
"""
#Εκτέλεση query και εκτύπωση
print(f"11.Υπολογισμός μέγιστων δυνατών εσόδων, σε μία μέρα, για γεμάτο εστιατόριο (Προϋποθέσεις: δεσμευμένα όλα τα τραπέζια κάθε στιγμή, διάρκεια κράτησης 2hours, min κατανάλωση 20€):")
execute_query_and_print(query11)

#--Queries σχετικά με KRATHSH-----------------------------------------------------------------------------------------------------------

#12.Λεπτομέρειες συγκεκριμένης κράτησης, σε συγκεκριμένη μέρα
query12 = """
SELECT K.*, A.ID_Trapeziou, T.ID_Xwrou
FROM KRATHSH AS K 
	JOIN AFORA AS A ON K.ID = A.ID_Krathshs 
	JOIN TRAPEZI AS T ON A.ID_Trapeziou = T.ID
WHERE K.Name like '%Ross%' AND date(K.Arrival) = '2024-01-05'
ORDER BY Arrival;
"""
#Εκτέλεση query και εκτύπωση
print(f"12.Λεπτομέρειες συγκεκριμένης κράτησης, σε συγκεκριμένη μέρα:")
execute_query_and_print(query12)


#13.Λεπτομέρειες κράτησης συγκεκριμένου πελάτη, σε συγκεκριμένη μέρα (Εφόσον ο πελάτης είναι χρήστης)
query13 = """
SELECT P.ID_Xrhsth, P.Lname, P.MobileNum, KR.Name as Res_Name, KR.MobileNumber as Res_Mobile, Kr.Num_of_People, KR.Arrival, A.ID_Trapeziou, T.ID_Xwrou
FROM PELATHS as P
	JOIN XRHSTHS as X ON P.ID_Xrhsth = X.ID
	JOIN KANEI as K ON X.ID = K.ID_Xrhsth 
	JOIN KRATHSH as KR ON K.ID_Krathshs = KR.ID 
	JOIN AFORA as A ON KR.ID = A.ID_Krathshs 
	JOIN TRAPEZI as T ON A.ID_Trapeziou = T.ID
WHERE KR.name like '%ROss%' AND date(Arrival) ='2024-01-05'
ORDER BY Arrival; 
"""

#Εκτέλεση query και εκτύπωση
print(f"13.Λεπτομέρειες κράτησης συγκεκριμένου πελάτη, σε συγκεκριμένη μέρα (Εφόσον ο πελάτης είναι χρήστης):")
execute_query_and_print(query13)


#14.Λεπτομέρειες κράτησης συγκεκριμένου πελάτη, σε συγκεκριμένη μέρα (Εφόσον ο πελάτης επικοινώνησε μέσω του Διαχειριστή)
query14 = """
SELECT E.ID_Diaxeiristh, P.Lname, P.Fname, KR.ID AS ResID, KR.Name as Res_Name, KR.MobileNumber as Res_Mobile, Kr.Num_of_People, KR.Arrival, A.ID_Trapeziou, T.ID_Xwrou
FROM EPIKOINWNEI AS E 
	JOIN PELATHS AS P 
	JOIN KRATHSH AS KR ON P.Lname=KR.name
	JOIN AFORA as A ON KR.ID = A.ID_Krathshs 
	JOIN TRAPEZI as T ON A.ID_Trapeziou = T.ID 
WHERE E.Lname_Pelath = P.Lname AND E.Fname_Pelath = P.Fname AND E.MobileNum_Pelath=P.MobileNum
		AND KR.name like '%Mart%' AND date(Arrival) ='2024-01-08';
"""
#Εκτέλεση query και εκτύπωση
print(f"14.Λεπτομέρειες κράτησης συγκεκριμένου πελάτη, σε συγκεκριμένη μέρα (Εφόσον ο πελάτης επικοινώνησε μέσω του Διαχειριστή):")
execute_query_and_print(query14)


#15.Εμφάνιση κρατήσεων που έχουν γίνει μέσω επικοινωνίας με Διαχειριστή
query15 = """
SELECT E.ID_Diaxeiristh, P.Lname, P.Fname, KR.ID AS ResID, KR.Name as Res_Name, KR.MobileNumber as Res_Mobile, Kr.Num_of_People, KR.Arrival, A.ID_Trapeziou, T.ID_Xwrou
FROM EPIKOINWNEI AS E 
	JOIN PELATHS AS P 
	JOIN KRATHSH AS KR ON P.Lname=KR.name
	JOIN AFORA as A ON KR.ID = A.ID_Krathshs 
	JOIN TRAPEZI as T ON A.ID_Trapeziou = T.ID 
WHERE E.Lname_Pelath = P.Lname AND E.Fname_Pelath = P.Fname AND E.MobileNum_Pelath=P.MobileNum AND E.ID_Krathshs=KR.ID
ORDER BY KR.Arrival
"""
#Εκτέλεση query και εκτύπωση
print(f"15.Εμφάνιση κρατήσεων που έχουν γίνει μέσω επικοινωνίας με Διαχειριστή:")
execute_query_and_print(query15)


#16.Πλήθος κρατήσεων που έχουν γίνει, από κάθε χρήστη --> Εύρεση χρήστη με τις περισσότερες κρατήσεις !Περιλαμβάνει κ του Διαχειριστή!
query16 = """
SELECT X.ID, X.Username,
		count (K.ID_Krathshs) AS Num_of_reservations
FROM XRHSTHS AS X JOIN KANEI AS K ON X.ID = K.ID_Xrhsth
GROUP BY X.ID, X.Username
ORDER BY Num_of_reservations DESC;
"""
#Εκτέλεση query και εκτύπωση
print(f"16.Πλήθος κρατήσεων που έχουν γίνει, από κάθε χρήστη --> Εύρεση χρήστη με τις περισσότερες κρατήσεις !Περιλαμβάνει κ του Διαχειριστή!:")
execute_query_and_print(query16)


#17.Πλήθος κρατήσεων που έχουν γίνει, από κάθε χρήστη --> Εύρεση χρήστη με τις περισσότερες κρατήσεις !Χωρίς του Διαχειριστή!
query17 = """
SELECT X.ID, X.Username,
		count (K.ID_Krathshs) AS Num_of_reservations
FROM XRHSTHS AS X JOIN KANEI AS K ON X.ID = K.ID_Xrhsth
WHERE X.Username != 'admin'
GROUP BY X.ID, X.Username
ORDER BY Num_of_reservations DESC;
"""
#Εκτέλεση query και εκτύπωση
print(f"17.Πλήθος κρατήσεων που έχουν γίνει, από κάθε χρήστη --> Εύρεση χρήστη με τις περισσότερες κρατήσεις !Χωρίς του Διαχειριστή!:")
execute_query_and_print(query17)


#18.Πλήθος κρατήσεων που έχουν γίνει, από συγκεκριμένο χρήστη
query18 = """
SELECT X.ID, X.Username, P.Lname, P.Fname,
		count (K.ID_Krathshs) AS Num_of_reservations
FROM PELATHS AS P 
	JOIN XRHSTHS AS X ON P.ID_Xrhsth = X.ID 
	JOIN KANEI AS K ON X.ID = K.ID_Xrhsth
WHERE P.Lname like '%fuller%' AND P.Fname like '%penelope%'
GROUP BY X.ID, X.Username, P.Lname, P.Fname
ORDER BY Num_of_reservations DESC;
"""
#Εκτέλεση query και εκτύπωση
print(f"18.Πλήθος κρατήσεων που έχουν γίνει, από συγκεκριμένο χρήστη:")
execute_query_and_print(query18)


#19.Εμφάνιση κρατήσεων μιας συγκεκριμένης μέρας
query19 = """
SELECT K.*, A.ID_Trapeziou, T.ID_Xwrou 
FROM KRATHSH AS K 
	JOIN AFORA AS A ON K.ID = A.ID_Krathshs 
	JOIN TRAPEZI AS T ON A.ID_Trapeziou = T.ID
WHERE date(K.Arrival)= '2024-01-05'
ORDER BY K.Arrival;
"""
#Εκτέλεση query και εκτύπωση
print(f"19.Εμφάνιση κρατήσεων μιας συγκεκριμένης μέρας:")
execute_query_and_print(query19)


#20.Πλήθος κρατήσεων μιας συγκεκριμένης μέρας
query20 = """
SELECT '2024-01-05' AS Arrival_date, count(*) AS Num_of_res
FROM KRATHSH AS K 
WHERE date(K.Arrival)= '2024-01-05'
"""
#Εκτέλεση query και εκτύπωση
print(f"20.Πλήθος κρατήσεων μιας συγκεκριμένης μέρας:")
execute_query_and_print(query20)


#21.Εμφάνιση κρατήσεων ενός συγκεκριμένου timeslot
query21 = """
SELECT K.*, A.ID_Trapeziou, T.ID_Xwrou
FROM KRATHSH AS K 
	JOIN AFORA AS A ON K.ID = A.ID_Krathshs 
	JOIN TRAPEZI AS T ON A.ID_Trapeziou = T.ID
WHERE K.Arrival BETWEEN '2024-01-05 15:00:00' AND '2024-01-05 18:00:00'
ORDER BY K.Arrival;
"""
#Εκτέλεση query και εκτύπωση
print(f"21.Εμφάνιση κρατήσεων ενός συγκεκριμένου timeslot:")
execute_query_and_print(query21)


#22.Πλήθος κρατήσεων ενός συγκεκριμένου timeslot
query22 = """
SELECT  '2024-01-05 15:00:00' AS 'From', 
		'2024-01-05 18:00:00' AS 'To',
		count(*) AS Num_of_res
FROM KRATHSH AS K
WHERE K.Arrival BETWEEN '2024-01-05 15:00:00' AND '2024-01-05 18:00:00'
"""
#Εκτέλεση query και εκτύπωση
print(f"22.Πλήθος κρατήσεων ενός συγκεκριμένου timeslot:")
execute_query_and_print(query22)


#23.Εμφάνιση κρατήσεων που καταχωρήθηκαν μια συγκεκριμένη μέρα
query23 = """
SELECT KA.Date_Reservation, K.*, A.ID_Trapeziou, T.ID_Xwrou
FROM KANEI AS KA 
	JOIN KRATHSH AS K ON KA.ID_Krathshs = K.ID
	JOIN AFORA AS A ON K.ID = A.ID_Krathshs 
	JOIN TRAPEZI AS T ON A.ID_Trapeziou = T.ID
WHERE date(KA.Date_Reservation)='2023-12-22';
"""
#Εκτέλεση query και εκτύπωση
print(f"23.Εμφάνιση κρατήσεων που καταχωρήθηκαν μια συγκεκριμένη μέρα:")
execute_query_and_print(query23)


#24.Πλήθος κρατήσεων που καταχωρήθηκαν μια συγκεκριμένη μέρα
query24 = """
SELECT '2023-12-22' AS Date_Reservation,
		count(*) AS Num_of_res_done
FROM KANEI AS KA
WHERE date(KA.Date_Reservation) ='2023-12-22'
"""
#Εκτέλεση query και εκτύπωση
print(f"24.Πλήθος κρατήσεων που καταχωρήθηκαν μια συγκεκριμένη μέρα:")
execute_query_and_print(query24)


#25.Πλήθος κρατήσεων, που έγιναν μέσω τηλεφώνου ή από κοντά (Δηλαδή αυτές μέσω του admin)
query25 = """
SELECT count(*) as Phone_or_visit
FROM KANEI AS K JOIN XRHSTHS AS X ON K.ID_Xrhsth = X.ID
WHERE X.Username = 'admin'
"""
#Εκτέλεση query και εκτύπωση
print(f"25.Πλήθος κρατήσεων, που έγιναν μέσω τηλεφώνου ή από κοντά (Δηλαδή αυτές μέσω του admin):")
execute_query_and_print(query25)


#26.Πλήθος κρατήσεων, που έγιναν μέσω της εφαρμογής
query26 = """
SELECT count(*) as Total_App_res
FROM KANEI
"""
#Εκτέλεση query και εκτύπωση
print(f"26.Πλήθος κρατήσεων, που έγιναν μέσω της εφαρμογής:")
execute_query_and_print(query26)


#27.Πλήθος κρατήσεων, που έγιναν μέσω της εφαρμογής (εξαιρουμένων του διαχειριστή)
query27 = """
SELECT count(*) as Clients_res_app
FROM KANEI AS K JOIN XRHSTHS AS X ON K.ID_Xrhsth = X.ID
WHERE X.Username != 'admin'
"""
#Εκτέλεση query και εκτύπωση
print(f"27.Πλήθος κρατήσεων, που έγιναν μέσω της εφαρμογής (εξαιρουμένων του διαχειριστή):")
execute_query_and_print(query27)


#28.Υπολογισμός προσδοκώμενων εσόδων ανά ημέρα κ συνολικά, για συγκεκριμένο χρονικό διάστημα (min κατανάλωση 20€/ άτομο)
query28 = """
	--Συνολικά
SELECT 'TOTAL' AS Reservation_Date, count(*) AS Num_of_res, sum(Num_of_People) AS Total_people, sum(Num_of_People) * 20 AS Total_income
FROM KRATHSH AS KR
WHERE date(KR.Arrival) BETWEEN '2024-01-01' AND '2024-01-30'

UNION
	--Ανά ημέρα
SELECT date(Arrival) AS Reservation_Date, count(*) AS Num_of_res, sum(Num_of_People) AS Total_people, sum(Num_of_People) * 20 AS Total_income
FROM KRATHSH AS KR
WHERE date(KR.Arrival) BETWEEN '2024-01-01' AND '2024-01-30'
GROUP BY Reservation_Date
ORDER BY Reservation_Date
"""
#Εκτέλεση query και εκτύπωση
print(f"28.Υπολογισμός προσδοκώμενων εσόδων ανά ημέρα κ συνολικά, για συγκεκριμένο χρονικό διάστημα (min κατανάλωση 20€/ άτομο):")
execute_query_and_print(query28)

#--Queries σχετικά με XRHSTHS-----------------------------------------------------------------------------------------------------------

#29.Πλήθος Χρηστών, εγγεγραμμένων στην εφαρμογή
query29 = """
SELECT COUNT(*) AS Num_of_users
FROM XRHSTHS;
"""
#Εκτέλεση query και εκτύπωση
print(f"29.Πλήθος Χρηστών, εγγεγραμμένων στην εφαρμογή:")
execute_query_and_print(query29)

#--Queries σχετικά με PROTIMHSEIS-----------------------------------------------------------------------------------------------------------

#30.Υπολογισμός πλήθους εμφανίσεων αγαπημένου επιδόρπιου --> Συχνότερο
query30 = """
SELECT Favorite_Dessert, count(*) AS Num_of_selections
FROM PROTIMHSEIS
GROUP BY Favorite_Dessert
ORDER BY Num_of_selections DESC
"""
#Εκτέλεση query και εκτύπωση
print(f"30.Υπολογισμός πλήθους εμφανίσεων αγαπημένου επιδόρπιου --> Συχνότερο:")
execute_query_and_print(query30)


#31.Υπολογισμός πλήθους εμφανίσεων αγαπημένου ποτού --> Συχνότερο
query31 = """
SELECT Favorite_Drink, count(*) AS Num_of_selections
FROM PROTIMHSEIS
GROUP BY Favorite_Drink
ORDER BY Num_of_selections DESC
"""
#Εκτέλεση query και εκτύπωση
print(f"31.Υπολογισμός πλήθους εμφανίσεων αγαπημένου ποτού --> Συχνότερο:")
execute_query_and_print(query31)


#32.Εμφάνιση προτιμήσεων, πελατών που έχουν κράτηση συγκεκριμένη μέρα
query32 = """
SELECT P.Lname, P.Fname, PR.Favorite_Dessert, PR.Favorite_Drink, KR.Arrival
FROM PROTIMHSEIS AS PR
	JOIN PELATHS AS P ON PR.ID_Pelath = P.ID_Xrhsth
	JOIN XRHSTHS AS X ON P.ID_Xrhsth = X.ID
	JOIN KANEI AS K ON X.ID = K.ID_Xrhsth
	JOIN KRATHSH AS KR ON K.ID_Krathshs = KR.ID
WHERE date(KR.Arrival) = '2024-01-05' 
ORDER BY P.Lname
"""
#Εκτέλεση query και εκτύπωση
print(f"32.Εμφάνιση προτιμήσεων, πελατών που έχουν κράτηση συγκεκριμένη μέρα:")
execute_query_and_print(query32)


#33.Δικαιούται ο συγκεκριμένος πελάτης κέρασμα (2 κρατήσεις); --Αν ναι, εμφάνισή του.
query33 = """
SELECT P.Lname, P.Fname, PR.Favorite_Dessert, PR.Favorite_Drink,  count(*) AS Num_of_res
FROM PROTIMHSEIS AS PR
	JOIN PELATHS AS P ON PR.ID_Pelath = P.ID_Xrhsth
	JOIN KANEI AS K ON P.ID_Xrhsth = K.ID_Xrhsth
WHERE P.Lname like '%Ful%'
GROUP BY P.Fname, P.Lname, PR.Favorite_Dessert, PR.Favorite_Drink
HAVING Num_of_res = 2
"""
#Εκτέλεση query και εκτύπωση
print(f"33.Δικαιούται ο συγκεκριμένος πελάτης κέρασμα (2 κρατήσεις); --Αν ναι, εμφάνισή του.:")
execute_query_and_print(query33)


#34.Πλήθος κρατήσεων συγκεκριμένου πελάτη
query34 = """
SELECT P.Lname, P.Fname, PR.Favorite_Dessert, PR.Favorite_Drink,  count(*) AS Num_of_res
FROM PROTIMHSEIS AS PR
	JOIN PELATHS AS P ON PR.ID_Pelath = P.ID_Xrhsth
	JOIN KANEI AS K ON P.ID_Xrhsth = K.ID_Xrhsth
WHERE P.Lname like '%Ful%'
GROUP BY P.Fname, P.Lname, PR.Favorite_Dessert, PR.Favorite_Drink
"""
#Εκτέλεση query και εκτύπωση
print(f"34.Πλήθος κρατήσεων συγκεκριμένου πελάτη:")
execute_query_and_print(query34)


#35.Εμφάνιση προτιμήσεων, των πελατών που δικαιούνται κέρασμα (2 κρατήσεις)
query35 = """
SELECT P.Lname, P.Fname, PR.Favorite_Dessert, PR.Favorite_Drink,  count(*) AS Num_of_res
FROM PROTIMHSEIS AS PR
	JOIN PELATHS AS P ON PR.ID_Pelath = P.ID_Xrhsth
	JOIN KANEI AS K ON P.ID_Xrhsth = K.ID_Xrhsth
GROUP BY P.Fname, P.Lname, PR.Favorite_Dessert, PR.Favorite_Drink
HAVING Num_of_res = 2
ORDER BY P.Lname
"""
#Εκτέλεση query και εκτύπωση
print(f"35.Εμφάνιση προτιμήσεων, των πελατών που δικαιούνται κέρασμα (2 κρατήσεις):")
execute_query_and_print(query35)

#--Queries σχετικά με ALLERGIA_PROTIMHSEIS-----------------------------------------------------------------------------------------------------------

#36.Εμφάνιση συχνότερης αλλεργιογόνας ουσίας
query36 = """
SELECT Substance,
		count(*) AS Frequency_of_sub
FROM ALLERGIA_PROTIMHSEIS
GROUP BY Substance
ORDER BY Frequency_of_sub DESC;
"""
#Εκτέλεση query και εκτύπωση
print(f"36.Εμφάνιση συχνότερης αλλεργιογόνας ουσίας:")
execute_query_and_print(query36)


#37.Εμφάνιση αλλεργίας συγκεκριμένης κράτησης
query37 = """
SELECT AP.Substance, P.Fname, P.Lname, P.MobileNum, KR.name AS ResName, KR.Arrival
FROM KRATHSH AS KR
	JOIN KANEI AS K ON KR.ID = K.ID_Krathshs
	JOIN ALLERGIA_PROTIMHSEIS AS AP ON K.ID_Xrhsth = AP.ID_Pelath
	JOIN PELATHS AS P ON K.ID_Xrhsth = P.ID_Xrhsth
WHERE P.Lname like '%Fu%' AND KR.Arrival = '2024-01-01 21:00:00';
"""
#Εκτέλεση query και εκτύπωση
print(f"37.Εμφάνιση αλλεργίας συγκεκριμένης κράτησης:")
execute_query_and_print(query37)

#--Queries σχετικά με KRITIKH-----------------------------------------------------------------------------------------------------------

#38.Εμφάνιση μέσου όρου κριτικών εστιατορίου
query38 = """
SELECT avg(Rate) AS AverageRate
FROM KRITIKH;
"""
#Εκτέλεση query και εκτύπωση
print(f"38.Εμφάνιση μέσου όρου κριτικών εστιατορίου:")
execute_query_and_print(query38)

#--Queries σχετικά με DIAXEIRISTHS-----------------------------------------------------------------------------------------------------------

#39.Υπολογισμός ωρών εργασίας Διαχειριστή (Ακρίβεια ώρας)
query39 = """
SELECT ID_Employee, Start_shift, End_shift, 
		CASE 
		WHEN time(End_shift) > time(Start_shift)
		THEN time(End_shift) - time(Start_shift)
		ELSE time(End_shift) - time(Start_shift)+ 24
		END AS WorkedHours
FROM DIAXEIRISTHS
WHERE ID_Employee = 1111
"""
#Εκτέλεση query και εκτύπωση
print(f"39.Υπολογισμός ωρών εργασίας Διαχειριστή (Ακρίβεια ώρας):")
execute_query_and_print(query39)


#40.Υπολογισμός μηνιαίας αμοιβής Διαχειριστή (Εαν πληρώνεται 4€/ώρα και δουλεύει 7/7 μέρες/βδομάδα --> 30 μέρες/μήνα)
query40 = """
SELECT ID_Employee, Start_shift, End_shift, WorkedHours, WorkedHours * 4 AS DayPayment, (WorkedHours * 4) * 30 AS MonthPayment
FROM 	(SELECT ID_Employee, Start_shift, End_shift, 
			CASE 
			WHEN time(End_shift) > time(Start_shift)
			THEN time(End_shift) - time(Start_shift)
			ELSE time(End_shift) - time(Start_shift)+ 24
			END AS WorkedHours
		FROM DIAXEIRISTHS
		WHERE ID_Employee = 1111)
"""
#Εκτέλεση query και εκτύπωση
print(f"40.Υπολογισμός μηνιαίας αμοιβής Διαχειριστή (Εαν πληρώνεται 4€/ώρα και δουλεύει 7/7 μέρες/βδομάδα --> 30 μέρες/μήνα):")
execute_query_and_print(query40)

#--Queries σχετικά με PELATHS-----------------------------------------------------------------------------------------------------------

#41.Ταξινόμηση Πελατών με κριτήριο τον ΤΚ
query41 = """
SELECT Lname, Fname, Address_PostalCode 
FROM PELATHS 
ORDER BY Address_PostalCode
"""
#Εκτέλεση query και εκτύπωση
print(f"41.Ταξινόμηση Πελατών με κριτήριο τον ΤΚ:")
execute_query_and_print(query41)

