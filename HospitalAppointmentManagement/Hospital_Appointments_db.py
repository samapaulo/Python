import sqlite3

# Hospital Appointment Database Backend


def appointment_data():
    connect = sqlite3.connect("HospitalAppointments.db")
    current = connect.cursor()
    current.execute("CREATE TABLE IF NOT EXISTS appointments (id INTEGER PRIMARY KEY, patient_name text, age text,\
                    gender text, prognosis text, symptoms text, address text, city text, state text, country text, \
                    appointment_time text, phone_no text)")
    connect.commit()
    connect.close()


def add_patient_rec(patient_name, age, gender, prognosis, symptoms, address, city, state, country, appointment_time,
                    phone_no):
    connect = sqlite3.connect("HospitalAppointments.db")
    current = connect.cursor()
    current.execute("INSERT INTO appointments VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (patient_name, age,
                                                                                                gender, prognosis,
                                                                                                symptoms, address, city,
                                                                                                state, country,
                                                                                                appointment_time,
                                                                                                phone_no))
    connect.commit()
    connect.close()


def view_data():
    connect = sqlite3.connect("HospitalAppointments.db")
    current = connect.cursor()
    current.execute("SELECT * FROM appointments")
    rows = current.fetchall()
    connect.close()
    return rows


def delete_record(id):
    connect = sqlite3.connect("HospitalAppointments.db")
    current = connect.cursor()
    current.execute("DELETE FROM appointments where id=?", (id,))
    connect.commit()
    connect.close()


def delete_all_data():
    connect = sqlite3.connect("HospitalAppointments.db")
    current = connect.cursor()
    current.execute("DELETE FROM appointments")
    connect.commit()
    connect.close()


def search_data(patient_name="", age="", gender="", prognosis="", symptoms="", address="", city="", state="", country=""
                , appointment_time="", phone_no=""):
    connect = sqlite3.connect("HospitalAppointments.db")
    current = connect.cursor()
    current.execute("SELECT * FROM appointments WHERE patient_name=? OR age=? OR gender=? OR prognosis=? OR symptoms=? \
    OR address=? OR city=? OR state=? OR country=? OR appointment_time=? OR phone_no=?", (patient_name, age, gender,
                                                                                          prognosis, symptoms, address,
                                                                                          city, state, country,
                                                                                          appointment_time, phone_no))
    rows = current.fetchall()
    connect.close()
    return rows


def update_data(patient_name="", age="", gender="", prognosis="", symptoms="", address="", city="", state="", country=""
                , appointment_time="", phone_no=""):
    connect = sqlite3.connect("HospitalAppointments.db")
    current = connect.cursor()
    current.execute("UPDATE appointments SET patient_name=?, age=?, gender=?, prognosis=?, symptoms=?, address=?, \
    city=?, state=?, country=?, appointment_time=?, phone_no=?", (patient_name, age, gender, prognosis, symptoms,
                                                                  address, city, state, country, appointment_time,
                                                                  phone_no, id))
    connect.commit()
    connect.close()


appointment_data()
