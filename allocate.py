### run before allocating ###

# 2. preference_locked=true
# 3. increase round number in a file

# fetch all students, fetch college id & seats, loop on them, get their preference in int list,
# loop on list and keep checking for availability in college seat, alloted id = college id, allotedseat--
import time

import mysql.connector


def get_preference_list(strpref):
    preference_list = list(strpref.split(" "))
    length = len(preference_list)
    index = 0
    for pref in preference_list:
        if index >= length:
            break
        l = int(pref)
        preference_list.remove(pref)
        preference_list.insert(index, l)
        index = index + 1
    return preference_list


mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='counselling')
cur = mydb.cursor()

file = open("database_crud/round_number.txt", 'r')
round_no = file.read(1)

if round_no == '0':
    stmt = '''UPDATE student 
    SET preference_list_locked={}'''.format(True)
    cur.execute(stmt)
    mydb.commit()
file.close()

file = open("database_crud/round_number.txt", 'w')
file.write('{}'.format(int(round_no)+1))
file.close()

college_dict = {}
college_stmt = "SELECT college_branch_id, actual_seats FROM college_branch"
cur.execute(college_stmt)
college_records = cur.fetchall()
for row in college_records:
    college_dict[row[0]] = row[1]

student_stmt = '''SELECT roll_no, preference_list, out_of_counselling FROM student
ORDER BY ranking'''
cur.execute(student_stmt)
student_records = cur.fetchall()

for row in student_records:
    if bool(row[2]) is True:
        continue
    pref_list = get_preference_list(row[1])
    for pref in pref_list:
        if college_dict[pref] > 0:
            allot_stmt = '''UPDATE student
            SET college_branch_alloted_id={}
            WHERE roll_no={}'''.format(pref, int(row[0]))
            cur.execute(allot_stmt)
            mydb.commit()
            college_dict[pref] = college_dict[pref] - 1
            break

mydb.close()
cur.close()
