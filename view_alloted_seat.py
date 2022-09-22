import mysql.connector

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

def opt_out(roll_no):
    mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='counselling')
    cur = mydb.cursor()
    opt_out_stmt = '''UPDATE student
    SET out_of_counselling={}
    WHERE roll_no={}'''.format(True, roll_no)
    cur.execute(opt_out_stmt)
    mydb.commit()
    mydb.close()
    cur.close()
    print("Opted out of counselling process")
    return


def freeze(roll_no, alloted_seat):
    mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='counselling')
    cur = mydb.cursor()
    freeze_stmt = '''UPDATE student
    SET college_branch_selected_id={}
    WHERE roll_no={}'''.format(alloted_seat, roll_no)
    cur.execute(freeze_stmt)
    mydb.commit()

    reduce_stmt = '''UPDATE college_branch
    SET actual_seats=actual_seats-1
    WHERE college_branch_id={}'''.format(alloted_seat)
    cur.execute(reduce_stmt)
    mydb.commit()

    mydb.close()
    cur.close()
    opt_out(roll_no)
    print("Congratulations!! You've selected a choice.")
    return


def view_alloted_seat(roll_no):
    mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='counselling')
    cur = mydb.cursor()
    stmt = '''SELECT college_branch_alloted_id FROM student where roll_no={}'''.format(roll_no)
    cur.execute(stmt)
    records = cur.fetchall()
    for row in records:
        alloted_seat = row[0]

    if alloted_seat is None:
        print("Please wait for other rounds of allotment!! Seats are lesser, someone might opt out.")
    else:
        print("Your alloted seat would be: "+get_college_list()[int(alloted_seat)])

    mydb.close()
    cur.close()

    while True:
        print("Press 0 for returning")
        if alloted_seat is not None:
            print("Press 1 for freezing the choice")
            print("Press 2 for floating the choice and wait for next round result.")
        print("Press 3 for opting out of counselling")

        c = int(input("Enter your choice"))
        if c == 0:
            return
        elif c == 1:
            freeze(roll_no, int(alloted_seat))
        elif c == 2:
            print("See you in next round!!")
        elif c == 3:
            opt_out(roll_no)
        else:
            print("Enter right choice")
