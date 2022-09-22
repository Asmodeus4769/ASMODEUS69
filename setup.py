import mysql.connector
def create_database() :
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root")

    cursor = db.cursor()
    create_db = '''CREATE DATABASE counselling'''

    cursor.execute(create_db)
    cursor.close()
    db.close()

def setup_tables() :
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="counselling")
    cur = db.cursor()

    create_student_stmt = "CREATE TABLE student (roll_no INT, ranking INT, passwd VARCHAR(255), name VARCHAR(255), preference_list VARCHAR(1000), preference_list_locked BOOLEAN, college_branch_alloted_id INT, college_branch_selected_id INT, out_of_counselling BOOLEAN, PRIMARY KEY(roll_no))"
    cur.execute(create_student_stmt)
    print("student table created")

    create_college_branch_stmt = "CREATE TABLE college_branch (college_branch_id INT, name VARCHAR(255), actual_seats INT, PRIMARY KEY(college_branch_id))"
    cur.execute(create_college_branch_stmt)
    print("college_branch table created")

    db.close()
    cur.close()

def initialize_tables_for_test() :
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="counselling")
    cur = db.cursor()

    insert_college_stmt = "INSERT INTO college_branch (college_branch_id, name, actual_seats) VALUES (%s, %s, %s)"
    colleges_to_insert = [(1, 'IIT Bombay CSE', 3),
                          (2, 'IIT Delhi CSE', 4),
                          (3, 'IIT Delhi ECE', 2),
                          (4, 'IIT Bombay ECE', 5),
                          (5, 'IIT Madras CSE', 4)]
    cur.executemany(insert_college_stmt, colleges_to_insert)
    db.commit()
    print("colleges inserted")

    insert_student_stmt = '''INSERT INTO
        student (roll_no, ranking, passwd, name, preference_list, preference_list_locked, out_of_counselling)
    VALUES
        (1, 15, '30052002', 'A', '1 2 3 4 5', FALSE, FALSE),
        (2, 11, '22082001', 'B', '1 2 3 4 5', FALSE, FALSE),
        (3, 7, '25052002', 'C', '1 2 3 4 5', FALSE, FALSE),
        (4, 16, '02082003', 'D', '1 2 3 4 5', FALSE, FALSE),
        (5, 5, '27122000', 'E', '1 2 3 4 5', FALSE, FALSE),
        (6, 17, '28082003', 'F', '1 2 3 4 5', FALSE, FALSE),
        (7, 9, '03112002', 'G', '1 2 3 4 5', FALSE, FALSE),
        (8, 1, '26092003', 'H', '1 2 3 4 5', FALSE, FALSE),
        (9, 10, '22092001', 'I', '1 2 3 4 5', FALSE, FALSE),
        (10, 18, '17042000', 'J', '1 2 3 4 5', FALSE, FALSE),
        (11, 12, '10092000', 'K', '1 2 3 4 5', FALSE, FALSE),
        (12, 19, '25042000', 'L', '1 2 3 4 5', FALSE, FALSE),
        (13, 4, '21032001', 'M', '1 2 3 4 5', FALSE, FALSE),
        (14, 20, '01012003', 'N', '1 2 3 4 5', FALSE, FALSE),
        (15, 13, '24022000', 'O', '1 2 3 4 5', FALSE, FALSE),
        (16, 8, '25092000', 'P', '1 2 3 4 5', FALSE, FALSE),
        (17, 14, '09042002', 'Q', '1 2 3 4 5', FALSE, FALSE),
        (18, 2, '21062002', 'R', '1 2 3 4 5', FALSE, FALSE),
        (19, 6, '12102000', 'S', '1 2 3 4 5', FALSE, FALSE),
        (20, 3, '14042002', 'T', '1 2 3 4 5', FALSE, FALSE)'''
    cur.execute(insert_student_stmt)
    db.commit()
    print("students inserted")

    db.close()
    cur.close()


create_database()
setup_tables()
initialize_tables_for_test()