import mysql.connector as mc
import pandas as pd
import sys
from tabulate import tabulate
db = mc.connect(host="localhost",
user="root", 
passwd="groot",
db="school") 
mycursor=db.cursor()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('''
      



''')
run_choice=0
print('''To go to login page ,type "login"

type 'exit' to close the program''' )
run_choice=(input('enter your choice:-')).lower()
while run_choice != 'exit':
        if run_choice == 'login':
            print('''How will you like to log in as a student(type s) or as a teacher(type t),to go back type 'exit' ''')
                  
            login_choice=(input('enter your login choice:-')).lower()
            l=0
            z=0 
            m=0      
            h=0
            p_choice=0
            n_choice=0
            l_choice2=0
            while l_choice2 != 'close':
                if login_choice=='t':
                    f=0
                    code=input('enter your ID number:-')
                    mycursor.execute("SELECT teacher_code FROM teacher_id ")
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        a=(''.join(x))
                        #print(a)
                        if code==a:
                            f=1
                            break
                    bhu =0
                    if f==1:
                       m=1
                    else:
                        abc=0
                        while abc !=1:
                            print('''Enter a valid code,the given code doesnt exist in the records
                                  You want to try again(type yes) or go back(type close)''')
                            l_choice2 = input('enter your choice:-')
                            
                            if l_choice2 == 'yes':
                                abc=1
                                continue
                            elif l_choice2 =='close':
                                abc=1
                                break
                            else:
                                        print('enter a valid command')
                    if m==1:
                    
                        while n_choice != 'close':
                            login_name=(input('enter your name:-')).lower()
                            mycursor.execute("SELECT teacher_name FROM teacher_id where teacher_code= " +'"'+a+'"')
                                
                            name_searched = (mycursor.fetchall())
                           
                            
                            m=0
                            name_searched = (name_searched[0][0])
                            name_searched = name_searched.lower()
                            r=0
                           
                            if name_searched == login_name:
                                if r==0:
                                    while p_choice!= 'close':
                                        enter_pass= (input('enter your password:-'))
                                        mycursor.execute("SELECT password FROM teacher_id where teacher_code= " +'"'+a+'"')
                                        l=0
                                        pass_searched = mycursor.fetchall()
                                        if pass_searched[0][0] == enter_pass:
                                            print('you have successfully logged in')
                                            l=1
                                            r=1
                                            break
                                        else:
                                            l=0
                                            r=0
                                            print('''password entered is incorrect.
                                                  You want to try again(type yes) or go back(type close)''' )
                                            p_choice = input('enter your choice:-')
                                            if p_choice == 'yes':
                                                continue
                                            elif p_choice =='close':
                                                break
                                            else:
                                                print('enter a valid command')
                            else:
                                print(''''The name you have entered does not match with your ID
                                      You want to try again(type yes) or go back(type close)''' )
                                n_choice = input('enter your choice:-')
                                if n_choice == 'yes':
                                    continue
                                elif n_choice =='close':
                                    break
                                else:
                                    print('enter a valid command')
                            break
                    break
                   
                if login_choice =='s':
            
                    code=input('enter your code number:-')
                    mycursor.execute("SELECT student_code FROM student_id ")
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        a=(''.join(x))
                        #print(a)
                        if code==a:
                            f=1
                            break
                    if f==1:
                        m=1
                    else:
                        abc=0
                    while abc !=1:
                        print('''Enter a valid code,the given code doesnt exist in the records
                              You want to try again(type yes) or go back(type close)''')
                        l_choice2 = input('enter your choice:-')
                        if l_choice2 == 'yes':
                            abc=1
                            continue
                        elif l_choice2 =='close':
                            abc=1
                            break
                        else:
                            print('enter a valid command')
                    if m==1:
                        while n_choice != 'close':
                            login_name=(input('enter your name:-')).lower()
                            mycursor.execute("SELECT student_name FROM student_id where student_code= " +'"'+a+'"')
                            name_searched = (mycursor.fetchall())
                            name_searched = (name_searched[0][0])
                            name_searched = name_searched.lower()
                            if name_searched == login_name:
                                while p_choice!= 'close':
                                    enter_pass= (input('enter your password:-'))
                                    mycursor.execute("SELECT password FROM student_id where student_code= " +'"'+a+'"')
                                    pass_searched = mycursor.fetchall()
                                    if pass_searched[0][0] == enter_pass:
                                        print('you have successfully logged in')
                                        z=1
                                        break
                                    else:
                                        z=0
                                        print('''password entered is incorrect.
                                              You want to try again(type yes) or go back(type close)''' )
                                    p_choice = input('enter your choice:-')
                                    if p_choice == 'yes':
                                        continue
                                    elif p_choice =='close':
                                        break
                                    else:
                                        print('enter a valid command')
                            else:
                                print(''''The name you have entered does not match with your ID
                                      You want to try again(type yes) or go back(type close)''' )
                                n_choice = input('enter your choice:-')
                                if n_choice == 'yes':
                                    continue
                                elif n_choice =='close':
                                    break
                                else:
                                    print('enter a valid command')
                                    break
                if login_choice =='exit': 
                    break
                if login_choice!='s' and login_choice!='t' and login_choice!='exit':
                    print('enter a valid command')
                    continue
                
        
        if l == 1:
            import teacher_part
        if z==1:
            import student_part
            student_part.student(code)
        
