def student(m):
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
    
    mycursor=db.cursor()
    # as student
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('''
          
    
    
    
    ''')
    a=1
    #m=r_no
    #m='1'
    s_choice1=0
    while s_choice1!='exit':
        print(
            '''what do u want to do
    
        type:-
            "my info" to check and update your details
            "homework" to check your home work
            "exam" to check your upcoming and current exams exams
            "fees" to check your fee record
            "exit" to log out''')
        s_choice1=input('enter your choice here:-')
        s_choice1=s_choice1.lower()
        a=1
        if s_choice1=='my info':        
            s_choice2=2
            while s_choice2!= 'close':
                if a==1:
                    mycursor.execute("SELECT * FROM students where r_no= " + '"' + m +'"' )
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        nnn.append(x)
                    print(tabulate(nnn,header1))
                    a=2
                print('''          type
                          
                          'edit' to edit information
                          'close' to go back to home page')''')
                s_choice2=input('enter u  choice:-')
                s_choice2=s_choice2.lower()
                if s_choice2=='edit':
                    t_rno_change=(input('enter your student id:-'))
                    print('''
                              
                              enter new details''')
                    a=t_rno_change
                    t_name_change=input('enter name :-')
                    t_pname_change=(input("enter father's name  \:-"))
                    sql = "UPDATE students SET student_name ="+"'" + t_name_change + "'" + ',parents_name=' + "'" + t_pname_change + "'" + ' WHERE r_no ='+"'"+a+"'"
                    mycursor.execute(sql)
                    db.commit()
                    a=1          
                    print(mycursor.rowcount, "record(s) affected")
                else:
                    print('enter a valid command')
        if s_choice1=='homework':
            s_choice2=2
            while s_choice2!= 'close':
                if a==1:                   
                    mycursor.execute("SELECT * FROM homework where r_no="+ '"' + m + '"')
                    myresult = mycursor.fetchall()
                    for x in myresult:    
                        print(tabulate(x))
                        a=2
                s_choice2=input('type "close" to go back to home page')
                s_choice2=s_choice2.lower()
                if s_choice2!='close':
                    print('enter a valid command')
        a=1
        if s_choice1=='exam':
    
            s_choice2=0
            while s_choice2!= 'close':
                if a==1:
                    mycursor.execute("SELECT * FROM exams")
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(tabulate(x))
                    a=2
                s_choice2=input('type "close" to go back to home page')
                s_choice2=s_choice2.lower()
                if s_choice2!='close':
                    print('enter a valid command')
        a=1
        if s_choice1=='fees':
            s_choice2=2
            while s_choice2!= 'close':
                if a==1:            
                    mycursor.execute("SELECT * FROM fees where r_no=" + '"' + m + '"')
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(tabulate(x))
                    a=2
                s_choice2 = input('enter your choice:-')
                if s_choice2 == 'reminders':
                    mycursor.execute("SELECT sr_no,date,remarks FROM fee_record where r_no=" + '"' + m + '"' +"or r_no ='all'")
                    myresult = mycursor.fetchall()
                    header=['sr_no','date','remarks']
                    for x in myresult:
                        print(tabulate(x,header))
                elif s_choice2!='close':
                    print('enter a valid command')    