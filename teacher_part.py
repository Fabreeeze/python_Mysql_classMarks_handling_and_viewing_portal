import mysql.connector
import pandas as pd
import sys
from tabulate import tabulate
header1=['rollno','students name', 'parents name']
nnn=[]
db = mysql.connector.connect(host="localhost",
user="root", 
passwd="groot",
db="school") 
print("Connected Sucessfully !!!!")
mycursor=db.cursor()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('''
      



''')
a=1
t_choice1=0
while t_choice1!='exit':
    print(
        '''what do u want to do

    type:-
        log to check and update student details
        homework to check and upload home work
        exam to check and upload exams
        fees to check fee record
        exit to log out''')
    t_choice1=input('enter your choice here:-')
    t_choice1=t_choice1.lower()
    a=1
    if t_choice1=='log':
        t_choice2=2
        while t_choice2!= 'close':
            if a==1:
                mycursor.execute("SELECT * FROM students order by r_no")
                myresult = mycursor.fetchall()
                for x in myresult:
                    nnn.append(x)
                print(tabulate(nnn,header1))
                a=2
            print('''          type
                      'insert'to enter new row
                      'edit' to edit information
                      'close' to go back to home page')''')
            t_choice2=input('enter u  choice:-')
            t_choice2=t_choice2.lower()
            if t_choice2=='insert':
                t_rno=int(input('enter roll number of student:-'))
                t_name=(input('enter name  of student:-'))
                t_pname=(input("enter parent's name  of student:-"))
                sql = "INSERT INTO students (r_no,student_name,parents_name) VALUES (%s, %s, %s)"
                val = (t_rno,t_name,t_pname)
                mycursor.execute(sql, val)
                db.commit()
                a=1
                print(mycursor.rowcount, "record inserted.")
            elif t_choice2=='edit':
                t_rno_change=(input('enter roll no of student whose details you want to change:-'))
                print('''
                          
                          enter new details''')
                a=t_rno_change
                t_name_change=input('enter name of student:-')
                t_pname_change=(input("enter parent's name  of student:-"))
                sql = "UPDATE students SET student_name ="+"'" + t_name_change + "'" + ',parents_name=' + "'" + t_pname_change + "'" + ' WHERE r_no ='+"'"+a+"'"
                mycursor.execute(sql)
                db.commit()
                a=1          
                print(mycursor.rowcount, "record(s) affected")
            else:
                print('enter a valid command')
    a=1                      
    if t_choice1=='homework':
        t_choice2=2
        while t_choice2!= 'close':
            if a==1:                   
                mycursor.execute("SELECT * FROM homework")
                myresult = mycursor.fetchall()
                for x in myresult:    
                    print(tabulate(x))
                a=2
            print('''          type
                  'add' to add homework
                  'edit' to edit homework
                  'close' to go back to home page')''')
            t_choice2=input('enter u  choice:-')
            t_choice2=t_choice2.lower()
            if t_choice2=='add':
                t_srno=int(input('enter serial number number :-'))
                t_date=(input('enter date(yyyy-mm-dd):-'))
                t_sname=(input("enter subject name:-"))
                t_hw=input('enter the homework:-')
                t_duedate=input('enter due date(yyyy-mm-dd):-')
                sql = "INSERT INTO homework  VALUES (%s, %s, %s,%s,%s)"
                val = (t_srno,t_date,t_sname,t_hw,t_duedate)
                mycursor.execute(sql, val)
                db.commit()
                a=1
                print(mycursor.rowcount, "record inserted.")
            elif t_choice2=='edit':
                t_rno_change=int(input('enter serial number of homework which you want to change:-'))
                print('''
        
                          enter new details''')
                a=t_rno_change
                t_date_change=input('enter date(yyyy-mm-dd):-')
                t_sname_change=(input("enter subject name:-"))
                t_hw_change=input('enter the homework:-')
                t_duedate_change=input('enter due date(yyyy-mm-dd):-')
                sql = "UPDATE homework SET date = t_date_change, subject=t_sname_change,homework= t_hw_change, due_date= t_duedate_change WHERE sr_no ="+""
                mycursor.execute(sql)
                a=1
                db.commit()
                print(mycursor.rowcount, "record(s) affected")
    a=1
    if t_choice1=='exam':
        t_choice2=0
        while t_choice2!= 'close':       
            if a==1:
                mycursor.execute("SELECT * FROM exams")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(tabulate(x))
                a=2
            print('''          type
                                  'insert'to enter new row
                                  'edit' to edit information
                                  'close' to go back to home page''')
            t_choice2=input('enter your choice here:-')
            t_choice2=t_choice2.lower()
            if t_choice2=='insert':
                t_srno=int(input('enter serial number :-'))
                t_subject=(input('enter subject:-'))
                t_edate=(input("enter date of exam(yyyy-mm-dd):-"))
                t_etime=input("enter exam time")
                t_esyllabus=input("enter exam syllabus")
                sql = "INSERT INTO exams  VALUES (%s, %s, %s,%s,%s)"
                val = (t_srno,t_subject,t_edate,t_etime,t_esyllabus)
                mycursor.execute(sql, val)
                db.commit()
                a=1
                print(mycursor.rowcount, "record inserted.")
            elif t_choice2=='edit':
                t_rno_change=int(input('enter serial number of homework which you want to change:-'))
                print('''
        
                                      enter new details''')
                a=t_rno_change
                t_edate_change=input('enter date of exam(yyyy-mm-dd):-')
                t_sname_change=(input("enter subject name:-"))
                t_syllabus_change=input('enter the exam syllabus:-')
                t_etime_change=input('enter exam time:-')
                sql = "UPDATE exams SET date = t_edate_change, subject=t_sname_change,syllabus= t_syllabus_change, time= t_etime_change WHERE sr_no ="+""
                mycursor.execute(sql)                          
                db.commit()
                a=1                      
                print(mycursor.rowcount, "record(s) affected")
            else:
                print('enter a valid command')
    a=1
    if t_choice1=='fees':
        t_choice2=2
        while t_choice2!= 'close':
            if a==1:            
                mycursor.execute("SELECT * FROM fees")
                myresult = mycursor.fetchall()
               # for x in myresult:
                #    print(x)
            print('''          type
                      'remind all'to remind all students to pay fees
                      'remind some' to remind selected student to pay fees
                      'remind late fee' to remind selected student to pay fees and late fee fine
                      'close' to go back)''')
            t_choice2=input('enter u  choice:-')
            t_choice2=t_choice2.lower()
            if t_choice2 == 'remind all':
                sql = "Select curdate()"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                for x in myresult:
                    a=x[0]
                sql = "Select sr_no from fee_record"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                for x in myresult:
                    x=x[0][0]
                    sr_no =int(x)+1
                    
                sql = "INSERT INTO fee_record  VALUES (%s, %s, %s , %s , %s , %s)"
                val = (sr_no,a  ,'all','all','all','reminder to pay fees on time.')
                mycursor.execute(sql, val)
                db.commit()
                a=1
    






