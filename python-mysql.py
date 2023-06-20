import mysql.connector
print("welcome")
print('''press one of the following to select your login type
press a for teacher log in
press b for student log in
press c for parents log in''')
n=(input('enter your choice'))
n=n.lower()
if n=='a':
    print('You will be logged in as a teacher')
elif n=='b':
    print('You wil be logged in as a student')
elif n=='c':
    print('You wil be logged in as a parent')
else:
    print("please select a valid option")
mydb=mysql.connector.connect(host="localhost",user="yourusername",password="yourpassword")

print(mydb) 
