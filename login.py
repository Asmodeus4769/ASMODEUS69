import time
from os import system
import mysql.connector
from database_crud.change_password import change_password
from database_crud.view_preference import preference
from database_crud.edit_preference import edit_preference
from database_crud.view_alloted_seat import view_alloted_seat


def get_college_list():
    db = mysql.connector.connect(host='localhost', user='root', password='root', database="counselling")
    cur = db.cursor()
    college_dict = {}
    college_stmt = "SELECT college_branch_id, name FROM college_branch"
    cur.execute(college_stmt)
    college_records = cur.fetchall()
    for row in college_records:
        college_dict[row[0]] = row[1]
    return college_dict

def show_options_after_login(roll_no):
    db = mysql.connector.connect(host='localhost', user='root', password='root', database="counselling")
    cur = db.cursor()
    stmt = "select name from student where roll_no={}".format(roll_no)
    cur.execute(stmt)
    records = cur.fetchall()
    name = ""
    for row in records:
        name = row[0]
    db.close()
    cur.close()

    while True:
        time.sleep(1)
        _ = system('clear')
        print("--------Hi " + name + ", Welcome to College Counselling Management---------\n")
        time.sleep(1)
        db = mysql.connector.connect(host='localhost', user='root', password='root', database="counselling")
        cur = db.cursor()
        stmt = "select preference_list_locked, out_of_counselling from student where roll_no={}".format(roll_no)
        cur.execute(stmt)
        records = cur.fetchall()
        preference_list_locked = False
        out_of_counselling = False
        for row in records:
            preference_list_locked = bool(row[0])
            out_of_counselling = bool(row[1])

        file = open("database_crud/round_number.txt", 'r')
        round_no = int(file.read(1))
        file.close()

        print("Press 1 for changing password")
        print("Press 2 for viewing current preference")
        if preference_list_locked is False:
            print("Press 3 for editing preference")
        elif out_of_counselling is True:
            print("Press 3 for selected seat")
        elif round_no > 0:
            print("Press 3 for viewing alloted seat")
        print("Press 0 for log out")

        c = int(input("Enter your Choice "))

        if c == 0:
            print("You logged out!!")
            time.sleep(1)
            db.close()
            cur.close()
            return
        if c == 1:
            change_password(roll_no)
        elif c == 2:
            preference(roll_no, get_college_list())
        elif c == 3:
            if preference_list_locked is False:
                edit_preference(roll_no, get_college_list())

            elif out_of_counselling is True:
                seat_query = "SELECT college_branch_selected_id FROM student where roll_no={}".format(roll_no)
                cur.execute(seat_query)
                seats = cur.fetchall()
                for row in seats:
                    seat = row[0]
                if seat is None:
                    print("You've opted out of the process. No seat selected.")
                else:
                    print("Congratulations!! You got selected in: "+get_college_list()[int(seat)])
                time.sleep(5)

            elif round_no > 0:
                view_alloted_seat(roll_no)

        else:
            print("enter right choice")
