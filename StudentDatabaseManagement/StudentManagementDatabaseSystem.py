from tkinter import *
import tkinter.messagebox
import student_db_backend


class StudentDB:

    def __init__(self, space):
        self.space = space
        self.space.title("Student Database Management System")
        self.space.geometry("1350x555+0+0")

    # ========= Variable Declaration ==================================================================================#

        student_id = StringVar()
        first_name = StringVar()
        surname = StringVar()
        date_of_birth = StringVar()
        gov_id = StringVar()
        gender = StringVar()
        major = StringVar()
        address1 = StringVar()
        address2 = StringVar()
        mobile_no = StringVar()

    # =================================================================================================================#

    # ================= Functions Declaration =========================================================================#

        def i_exit():
            i_exit = tkinter.messagebox.askyesno("Student Database Management System", "Confirm if you want to exit")

            if i_exit > 0:
                space.destroy()
                return

        def clear_data():
            self.txt_student_id.delete(0, END)
            self.txt_first_name.delete(0, END)
            self.txt_surname.delete(0, END)
            self.txt_date_of_birth.delete(0, END)
            self.txt_gov_id.delete(0, END)
            self.txt_gender.delete(0, END)
            self.txt_major.delete(0, END)
            self.txt_address1.delete(0, END)
            self.txt_address2.delete(0, END)
            self.txt_mobile_no.delete(0, END)

        def add_data():
            if len(student_id.get()) != 0:
                student_db_backend.add_student_rec(student_id.get(), first_name.get(), surname.get(),
                                                   date_of_birth.get(), gov_id.get(), gender.get(), major.get(),
                                                   address1.get(), address2.get(), mobile_no.get())
                student_list.delete(0, END)
                student_list.insert(student_id.get(), first_name.get(), surname.get(), date_of_birth.get(), gov_id.get(),
                                    gender.get(), major.get(), address1.get(), address2.get(), mobile_no.get())

        def display_data():
            student_list.delete(0, END)
            for row in student_db_backend.view_data():
                student_list.insert(END, row, str(""))

        def student_select(event):
            global student_rec
            search_student = student_list.curselection()[0]
            student_rec = student_list.get(search_student)

            self.txt_student_id.delete(0, END)
            self.txt_student_id.insert(END, student_rec[1])
            self.txt_first_name.delete(0, END)
            self.txt_first_name.insert(END, student_rec[2])
            self.txt_surname.delete(0, END)
            self.txt_surname.insert(END, student_rec[3])
            self.txt_date_of_birth.delete(0, END)
            self.txt_date_of_birth.insert(END, student_rec[4])
            self.txt_gov_id.delete(0, END)
            self.txt_gov_id.insert(END, student_rec[5])
            self.txt_gender.delete(0, END)
            self.txt_gender.insert(END, student_rec[6])
            self.txt_major.delete(0, END)
            self.txt_major.insert(END, student_rec[7])
            self.txt_address1.delete(0, END)
            self.txt_address1.insert(END, student_rec[8])
            self.txt_address2.delete(0, END)
            self.txt_address2.insert(END, student_rec[9])
            self.txt_mobile_no.delete(0, END)
            self.txt_mobile_no.insert(END, student_rec[10])

        def delete_data():
            i_del = tkinter.messagebox.askyesno("Student Database Management System", "Confirm if you want to exit")
            if i_del > 0:
                if len(student_id.get()) != 0:
                    student_db_backend.delete_record(student_rec[0])
                    clear_data()
                    display_data()
                    return

        def delete_db_data():
            i_del = tkinter.messagebox.askyesno("Student Database Management System", "Do you really want to delete ALL\
                                                                                      your data?")
            if i_del > 0:
                student_db_backend.delete_all_data()
                clear_data()
                display_data()
                return

        def search_db():
            student_list.delete(0, END)
            for row in student_db_backend.search_data(student_id.get(), first_name.get(), surname.get(),
                                                      date_of_birth.get(), gender.get(), gov_id.get(), major.get(),
                                                      address1.get(), address2.get(), mobile_no.get()):
                student_list.insert(END, row, str(""))

        def update_db():
            if len(student_id.get()) != 0:
                student_db_backend.delete_record(student_rec[0])
            if len(student_id.get()) != 0:
                student_db_backend.add_student_rec(student_id.get(), first_name.get(), surname.get(),
                                                   date_of_birth.get(), gender.get(), gov_id.get(), major.get(),
                                                   address1.get(), address2.get(), mobile_no.get())
                student_list.delete(0, END)
                student_list.insert(END, (student_id.get(), first_name.get(), surname.get(), date_of_birth.get(),
                                          gender.get(), gov_id.get(), major.get(), address1.get(), address2.get(),
                                          mobile_no.get()))

    # =============================================================:====================================================#

    # ================= Frame Setup ===================================================================================#

        main_frame = Frame(self.space, bg="teal")
        main_frame.grid()

        title_frame = Frame(main_frame, bd=2, padx=40, pady=8, bg="teal")
        title_frame.pack(side=TOP)

        self.lbl_title = Label(title_frame, font=('Verdana', 43, 'bold'), text="Student Database Management System",
                               bg="teal")
        self.lbl_title.grid(sticky=W)

        button_frame = Frame(main_frame, bd=2, width=1350, height=150, padx=20, pady=20, bg="teal")
        button_frame.pack(side=BOTTOM)

        data_frame = Frame(main_frame, bd=1, width=1350, height=350, padx=20, pady=20, bg="teal")
        data_frame.pack(side=BOTTOM)

        data_frame_left = LabelFrame(data_frame, bd=1, width=550, height=300, padx=30, font=('courier 15 bold'),
                                     text="Student Membership Info:", bg="teal")
        data_frame_left.pack(side=LEFT)

        data_frame_right = LabelFrame(data_frame, bd=1, width=800, height=300, padx=30, font=('courier 15 bold'),
                                      text="Student Records:", bg="teal")
        data_frame_right.pack(side=RIGHT)

    # =================================================================================================================#

    # =============== Left Frame Data Entry Setup =====================================================================#

        self.lbl_student_id = Label(data_frame_left, font=('Verdana', 12, 'bold'), text="Student ID:", padx=3, pady=3,
                                    bg="teal")
        self.lbl_student_id.grid(row=0, column=0, sticky=W)
        self.txt_student_id = Entry(data_frame_left, font=('Verdana', 12, 'bold'), textvariable=student_id, width=40)
        self.txt_student_id.grid(row=0, column=1)

        self.lbl_first_name = Label(data_frame_left, font=('Verdana', 12, 'bold'), text="First Name:", padx=3, pady=3,
                                    bg="teal")
        self.lbl_first_name.grid(row=1, column=0, sticky=W)
        self.txt_first_name = Entry(data_frame_left, font=('Verdana', 12, 'bold'), textvariable=first_name, width=40)
        self.txt_first_name.grid(row=1, column=1)

        self.lbl_surname = Label(data_frame_left, font=('Verdana', 12, 'bold'), text="Surname:", padx=3, pady=3,
                                 bg="teal")
        self.lbl_surname.grid(row=2, column=0, sticky=W)
        self.txt_surname = Entry(data_frame_left, font=('Verdana', 12, 'bold'), textvariable=surname, width=40)
        self.txt_surname.grid(row=2, column=1)

        self.lbl_date_of_birth = Label(data_frame_left, font=('Verdana', 12, 'bold'), text="Date of Birth:", padx=3,
                                       pady=3, bg="teal")
        self.lbl_date_of_birth.grid(row=3, column=0, sticky=W)
        self.txt_date_of_birth = Entry(data_frame_left, font=('Verdana', 12, 'bold'), textvariable=date_of_birth,
                                       width=40)
        self.txt_date_of_birth.grid(row=3, column=1)

        self.lbl_gov_id = Label(data_frame_left, font=('Verdana', 12, 'bold'), text="Government ID:", padx=3, pady=3,
                                bg="teal")
        self.lbl_gov_id.grid(row=4, column=0, sticky=W)
        self.txt_gov_id = Entry(data_frame_left, font=('Verdana', 12, 'bold'), textvariable=gov_id, width=40)
        self.txt_gov_id.grid(row=4, column=1)

        self.lbl_gender = Label(data_frame_left, font=('Verdana', 12, 'bold'), text="Gender:", padx=3, pady=3, bg="teal")
        self.lbl_gender.grid(row=5, column=0, sticky=W)
        self.txt_gender = Entry(data_frame_left, font=('Verdana', 12, 'bold'), textvariable=gender, width=40)
        self.txt_gender.grid(row=5, column=1)

        self.lbl_major = Label(data_frame_left, font=('Verdana', 12, 'bold'), text="Major:", padx=3, pady=3, bg="teal")
        self.lbl_major.grid(row=6, column=0, sticky=W)
        self.txt_major = Entry(data_frame_left, font=('Verdana', 12, 'bold'), textvariable=major, width=40)
        self.txt_major.grid(row=6, column=1)

        self.lbl_address1 = Label(data_frame_left, font=('Verdana', 12, 'bold'), text="Address:", padx=3, pady=3,
                                  bg="teal")
        self.lbl_address1.grid(row=7, column=0, sticky=W)
        self.txt_address1 = Entry(data_frame_left, font=('Verdana', 12, 'bold'), textvariable=address1, width=40)
        self.txt_address1.grid(row=7, column=1)

        self.lbl_address2 = Label(data_frame_left, font=('Verdana', 12, 'bold'), text="City & State:", padx=3, pady=3,
                                  bg="teal")
        self.lbl_address2.grid(row=8, column=0, sticky=W)
        self.txt_address2 = Entry(data_frame_left, font=('Verdana', 12, 'bold'), textvariable=address2, width=40)
        self.txt_address2.grid(row=8, column=1)

        self.lbl_mobile_no = Label(data_frame_left, font=('Verdana', 12, 'bold'), text="Mobile No.:", padx=3, pady=3,
                                   bg="teal")
        self.lbl_mobile_no.grid(row=9, column=0, sticky=W)
        self.txt_mobile_no = Entry(data_frame_left, font=('Verdana', 12, 'bold'), textvariable=mobile_no, width=40)
        self.txt_mobile_no.grid(row=9, column=1)

    # =================================================================================================================#

    # ============= Listbox and Scrollbar =============================================================================#

        scrollbar = Scrollbar(data_frame_right)
        scrollbar.grid(row=0, column=1, sticky='ns')

        student_list = Listbox(data_frame_right, width=65, height=11, font=('Helvetica', 12, 'bold'),
                               yscrollcommand=scrollbar.set)
        student_list.bind('<<ListboxSelect>>', student_select)
        student_list.grid(row=0, column=0, padx=5)
        scrollbar.config(command=student_list.yview)

    # =================================================================================================================#

    # ================== Button Bar Setup =============================================================================#

        self.button_add_data = Button(button_frame, text='Add Data', font=('Helvetica', 14, 'bold'), height=2, width=12,
                                      bd=5, command=add_data)
        self.button_add_data.grid(row=0, column=0)

        self.button_display_data = Button(button_frame, text='Display Data', font=('Helvetica', 14, 'bold'), height=2,
                                          width=12, bd=5, command=display_data)
        self.button_display_data.grid(row=0, column=1)

        self.button_clear_data = Button(button_frame, text='Clear Data', font=('Helvetica', 14, 'bold'), height=2,
                                        width=12, bd=5, command=clear_data)
        self.button_clear_data.grid(row=0, column=2)

        self.button_delete_data = Button(button_frame, text='Delete Record', font=('Helvetica', 14, 'bold'), height=2,
                                         width=12, bd=5, command=delete_data)
        self.button_delete_data.grid(row=0, column=3)

        self.button_update_data = Button(button_frame, text='Update Data', font=('Helvetica', 14, 'bold'), height=2,
                                         width=12, bd=5, command=update_db)
        self.button_update_data.grid(row=0, column=4)

        self.button_search_data = Button(button_frame, text='Search Data', font=('Helvetica', 14, 'bold'), height=2,
                                         width=12, bd=5, command=search_db)
        self.button_search_data.grid(row=0, column=5)

        self.button_delete_all_data = Button(button_frame, text='Delete All Data', font=('Helvetica', 14, 'bold'),
                                             height=2, width=12, bd=5, command=delete_db_data)
        self.button_delete_all_data.grid(row=0, column=6)

        self.button_exit = Button(button_frame, text='Exit', font=('Helvetica', 14, 'bold'), height=2, width=12, bd=5,
                                  command=i_exit)
        self.button_exit.grid(row=0, column=7)

    # =================================================================================================================#


if __name__ == '__main__':
    space = Tk()
    application = StudentDB(space)
    space.mainloop()
