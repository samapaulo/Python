from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import Hospital_Appointments_db


class HospitalAppointment:

    def __init__(self, space):
        self.space = space
        self.space.title("Hospital Appointment Database System")
        self.space.geometry("1350x600+0+0")

    # =========== Variable Declaration ================================================================================#

        patient_name = StringVar()
        age = StringVar()
        gender = StringVar()
        prognosis = StringVar()
        symptoms = StringVar()
        address = StringVar()
        city = StringVar()
        state = StringVar()
        country = StringVar()
        appointment_time = StringVar()
        phone_no = StringVar()

    # =================================================================================================================#

    # ==================== Functions ==================================================================================#

        def i_exit():
            i_exit = tkinter.messagebox.askyesno("Hospital Appointments System", "Confirm if you want to exit")
            if i_exit > 0:
                space.destroy()
                return

        def add_data():
            if len(patient_name.get()) != 0:
                Hospital_Appointments_db.add_patient_rec(patient_name.get(), age.get(), gender.get(), prognosis.get(),
                                                         symptoms.get(), address.get(), city.get(), state.get(),
                                                         country.get(), appointment_time.get(), phone_no.get())
                patient_list.delete(0, END)
                patient_list.insert(patient_name.get(), age.get(), gender.get(), prognosis.get(), symptoms.get(),
                                    address.get(), city.get(), state.get(), country.get(), appointment_time.get(),
                                    phone_no.get())

        def clear_data():
            self.txt_patient_name.delete(0, END)
            self.txt_age.delete(0, END)
            self.txt_gender.delete(0, END)
            self.txt_prognosis.delete(0, END)
            self.txt_symptoms.delete(0, END)
            self.txt_address.delete(0, END)
            self.txt_city.delete(0, END)
            self.txt_state.delete(0, END)
            self.txt_country.delete(0, END)
            self.txt_appointment_time.delete(0, END)
            self.txt_phone_no.delete(0, END)

        def display_data():
            patient_list.delete(0, END)
            count = 0
            for row in Hospital_Appointments_db.view_data():
                count = count + 1
                patient_list.insert(END, row, str(""))
            patient_list.insert(END, "Total Patient Appointments are: " + str(count))

        def patient_select(event):
            global patient_rec
            search_patient = patient_list.curselection()[0]
            patient_rec = patient_list.get(search_patient)

            self.txt_gender = ttk.Combobox(data_frame_left, font=('verdana 12 bold'), textvariable=gender, width=24,
                                           state='enable', values=['Male', 'Female'])
            self.txt_gender.grid(row=2, column=1)

            self.txt_patient_name.delete(0, END)
            self.txt_patient_name.insert(END, patient_rec[1])
            self.txt_age.delete(0, END)
            self.txt_age.insert(END, patient_rec[2])
            self.txt_gender.delete(0, END)
            self.txt_gender.insert(END, patient_rec[3])
            self.txt_prognosis.delete(0, END)
            self.txt_prognosis.insert(END, patient_rec[4])
            self.txt_symptoms.delete(0, END)
            self.txt_symptoms.insert(END, patient_rec[5])
            self.txt_address.delete(0, END)
            self.txt_address.insert(END, patient_rec[6])
            self.txt_city.delete(0, END)
            self.txt_city.insert(END, patient_rec[7])
            self.txt_state.delete(0, END)
            self.txt_state.insert(END, patient_rec[8])
            self.txt_country.delete(0, END)
            self.txt_country.insert(END, patient_rec[9])
            self.txt_appointment_time.delete(0, END)
            self.txt_appointment_time.insert(END, patient_rec[10])
            self.txt_phone_no.delete(0, END)
            self.txt_phone_no.insert(END, patient_rec[11])

        def delete_data():
            i_del = tkinter.messagebox.askyesno("Hospital Appointment Database System", "Confirm if you want to exit")
            if i_del > 0:
                if len(patient_name.get()) != 0:
                    Hospital_Appointments_db.delete_record(patient_rec[0])
                    clear_data()
                    display_data()
                    return

        def delete_db_data():
            i_del = tkinter.messagebox.askyesno("Hospital Appointment Database System", "Do you really want to DELETE \
                                                                                        ALL your appointments?")
            if i_del > 0:
                Hospital_Appointments_db.delete_all_data()
                clear_data()
                display_data()
                return

        def search_db():
            patient_list.delete(0, END)
            for row in Hospital_Appointments_db.search_data(patient_name.get(), age.get(), gender.get(), prognosis.get(),
                                                            symptoms.get(), address.get(), city.get(), state.get(),
                                                            country.get(), appointment_time.get(), phone_no.get()):
                patient_list.insert(END, row, str(""))

        def update_db():
            if len(patient_name.get()) != 0:
                Hospital_Appointments_db.delete_record(patient_rec[0])
            if len(patient_name.get()) != 0:
                Hospital_Appointments_db.add_patient_rec(patient_name.get(), age.get(), gender.get(), prognosis.get(),
                                                         symptoms.get(), address.get(), city.get(), state.get(),
                                                         country.get(), appointment_time.get(), phone_no.get())
                patient_list.delete(0, END)
                patient_list.insert(END, (patient_name.get(), age.get(), gender.get(), prognosis.get(), symptoms.get(),
                                          address.get(), city.get(), state.get(), country.get(), appointment_time.get(),
                                          phone_no.get()))
    # =================================================================================================================#

    # ==================== Frame Setup ================================================================================#

        main_frame = Frame(self.space, bg="gray18")
        main_frame.grid()

        title_frame = Frame(main_frame, bd=2, padx=40, pady=8, bg='gray18')
        title_frame.pack(side=TOP)

        self.lbl_title = Label(title_frame, font=('Arial 40 bold'), text=" Hospital Appointment Database System",
                               bg='gray18', fg='white')
        self.lbl_title.grid(sticky=W)

        button_frame = Frame(main_frame, bd=2, width=1350, height=350, padx=20, pady=20, bg='gray18')
        button_frame.pack(side=BOTTOM)

        data_frame = Frame(main_frame, bd=1, width=1350, height=200, padx=20, pady=20, bg="gray18")
        data_frame.pack(side=BOTTOM)

        data_frame_left = LabelFrame(data_frame, bd=1, width=500, height=200, padx=30, font=('courier 15 bold'),
                                     text="Patient Information:", bg='gray18', fg='white')
        data_frame_left.pack(side=LEFT)

        data_frame_right = LabelFrame(data_frame, bd=1, width=800, height=200, padx=30, font=('courier 15 bold'),
                                      text="Patient Appointments:", bg='gray18', fg='white')
        data_frame_right.pack(side=RIGHT)

        # =============================================================================================================#

        # ============ Left Frame Data Entry Setup ====================================================================#

        self.lbl_patient_name = Label(data_frame_left, font=('verdana 12 bold'), text="Patient Name:", padx=2, pady=5,
                                      bg='gray18', fg='white')
        self.lbl_patient_name.grid(row=0, column=0, sticky=W)
        self.txt_patient_name = Entry(data_frame_left, font=('verdana 12 bold'), textvariable=patient_name, width=25,
                                      fg='blue')
        self.txt_patient_name.grid(row=0, column=1)

        self.lbl_age = Label(data_frame_left, font=('verdana 12 bold'), text="Age:", padx=2, pady=5, bg='gray18',
                             fg='white')
        self.lbl_age.grid(row=1, column=0, sticky=W)
        self.txt_age = Entry(data_frame_left, font=('verdana 12 bold'), textvariable=age, width=25, fg='blue')
        self.txt_age.grid(row=1, column=1)

        self.lbl_gender = Label(data_frame_left, font=('verdana 12 bold'), text="Gender:", padx=2, pady=4, bg='gray18',
                                fg='white')
        self.lbl_gender.grid(row=2, column=0, sticky=W)
        self.txt_gender = ttk.Combobox(data_frame_left, font=('verdana 12 bold'), textvariable=gender, width=24,
                                       state='readonly', values=['Male', 'Female'])
        self.txt_gender.grid(row=2, column=1)

        self.lbl_prognosis = Label(data_frame_left, font=('verdana 12 bold'), text="Medical Condition:", padx=2, pady=5,
                                   bg='gray18', fg='white')
        self.lbl_prognosis.grid(row=3, column=0, sticky=W)
        self.txt_prognosis = Entry(data_frame_left, font=('verdana 12 bold'), textvariable=prognosis, width=25,
                                   fg='blue')
        self.txt_prognosis.grid(row=3, column=1)

        self.lbl_symptoms = Label(data_frame_left, font=('verdana 12 bold'), text="Symptoms:", padx=2, pady=5,
                                  bg='gray18', fg='white')
        self.lbl_symptoms.grid(row=4, column=0, sticky=W)
        self.txt_symptoms = Entry(data_frame_left, font=('verdana 12 bold'), textvariable=symptoms, width=25, fg='blue')
        self.txt_symptoms.grid(row=4, column=1)

        self.lbl_address = Label(data_frame_left, font=('verdana 12 bold'), text="Address:", padx=2, pady=5, bg='gray18'
                                 , fg='white')
        self.lbl_address.grid(row=5, column=0, sticky=W)
        self.txt_address = Entry(data_frame_left, font=('verdana 12 bold'), textvariable=address, width=25, fg='blue')
        self.txt_address.grid(row=5, column=1)

        self.lbl_city = Label(data_frame_left, font=('verdana 12 bold'), text="City:", padx=2, pady=5, bg='gray18',
                              fg='white')
        self.lbl_city.grid(row=6, column=0, sticky=W)
        self.txt_city = Entry(data_frame_left, font=('verdana 12 bold'), textvariable=city, width=25, fg='blue')
        self.txt_city.grid(row=6, column=1)

        self.lbl_state = Label(data_frame_left, font=('verdana 12 bold'), text="State/Province/County:", padx=2, pady=5,
                               bg='gray18', fg='white')
        self.lbl_state.grid(row=7, column=0, sticky=W)
        self.txt_state = Entry(data_frame_left, font=('verdana 12 bold'), textvariable=state, width=25, fg='blue')
        self.txt_state.grid(row=7, column=1)

        self.lbl_country = Label(data_frame_left, font=('verdana 12 bold'), text="Country:", padx=2, pady=5, bg='gray18'
                                 , fg='white')
        self.lbl_country.grid(row=8, column=0, sticky=W)
        self.txt_country = Entry(data_frame_left, font=('verdana 12 bold'), textvariable=country, width=25, fg='blue')
        self.txt_country.grid(row=8, column=1)

        self.lbl_appointment_time = Label(data_frame_left, font=('verdana 12 bold'), text="Appointment Time:", padx=2,
                                          pady=5, bg='gray18', fg='white')
        self.lbl_appointment_time.grid(row=9, column=0, sticky=W)
        self.txt_appointment_time = Entry(data_frame_left, font=('verdana 12 bold'), textvariable=appointment_time,
                                          width=25, fg='blue')
        self.txt_appointment_time.grid(row=9, column=1)

        self.lbl_phone_no = Label(data_frame_left, font=('verdana 12 bold'), text="Phone Number:", padx=2, pady=5,
                                  bg='gray18', fg='white')
        self.lbl_phone_no.grid(row=10, column=0, sticky=W)
        self.txt_phone_no = Entry(data_frame_left, font=('verdana 12 bold'), textvariable=phone_no, width=25, fg='blue')
        self.txt_phone_no.grid(row=10, column=1)

        # ============== Patient Appointments Box =====================================================================#

        scrollbar = Scrollbar(data_frame_right)
        scrollbar.grid(row=0, column=1, sticky='ns')

        patient_list = Listbox(data_frame_right, width=77, height=14, font=('Helvetica 12 bold'),
                               yscrollcommand=scrollbar.set)
        patient_list.bind('<<ListboxSelect>>', patient_select)
        patient_list.grid(row=0, column=0, padx=2)
        scrollbar.config(command=patient_list.yview)

        # =============================================================================================================#

        # ============= Buttons Setup =================================================================================#
        self.button_add_data = Button(button_frame, text='Add Appointment', font=('Helvetica 10 bold'), height=2,
                                      width=18, bd=5, command=add_data)
        self.button_add_data.grid(row=0, column=0)

        self.button_display_data = Button(button_frame, text='Display Appointments', font=('Helvetica 10 bold'),
                                          height=2, width=18, bd=5, command=display_data)
        self.button_display_data.grid(row=0, column=1)

        self.button_clear_data = Button(button_frame, text='Clear Entries', font=('Helvetica 10 bold'), height=2,
                                        width=18, bd=5, command=clear_data)
        self.button_clear_data.grid(row=0, column=2)

        self.button_delete_data = Button(button_frame, text='Delete Appointment', font=('Helvetica 10 bold'), height=2,
                                         width=18, bd=5, command=delete_data)
        self.button_delete_data.grid(row=0, column=3)

        self.button_update_data = Button(button_frame, text='Update Appointment', font=('Helvetica 10 bold'), height=2,
                                         width=18, bd=5, command=update_db)
        self.button_update_data.grid(row=0, column=4)

        self.button_search_data = Button(button_frame, text='Search Appointment', font=('Helvetica 10 bold'), height=2,
                                         width=18, bd=5, command=search_db)
        self.button_search_data.grid(row=0, column=5)

        self.button_delete_all_data = Button(button_frame, text='Delete All Appointments', font=('Helvetica 10 bold'),
                                             height=2, width=18, bd=5, command=delete_db_data)
        self.button_delete_all_data.grid(row=0, column=6)

        self.button_exit = Button(button_frame, text='Exit', font=('Helvetica 10 bold'), height=2, width=18, bd=5,
                                  command=i_exit)
        self.button_exit.grid(row=0, column=7)

        # =============================================================================================================#


if __name__ == '__main__':
    space = Tk()
    application = HospitalAppointment(space)
    space.mainloop()
