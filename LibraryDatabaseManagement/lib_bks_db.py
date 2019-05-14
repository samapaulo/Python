import sqlite3


def connect_data():
    connect = sqlite3.connect("libbooks.db")
    current = connect.cursor()
    current.execute("CREATE TABLE IF NOT EXISTS libbooks (id INTEGER PRIMARY KEY, member_type text, reference text,\
                     book_id text, book_title text, title text, first_name text, surname text, author text,\
                    date_borrowed text, due_date text, address1 text, address2 text, postal_code text, days_on_loan text,\
                     late_fine text, overdue_date text, selling_price text, mobile_no text) ")
    connect.commit()
    connect.close()


def add_data_rec(member_type, reference, book_id, book_title, title, first_name, surname, author, due_date, address1,
                 address2, postal_code, days_on_loan, late_fine, date_borrowed, overdue_date, selling_price, mobile_no):
    connect = sqlite3.connect("libbooks.db")
    current = connect.cursor()
    current.execute("INSERT INTO libbooks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
                    (member_type, reference, book_id, book_title, title, first_name, surname, author, date_borrowed,
                     due_date, address1, address2, postal_code, days_on_loan, late_fine, overdue_date, selling_price,
                     mobile_no))
    connect.commit()
    connect.close()


def view_data():
    connect = sqlite3.connect("libbooks.db")
    current = connect.cursor()
    current.execute("SELECT * FROM libbooks")
    rows = current.fetchall()
    connect.close()
    return rows


def delete_rec(id):
    connect = sqlite3.connect("libbooks.db")
    current = connect.cursor()
    current.execute("DELETE FROM libbooks WHERE id=?", (id,))
    connect.commit()
    connect.close()


def delete_data():
    connect = sqlite3.connect("libbooks.db")
    current = connect.cursor()
    current.execute("DELETE FROM libbooks")
    connect.commit()
    connect.close()

    
def search_data(member_type="", reference="", book_id="", book_title="", title="", first_name="", surname="", author="",
                date_borrowed="", due_date="", address1="", address2="", postal_code="", days_on_loan="", late_fine="",
                overdue_date="", selling_price="", mobile_no=""):
    connect = sqlite3.connect("libbooks.db")
    current = connect.cursor()
    current.execute("SELECT * FROM libbooks WHERE member_type=? OR reference=? OR book_id=? OR book_title=? OR title=?\
                    OR first_name=? OR surname=? OR author=? OR date_borrowed=? OR due_date=? OR address1=? OR \
                    address2=? OR postal_code=? OR days_on_loan=? OR late_fine=? OR overdue_date=? OR selling_price=? OR\
                    mobile_no=?", (member_type, reference, book_id, book_title, title, first_name, surname, author,
                                   date_borrowed, due_date, address1, address2, postal_code, days_on_loan, late_fine,
                                   overdue_date, selling_price, mobile_no))
    rows = current.fetchall()
    connect.close()
    return rows


def update_data(id, member_type="", reference="", book_id="", book_title="", title="", first_name="", surname="",
                author="", date_borrowed="", due_date="", address1="", address2="", postal_code="", days_on_loan="",
                late_fine="", overdue_date="", selling_price="", mobile_no=""):
    connect = sqlite3.connect("libbooks.db")
    current = connect.cursor()
    current.execute("UPDATE libbooks SET member_type=?, reference=?, book_id=?, book_title=?, title=?, first_name=?,\
                    surname=?, author=?, date_borrowed=?, due_date=?, address1=?, address2=?, postal_code=?, \
                    days_on_loan=?, late_fine=?, overdue_date=?, selling_price=?, mobile_no=?",
                    (member_type, reference, book_id, book_title, title, first_name, surname, author, date_borrowed,
                     due_date, address1, address2, postal_code, days_on_loan, late_fine, overdue_date, selling_price,
                     mobile_no))
    connect.commit()
    connect.close()


connect_data()
