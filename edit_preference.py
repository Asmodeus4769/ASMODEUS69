import time

import mysql.connector
from database_crud.view_preference import view_preference

def lock_preference(roll_no):
    mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='counselling')
    cur = mydb.cursor()
    lock_stmt = '''UPDATE student
    SET preference_list_locked={}
    WHERE roll_no={}'''.format(True, roll_no)
    cur.execute(lock_stmt)
    mydb.commit()
    mydb.close()
    cur.close()
    print("preference list locked!! now you can't edit it.")
    return

def edit_preference(roll_no, college_dict):
    view_preference(roll_no, college_dict)
    time.sleep(2)

    mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='counselling')
    cur = mydb.cursor()
    stmt = '''SELECT preference_list FROM student where roll_no={}'''.format(roll_no)
    cur.execute(stmt)
    records = cur.fetchall()
    preference = ""
    for row in records:
        preference = row[0]
    preference_list = list(preference.split(" "))

    length = len(preference_list)

    while True:
        a1 = int(input("Don't want to change preference?(enter 1 for yes) "))
        if a1 == 1:
            return

        print("\nIDs for colleges:")
        index = 0
        for key, value in college_dict.items():
            index += 1
            print("{}. {} : {}".format(index, value, key))

        c = input("Which college's position you want to change, enter its id: ")

        if c not in preference_list:
            print("You entered wrong id, try again!!")
            continue

        preference_list.remove(c)

        new_position = int(input("where do you want to place it? Enter position. "))
        if new_position > length:
            new_position = length

        if new_position <= 0:
            new_position = 1

        preference_list.insert(new_position-1, c)

        choice = int(input("Done with changes?(enter 1 for yes) "))
        if choice == 1:
            strpreference = ' '.join([str(elem) for elem in preference_list])
            update_pref_stmt = '''UPDATE student
            SET preference_list='{}'
            WHERE roll_no={}'''.format(strpreference, roll_no)
            cur.execute(update_pref_stmt)
            mydb.commit()
            print("Preference changed!!")
            view_preference(roll_no, college_dict)
            mydb.close()
            cur.close()

            lock = int(input("Do you want to lock your choices?(enter 1 for yes) "))
            if lock == 1:
                lock_preference(roll_no)
            return

