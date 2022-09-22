import time
from os import system
import mysql.connector
from database_crud.login import show_options_after_login

while True:
    _ = system('clear')
    print("--------------------------------Welcome to College Counselling Management---------------------------------------\n")

    roll_no = int(input("Enter your roll no. "))
    password = input("Enter password(Enter date-of-birth in (ddmmyyyy) format if logging in for the first time) ")

    db = mysql.connector.connect(host='localhost', user='root', password='root', database="counselling")
    cur = db.cursor()
    stmt = "select passwd from student where roll_no={}".format(roll_no)
    cur.execute(stmt)
    records = cur.fetchall()
    for row in records:
        if row[0] == password:
            print("login successful")
            time.sleep(1)
            _ = system('clear')
            show_options_after_login(roll_no)
            break
    else:
        print("either roll_no/password is wrong, try again.")

    c = int(input("Want to exit?(1 for yes) "))
    if c == 1:
        break
