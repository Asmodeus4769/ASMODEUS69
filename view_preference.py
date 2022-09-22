import time

import mysql.connector

def view_preference(roll_no, college_dict):
    mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='counselling')
    cur = mydb.cursor()
    stmt = '''SELECT preference_list FROM student where roll_no={}'''.format(roll_no)
    cur.execute(stmt)
    records = cur.fetchall()
    preference = ""
    for row in records:
        preference = row[0]
    preference_list = list(preference.split(" "))
    index = 0
    print("Your current preference is: ")
    for choice in preference_list:
        index = index + 1
        print("{}. {}".format(index, college_dict[int(choice)]))
    mydb.close()
    cur.close()

def preference(roll_no, college_dict):

    view_preference(roll_no, college_dict)

    print("Enter 1 if you want to return to main menu. ")
    while True:
        c = int(input())
        if c == 1:
            return
        else:
            continue
