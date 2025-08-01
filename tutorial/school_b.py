import sqlite3 

# Connect to the database

def add_student(cursor, name, age, major):
    try:
        cursor.execute("INSERT INTO Students (name, age, major) VALUES (?,?,?)", (name, age, major))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_course(cursor, name, instructor):
    try:
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?,?)", (name, instructor))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def enroll_student(cursor, student, course):
    cursor.execute("SELECT * FROM Students WHERE name = ?", (student,)) # For a tuple with one element, you need to include the comma
    results = cursor.fetchall()
    if len(results) > 0:
        student_id = results[0][0]
    else:
        print(f"There was no student named {student}.")
        return
    cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
    results = cursor.fetchall()
    if len(results) > 0:
        course_id = results[0][0]
    else:
        print(f"There was no course named {course}.")
        return
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
    # cursor.execute("INSERT INTO Enrollments (student_id, course_id) (95, 43)")
    cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Student {student} is already enrolled in course {course}.")
        return

with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Insert sample data into tables

    add_student(cursor, 'Alice', 20, 'Computer Science')  
    add_student(cursor, 'Bob', 22, 'History')
    add_student(cursor, 'Charlie', 19, 'Biology')
    add_course(cursor, 'Math 101', 'Dr. Smith')
    add_course(cursor, 'English 101', 'Ms. Jones')
    add_course(cursor, 'Chemistry 101', 'Dr. Lee')

    conn.commit() 
    # And at the bottom of your "with" block
    enroll_student(cursor, "Alice", "Math 101")
    enroll_student(cursor, "Alice", "Chemistry 101")
    enroll_student(cursor, "Bob", "Math 101")
    enroll_student(cursor, "Bob", "English 101")
    enroll_student(cursor, "Charlie", "English 101")
    conn.commit() # more writes, so we have to commit to make them final!
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.")


    # cursor.execute("SELECT * FROM Students WHERE name = 'Alice'")


    # cursor.execute("SELECT * FROM Courses WHERE course_name LIKE 'math%'")
    # cursor.execute("SELECT Students.name, Course.course_name FROM Students JOIN Enrollments ON Students.student_id = Enrollments.student_id JOIN Courses ON Enrollments.course_id = Courses.course_id")
    # cursor.execute("SELECT s.name, c.course_name FROM Students AS s JOIN Enrollments AS e ON s.student_id = e.student_id JOIN Courses AS c ON e.course_id = c.course_id")
    # cursor.execute("SELECT s.name, c.course_name FROM Students s JOIN Enrollments e ON s.student_id = e.student_id JOIN Courses c ON e.course_id = c.course_id")
    # cursor.execute("SELECT c.customer_name, o.order_id FROM customers c LEFT JOIN orders o on c.customer_id = o.customer_id")
    # cursor.execute("SELECT Students.name, Courses.course_name 
# FROM Enrollments
# JOIN Students ON Enrollments.student_id = Students.student_id
# JOIN Courses ON Enrollments.course_id = Courses.course_id;")


    result = cursor.fetchall()
    for row in result:
        print(row)

