import mysql.connector

def change_password(roll_no):
    new_password = input("Enter new password. ")
    mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='counselling')
    cur = mydb.cursor()
    stmt = '''UPDATE student
    SET passwd='{}'
    WHERE roll_no={}'''.format(new_password, roll_no)
    cur.execute(stmt)
    mydb.commit()
    print("Password changed.")
    mydb.close()
    cur.close()
    return