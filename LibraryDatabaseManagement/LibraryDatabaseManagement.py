from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import lib_bks_db


class LibraryDB:

    def __init__(self, space):
        self.space = space
        self.space.title("Library Database Management System")
        self.space.geometry("1350x570+0+0")

    # =========== Variable Declaration ================================================================================#

        member_type = StringVar()
        reference = StringVar()
        title = StringVar()
        first_name = StringVar()
        surname = StringVar()
        address1 = StringVar()
        address2 = StringVar()
        postal_code = StringVar()
        mobile_no = StringVar()
        book_id = StringVar()
        book_title = StringVar()
        author = StringVar()
        date_borrowed = StringVar()
        due_date = StringVar()
        selling_price = StringVar()
        late_fine = StringVar()
        overdue_date = StringVar()
        days_on_loan = StringVar()

    # ================ Function Declaration ===========================================================================#

        def i_exit():
            i_exit = tkinter.messagebox.askyesno("Library Database Management System", "Confirm if you want to exit")
            if i_exit > 0:
                space.destroy()
                return

        def clear_data():
            self.txt_title_txt = ttk.Combobox(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=title,
                                              width=24, state='enable', values=['Mr.', 'Ms', 'Mrs', 'Dr.', 'Sr.',
                                                                                  'Eng', 'Madam', 'Lord', 'Lady'])
            self.txt_title_txt.grid(row=2, column=1, sticky=W)

            self.txt_member_type.delete(0, END)
            self.txt_reference.delete(0, END)
            self.txt_book_id.delete(0, END)
            self.txt_book_title.delete(0, END)
            self.txt_title_txt.delete(0, END)
            self.txt_first_name.delete(0, END)
            self.txt_surname.delete(0, END)
            self.txt_author.delete(0, END)
            self.txt_date_borrowed.delete(0, END)
            self.txt_due_date.delete(0, END)
            self.txt_address1.delete(0, END)
            self.txt_address2.delete(0, END)
            self.txt_postal_code.delete(0, END)
            self.txt_days_on_loan.delete(0, END)
            self.txt_late_fine.delete(0, END)
            self.txt_overdue_date.delete(0, END)
            self.txt_selling_price.delete(0, END)
            self.txt_mobile_no.delete(0, END)

        def add_data():
            if len(member_type.get()) != 0:
                lib_bks_db.add_data_rec(member_type.get(), reference.get(), book_id.get(), book_title.get(), title.get()
                                        , first_name.get(), surname.get(), author.get(), date_borrowed.get(),
                                        due_date.get(), address1.get(), address2.get(), postal_code.get(),
                                        days_on_loan.get(), late_fine.get(), overdue_date.get(), selling_price.get(),
                                        mobile_no.get())

                book_list.delete(0, END)
                book_list.insert(END, member_type.get(), reference.get(), book_id.get(), book_title.get(), title.get(),
                                 first_name.get(), surname.get(), author.get(), date_borrowed.get(), due_date.get(),
                                 address1.get(), address2.get(), postal_code.get(), days_on_loan.get(), late_fine.get(),
                                 overdue_date.get(), selling_price.get(), mobile_no.get())

        def display_data():
            book_list.delete(0, END)
            for row in lib_bks_db.view_data():
                book_list.insert(END, row)

        def select_book(event):
            global select_bk
            book_search = book_list.curselection()[0]
            select_bk = book_list.get(book_search)

            self.txt_title_txt = ttk.Combobox(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=title,
                                              width=24, state='enable', values=['Mr.', 'Ms', 'Mrs', 'Dr.', 'Sr.',
                                                                                  'Eng', 'Madam', 'Lord', 'Lady'])
            self.txt_title_txt.grid(row=2, column=1, sticky=W)

            self.txt_member_type.delete(0, END)
            self.txt_member_type.insert(END, select_bk[1])
            self.txt_reference.delete(0, END)
            self.txt_reference.insert(END, select_bk[2])
            self.txt_book_id.delete(0, END)
            self.txt_book_id.insert(END, select_bk[3])
            self.txt_book_title.delete(0, END)
            self.txt_book_title.insert(END, select_bk[4])
            self.txt_title_txt.delete(0, END)
            self.txt_title_txt.insert(END, select_bk[5])
            self.txt_first_name.delete(0, END)
            self.txt_first_name.insert(END, select_bk[6])
            self.txt_surname.delete(0, END)
            self.txt_surname.insert(END, select_bk[7])
            self.txt_author.delete(0, END)
            self.txt_author.insert(END, select_bk[8])
            self.txt_date_borrowed.delete(0, END)
            self.txt_date_borrowed.insert(END, select_bk[9])
            self.txt_due_date.delete(0, END)
            self.txt_due_date.insert(END, select_bk[10])
            self.txt_address1.delete(0, END)
            self.txt_address1.insert(END, select_bk[11])
            self.txt_address2.delete(0, END)
            self.txt_address2.insert(END, select_bk[12])
            self.txt_postal_code.delete(0, END)
            self.txt_postal_code.insert(END, select_bk[13])
            self.txt_days_on_loan.delete(0, END)
            self.txt_days_on_loan.insert(END, select_bk[14])
            self.txt_late_fine.delete(0, END)
            self.txt_late_fine.insert(END, select_bk[15])
            self.txt_overdue_date.delete(0, END)
            self.txt_overdue_date.insert(END, select_bk[16])
            self.txt_selling_price.delete(0, END)
            self.txt_selling_price.insert(END, select_bk[17])
            self.txt_mobile_no.delete(0, END)
            self.txt_mobile_no.insert(END, select_bk[18])

        def delete_data():
            i_del = tkinter.messagebox.askyesno("Library Database Management System", "Confirm if you want to delete")
            if i_del > 0:
                if len(member_type.get()) != 0:
                    lib_bks_db.delete_rec(select_bk[0])
                    clear_data()
                    display_data()
                return

        def delete_all_data():
            i_del = tkinter.messagebox.askyesno("Library Database Management System",\
                                                "Do you really want to delete ALL your data?")
            if i_del > 0:
                lib_bks_db.delete_data()
                clear_data()
                display_data()
                return

        def search_db():
            book_list.delete(0, END)
            for row in lib_bks_db.search_data(member_type.get(), reference.get(), book_id.get(), book_title.get(),
                                              title.get(), first_name.get(), surname.get(), author.get(),
                                              date_borrowed.get(), due_date.get(), address1.get(), address2.get(),
                                              postal_code.get(), days_on_loan.get(), late_fine.get(), overdue_date.get(),
                                              selling_price.get(), mobile_no.get()):
                book_list.insert(END, row)

        def update_db():
            '''
            if len(member_type.get()) != 0:
                lib_bks_db.update_data(select_bk[0], member_type.get(), book_id.get(), reference.get(), book_title.get(),
                                       title.get(), author.get(), first_name.get(), surname.get(), due_date.get(),
                                       address1.get(), address2.get(), days_on_loan.get(), late_fine.get(),
                                       postal_code.get(), date_borrowed.get(), overdue_date.get(), selling_price.get(),
                                       mobile_no.get())
            '''

            if len(member_type.get()) != 0:
                lib_bks_db.delete_rec(select_bk[0])
            if len(member_type.get()) != 0:
                lib_bks_db.add_data_rec(member_type.get(), reference.get(), book_id.get(), book_title.get(), title.get(),
                                        first_name.get(), surname.get(),  author.get(), date_borrowed.get(),
                                        due_date.get(), address1.get(), address2.get(), postal_code.get(),
                                        days_on_loan.get(), late_fine.get(), overdue_date.get(), selling_price.get(),
                                        mobile_no.get())
            book_list.delete(0, END)
            book_list.insert(END, (member_type.get(), reference.get(), book_id.get(), book_title.get(), title.get(),
                                   first_name.get(), surname.get(), author.get(), date_borrowed.get(), due_date.get(),
                                   address1.get(), address2.get(), postal_code.get(), days_on_loan.get(),
                                   late_fine.get(), overdue_date.get(), selling_price.get(), mobile_no.get()))

    # =================================================================================================================#

    # ================ Frame Setup ====================================================================================#

        main_frame = Frame(self.space, bg="steelblue")
        main_frame.grid()

        title_frame = Frame(main_frame, bd=2, padx=40, pady=8, bg="steelblue")
        title_frame.pack(side=TOP)

        self.lbl_title = Label(title_frame, font=('Helvetica', 45, 'bold'), text="Library Database Management System",
                               bg="steelblue")
        self.lbl_title.grid(sticky=W)

        button_frame = Frame(main_frame, bd=2, width=1350, height=150, padx=20, pady=20, bg="steelblue")
        button_frame.pack(side=BOTTOM)

        data_frame = Frame(main_frame, bd=1, width=1350, height=300, padx=20, pady=20, bg="steelblue")
        data_frame.pack(side=BOTTOM)

        data_frame_left = LabelFrame(data_frame, bd=1, width=800, height=300, padx=30,
                                     font=('Courier', 15, 'bold'), text="Library Membership Info:", bg="steelblue")
        data_frame_left.pack(side=LEFT)

        data_frame_right = LabelFrame(data_frame, bd=1, width=550, height=300, padx=20,
                                      font=('Courier', 15, 'bold'), text="Book Details:", bg="steelblue")
        data_frame_right.pack(side=RIGHT)

    # =================================================================================================================#

    # ==================== Labels and  Data Entry =====================================================================#

        self.lbl_member_type = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Member Type:', padx=2,
                                     pady=2, bg="steelblue")
        self.lbl_member_type.grid(row=0, column=0, sticky=W)
        self.txt_member_type = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=member_type,
                                     width=25)
        self.txt_member_type.grid(row=0, column=1, sticky=W)

        self.lbl_book_id = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Book ID:', padx=2, pady=2,
                                 bg="steelblue")
        self.lbl_book_id.grid(row=0, column=2, sticky=W)
        self.txt_book_id = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=book_id, width=25)
        self.txt_book_id.grid(row=0, column=3, sticky=W)

        self.lbl_reference = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Reference No', padx=2, pady=2,
                                   bg="steelblue")
        self.lbl_reference.grid(row=1, column=0, sticky=W)
        self.txt_reference = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=reference, width=25)
        self.txt_reference.grid(row=1, column=1, sticky=W)

        self.lbl_book_title = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Book Title:', padx=2, pady=2,
                                    bg="steelblue")
        self.lbl_book_title.grid(row=1, column=2, sticky=W)
        self.txt_book_title = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=book_title, width=25)
        self.txt_book_title.grid(row=1, column=3, sticky=W)

        self.lbl_title_txt = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Title:', padx=2, pady=2,
                                   bg="steelblue")
        self.lbl_title_txt.grid(row=2, column=0, sticky=W)
        self.txt_title_txt = ttk.Combobox(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=title, width=24,
                                          values=['', 'Mr.', 'Ms', 'Mrs', 'Dr.', 'Sr.', 'Eng', 'Madam', 'Lord', 'Lady'],
                                          state='readonly')
        self.txt_title_txt.grid(row=2, column=1, sticky=W)

        self.lbl_author = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Author:', padx=2, pady=2,
                                bg="steelblue")
        self.lbl_author.grid(row=2, column=2, sticky=W)
        self.txt_author = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=author, width=25)
        self.txt_author.grid(row=2, column=3, sticky=W)

        self.lbl_first_name = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='First Name:', padx=2, pady=2,
                                    bg="steelblue")
        self.lbl_first_name.grid(row=3, column=0, sticky=W)
        self.txt_first_name = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=first_name, width=25)
        self.txt_first_name.grid(row=3, column=1, sticky=W)

        self.lbl_date_borrowed = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Date Borrowed:', padx=2,
                                       pady=2, bg="steelblue")
        self.lbl_date_borrowed.grid(row=3, column=2, sticky=W)
        self.txt_date_borrowed = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=date_borrowed,
                                       width=25)
        self.txt_date_borrowed.grid(row=3, column=3, sticky=W)

        self.lbl_surname = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Surname:', padx=2, pady=2,
                                 bg="steelblue")
        self.lbl_surname.grid(row=4, column=0, sticky=W)
        self.txt_surname = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=surname, width=25)
        self.txt_surname.grid(row=4, column=1, sticky=W)

        self.lbl_due_date = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Due Date:', padx=2, pady=2,
                                  bg="steelblue")
        self.lbl_due_date.grid(row=4, column=2, sticky=W)
        self.txt_due_date = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=due_date, width=25)
        self.txt_due_date.grid(row=4, column=3, sticky=W)

        self.lbl_address1 = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Address:', padx=2, pady=2,
                                  bg="steelblue")
        self.lbl_address1.grid(row=5, column=0, sticky=W)
        self.txt_address1 = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=address1, width=25)
        self.txt_address1.grid(row=5, column=1, sticky=W)

        self.lbl_days_on_loan = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Days on Loan:', padx=2,
                                      pady=2, bg="steelblue")
        self.lbl_days_on_loan.grid(row=5, column=2, sticky=W)
        self.txt_days_on_loan = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=days_on_loan,
                                      width=25)
        self.txt_days_on_loan.grid(row=5, column=3, sticky=W)

        self.lbl_address2 = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='City & State:', padx=2, pady=2,
                                  bg="steelblue")
        self.lbl_address2.grid(row=6, column=0, sticky=W)
        self.txt_address2 = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=address2, width=25)
        self.txt_address2.grid(row=6, column=1, sticky=W)

        self.lbl_late_fine = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Late Fine:', padx=2, pady=2,
                                   bg="steelblue")
        self.lbl_late_fine.grid(row=6, column=2, sticky=W)
        self.txt_late_fine = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=late_fine, width=25)
        self.txt_late_fine.grid(row=6, column=3, sticky=W)

        self.lbl_postal_code = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Postal Code:', padx=2,
                                     pady=2, bg="steelblue")
        self.lbl_postal_code.grid(row=7, column=0, sticky=W)
        self.txt_postal_code = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=postal_code,
                                     width=25)
        self.txt_postal_code.grid(row=7, column=1, sticky=W)

        self.lbl_overdue_date = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Overdue Date:', padx=2,
                                      pady=2, bg="steelblue")
        self.lbl_overdue_date.grid(row=7, column=2, sticky=W)
        self.txt_overdue_date = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=overdue_date,
                                      width=25)
        self.txt_overdue_date.grid(row=7, column=3, sticky=W)

        self.lbl_mobile_no = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Mobile No.:', padx=2, pady=2,
                                   bg="steelblue", bd=4)
        self.lbl_mobile_no.grid(row=8, column=0, sticky=W)
        self.txt_mobile_no = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=mobile_no, width=25)
        self.txt_mobile_no.grid(row=8, column=1, sticky=W)

        self.lbl_selling_price = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Selling Price:', padx=2,
                                       pady=2, bg="steelblue", bd=4)
        self.lbl_selling_price.grid(row=8, column=2, sticky=W)
        self.txt_selling_price = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=selling_price,
                                       width=25)
        self.txt_selling_price.grid(row=8, column=3, sticky=W)

    # =================================================================================================================#

    # ==================== Listbox and Scrollbar=======================================================================#

        scrollbar = Scrollbar(data_frame_right)
        scrollbar.grid(row=0, column=1, sticky='ns')

        book_list = Listbox(data_frame_right, width=55, height=11, font=('Helvetica', 12, 'bold'),
                            yscrollcommand=scrollbar.set)
        book_list.bind('<<ListboxSelect>>', select_book)
        book_list.grid(row=0, column=0, padx=7)
        scrollbar.config(command=book_list.yview)

    # =================================================================================================================#

    # =================== Button Bar ==================================================================================#

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
                                             height=2, width=12, bd=5, command=delete_all_data)
        self.button_delete_all_data.grid(row=0, column=6)

        self.button_exit = Button(button_frame, text='Exit', font=('Helvetica', 14, 'bold'), height=2, width=12, bd=5,
                                  command=i_exit)
        self.button_exit.grid(row=0, column=7)

    # =================================================================================================================#


if __name__ == '__main__':
    space = Tk()
    application = LibraryDB(space)
    space.mainloop()
