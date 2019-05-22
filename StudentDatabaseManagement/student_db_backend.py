import sqlite3

# Student Database Backend


def student_data():
    connect = sqlite3.connect("student.db")
    current = connect.cursor()
    current.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, student_id text, first_name text,\
                    surname text, date_of_birth text, gov_id text, gender text, major text, address1 text, \
                    address2 text, mobile_no text)")
    connect.commit()
    connect.close()


def add_student_rec(student_id, first_name, surname, date_of_birth, gov_id, gender, major, address1, address2,
                    mobile_no):
    connect = sqlite3.connect("student.db")
    current = connect.cursor()
    current.execute("INSERT INTO student VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (student_id, first_name, surname,
                    date_of_birth, gov_id, gender, major, address1, address2, mobile_no))
    connect.commit()
    connect.close()


def view_data():
    connect = sqlite3.connect("student.db")
    current = connect.cursor()
    current.execute("SELECT * FROM student")
    rows = current.fetchall()
    connect.close()
    return rows


def delete_record(id):
    connect = sqlite3.connect("student.db")
    current = connect.cursor()
    current.execute("DELETE FROM student where id=?", (id,))
    connect.commit()
    connect.close()


def delete_all_data():
    connect = sqlite3.connect("student.db")
    current = connect.cursor()
    current.execute("DELETE FROM student")
    connect.commit()
    connect.close()


def search_data(student_id="", first_name="", surname="", date_of_birth="", gov_id="", gender="", major="",
                address1="", address2="", mobile_no=""):
    connect = sqlite3.connect("student.db")
    current = connect.cursor()
    current.execute("SELECT * FROM student WHERE student_id=? OR first_name=? OR surname=? OR date_of_birth=? OR \
    gov_id=? OR gender=? OR major=? OR address1=? OR address2=? OR mobile_no", (student_id, first_name, surname,
                                                                                date_of_birth, gov_id, gender, major,
                                                                                address1, address2, mobile_no))
    rows = current.fetchall()
    connect.close()
    return rows


def update_data(student_id="", first_name="", surname="", date_of_birth="", gov_id="", gender="", major="",
                address1="", address2="", mobile_no=""):
    connect = sqlite3.connect("student.db")
    current = connect.cursor()
    current.execute("UPDATE student SET student_id=?, first_name=?, surname=?, date_of_birth=?, gov_id=?, \
    gender=?, major=?, address1=?, address2=?, mobile_no", (student_id, first_name, surname, date_of_birth, gov_id,
                                                            gender, major, address1, address2, mobile_no, id))
    connect.commit()
    connect.close()


student_data()
