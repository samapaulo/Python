from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class Medical:

    def __init__(self, space):

        # ======== Form Setup ==========================================================================================

        self.space = space
        self.space.title("Patient Medical Management System")
        self.space.geometry("1450x750+0+0")
        self.space.configure(background="azure")

        # ==============================================================================================================

        # ======== Frame Setup =========================================================================================

        main_frame = Frame(self.space)
        main_frame.grid()

        title_frame = Frame(main_frame, bd=10, width=1550, padx=20, relief=FLAT)
        title_frame.pack(side=TOP)

        self.lbl_title = Label(title_frame, font=('Helvetica', 40, 'bold'), text='Patient Medical Management System',
                               padx=2, fg='navy blue')
        self.lbl_title.grid()

        display_frame = Frame(main_frame, bd=10, width=1450, height=150, padx=2, relief=RIDGE)
        display_frame.pack(side=BOTTOM)

        button_frame = Frame(main_frame, bd=10, width=1450, height=80, padx=1, relief=RIDGE)
        button_frame.pack(side=BOTTOM)

        data_frame = Frame(main_frame, bd=10, width=1450, height=400, padx=2, relief=RIDGE)
        data_frame.pack(side=BOTTOM)

        data_frame_left = LabelFrame(data_frame, bd=1, width=800, height=350, padx=2, relief=RIDGE,
                                     font=('Courier', 15, 'bold'), text='Patient Information:')
        data_frame_left.pack(side=LEFT)

        data_frame_right = LabelFrame(data_frame, bd=1, width=620, height=350, padx=2, relief=RIDGE,
                                      font=('Courier', 15, 'bold'), text='Prescription:')
        data_frame_right.pack(side=RIGHT)

        # ==============================================================================================================

        # ========== Variable Declarations =============================================================================

        cmb_name_tablets = StringVar()
        ref = StringVar()
        dose = StringVar()
        number_tablets = StringVar()
        lot = StringVar()
        issued_date = StringVar()
        exp_date = StringVar()
        daily_dose = StringVar()
        side_effects = StringVar()
        further_info = StringVar()
        storage_advice = StringVar()
        operating_machines = StringVar()
        medication_usage = StringVar()
        patient_id = StringVar()
        patient_ins_num = StringVar()
        patient_name = StringVar()
        date_of_birth = StringVar()
        patient_address = StringVar()
        prescription = StringVar()

        # ==============================================================================================================

        # =========== Functions ========================================================================================

        def i_exit():
            i_exit = tkinter.messagebox.askyesno("Patient Medical Management System", "Do you want to exit?")
            if i_exit > 0:
                space.destroy()
                return

        def i_prescription():

            self.txt_prescription.insert(END, 'Name of Tablets: \t\t' + cmb_name_tablets.get() + '\t Further Info:\t\t'
                                         + further_info.get() + "\n"
                                         + 'Reference No: \t\t' + ref.get() + '\tStorage Advice:\t\t' +
                                         storage_advice.get() + "\n"
                                         + 'Dosage: \t\t' + dose.get() + '\tOperating Machinery?\t\t'
                                         + operating_machines.get() + "\n"
                                         + 'No. of Tablets: \t\t' + number_tablets.get() + '\tMedication Usage:\t\t'
                                         + medication_usage.get() + "\n"
                                         + 'Lot: \t\t' + lot.get() + '\tPatient ID:\t\t' + patient_id.get() + "\n"
                                         + 'Issued Date: \t\t' + issued_date.get() + '\tInsurance No.:\t\t'
                                         + patient_ins_num.get() + "\n"
                                         + 'Expiry Date: \t\t' + exp_date.get() + '\tPatient Name:\t\t' +
                                         patient_name.get() + "\n"
                                         + 'Daily Dose: \t\t' + daily_dose.get() + '\tDate of Birth:\t\t' +
                                         date_of_birth.get() + "\n"
                                         + 'Side Effects: \t\t' + side_effects.get() + '\tPatient Address:\t\t'
                                         + patient_address.get() + "\n")

            return

        def i_prescription_data():

            self.txt_display.insert(END, "   " + cmb_name_tablets.get() + "\t\t" + ref.get() + "\t\t" + lot.get() +
                                    "\t\t" + number_tablets.get() + "\t" + dose.get() + "\t\t" +
                                    issued_date.get() + "\t" + exp_date.get() + "\t\t" + daily_dose.get() +
                                    "\t" + storage_advice.get() + "\t\t" + patient_ins_num.get() + "\t" +
                                    patient_name.get() + "\t    " + date_of_birth.get() + "\t    " +
                                    patient_address.get() + "\n")

            return

        def i_reset():

            cmb_name_tablets.set("")
            self.cmb_name_tablet.current(0)
            ref.set("")
            dose.set("")
            number_tablets.set("")
            lot.set("")
            issued_date.set("")
            exp_date.set("")
            daily_dose.set("")
            side_effects.set("")
            further_info.set("")
            storage_advice.set("")
            operating_machines.set("")
            medication_usage.set("")
            patient_id.set("")
            patient_ins_num.set("")
            patient_name.set("")
            date_of_birth.set("")
            patient_address.set("")
            self.txt_prescription.delete("1.0", END)

            return

        def i_delete():

            i_reset()

            self.txt_display.delete("1.0", END)

            return

        # ==============================================================================================================

        # =========== Data Left Frame -> Patient Information Form Set up ===============================================

        self.lbl_name_title = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Name of Tablets:',
                                    padx=2, pady=3, width=15, anchor='w')
        self.lbl_name_title.grid(row=0, column=0)

        self.cmb_name_tablet = ttk.Combobox(data_frame_left, font=('Helvetica', 12, 'bold'), width=15,
                                            textvariable=cmb_name_tablets, state='readonly')
        self.cmb_name_tablet['value'] = ('', 'Ibuprofen', 'Hydrocodone', 'Statin', 'Angiotensin', 'Paracetamol',
                                         'Penicillin', 'Other Antibiotic')
        self.cmb_name_tablet.current(0)
        self.cmb_name_tablet.grid(row=0, column=1)

        self.lbl_further_info = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Further Information:',
                                      padx=2, pady=3, width=20, anchor='w')
        self.lbl_further_info.grid(row=0, column=2)
        self.txt_further_info = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=further_info,
                                      width=35, fg='indigo')
        self.txt_further_info.grid(row=0, column=3)

        self.lbl_reference = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Reference:', padx=2, pady=3,
                                   width=15, anchor='w')
        self.lbl_reference.grid(row=1, column=0)
        self.txt_reference = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=ref, width=17,
                                   fg='indigo')
        self.txt_reference.grid(row=1, column=1)

        self.lbl_storage = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Storage Advice:', padx=2,
                                 pady=3, width=20, anchor='w')
        self.lbl_storage.grid(row=1, column=2)
        self.txt_storage = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=storage_advice, width=35,
                                 fg='red')
        self.txt_storage.grid(row=1, column=3)

        self.lbl_dose = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Dose:', padx=2, pady=3, width=15,
                              anchor='w')
        self.lbl_dose.grid(row=2, column=0)
        self.txt_dose = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=dose, width=17,
                              fg='red')
        self.txt_dose.grid(row=2, column=1)

        self.lbl_operating_machines = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Operating Machinery?'
                                            , padx=2, pady=3, width=20, anchor='w')
        self.lbl_operating_machines.grid(row=2, column=2)
        self.txt_operating_machines = Entry(data_frame_left, font=('Helvetica', 12, 'bold'),
                                            textvariable=operating_machines, width=35, fg='red')
        self.txt_operating_machines.grid(row=2, column=3)

        self.lbl_number_tablets = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='No. of Tablets:', padx=2,
                                        pady=3, width=15, anchor='w')
        self.lbl_number_tablets.grid(row=3, column=0)
        self.txt_number_tablets = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=number_tablets,
                                        width=17, fg='red')
        self.txt_number_tablets.grid(row=3, column=1)

        self.lbl_medication_usage = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Medication Usage:',
                                          padx=2, pady=3, width=20, anchor='w')
        self.lbl_medication_usage.grid(row=3, column=2)
        self.txt_medication_usage = Entry(data_frame_left, font=('Helvetica', 12, 'bold'),
                                          textvariable=medication_usage, width=35, fg='red')
        self.txt_medication_usage.grid(row=3, column=3)

        self.lbl_lot = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Lot:', padx=2, pady=3, width=15,
                             anchor='w')
        self.lbl_lot.grid(row=4, column=0)
        self.txt_lot = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=lot, width=17, fg='indigo')
        self.txt_lot.grid(row=4, column=1)

        self.lbl_patient_id = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Patient ID:', padx=2, pady=3,
                                    width=20, anchor='w')
        self.lbl_patient_id.grid(row=4, column=2)
        self.txt_patient_id = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=patient_id, width=35,
                                    fg='indigo')
        self.txt_patient_id.grid(row=4, column=3)

        self.lbl_issued_date = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Issued Date:', padx=2,
                                     pady=3, width=15, anchor='w')
        self.lbl_issued_date.grid(row=5, column=0)
        self.txt_issued_date = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=issued_date,
                                     width=17, fg='red')
        self.txt_issued_date.grid(row=5, column=1)

        self.lbl_ins_number = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Insurance No.:', padx=2,
                                    pady=3, width=20, anchor='w')
        self.lbl_ins_number.grid(row=5, column=2)
        self.txt_ins_number = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=patient_ins_num,
                                    width=35, fg='indigo')
        self.txt_ins_number.grid(row=5, column=3)

        self.lbl_exp_date = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Expiry Date:', padx=2, pady=3,
                                  width=15, anchor='w')
        self.lbl_exp_date.grid(row=6, column=0)
        self.txt_exp_date = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=exp_date, width=17,
                                  fg='red')
        self.txt_exp_date.grid(row=6, column=1)

        self.lbl_patient_name = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Patient Name:', padx=2,
                                      pady=3, width=20, anchor='w')
        self.lbl_patient_name.grid(row=6, column=2)
        self.txt_patient_name = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=patient_name,
                                      width=35, fg='indigo')
        self.txt_patient_name.grid(row=6, column=3)

        self.lbl_daily_dose = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Daily Dose:', padx=2, pady=3,
                                    width=15, anchor='w')
        self.lbl_daily_dose.grid(row=7, column=0)
        self.txt_daily_dose = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=daily_dose, width=17,
                                    fg='red')
        self.txt_daily_dose.grid(row=7, column=1)

        self.lbl_birth_date = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Date of Birth:', padx=2,
                                    pady=3, width=20, anchor='w')
        self.lbl_birth_date.grid(row=7, column=2)
        self.txt_birth_date = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=date_of_birth,
                                    width=35, fg='indigo')
        self.txt_birth_date.grid(row=7, column=3)

        self.lbl_side_effects = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Side Effects:', padx=2,
                                      pady=3, width=15, anchor='w')
        self.lbl_side_effects.grid(row=8, column=0)
        self.txt_side_effects = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=side_effects,
                                      width=17, fg='red')
        self.txt_side_effects.grid(row=8, column=1)

        self.lbl_patient_address = Label(data_frame_left, font=('Helvetica', 12, 'bold'), text='Patient Address:',
                                         padx=2, pady=3, width=20, anchor='w')
        self.lbl_patient_address.grid(row=8, column=2)
        self.txt_patient_address = Entry(data_frame_left, font=('Helvetica', 12, 'bold'), textvariable=patient_address,
                                         width=35, fg='indigo')
        self.txt_patient_address.grid(row=8, column=3)

        # ==============================================================================================================

        # ==================== Date Frame Right -> Prescription Form Setup =============================================

        self.txt_prescription = Text(data_frame_right, font=('Helvetica', 12, 'bold'), width=66, height=12, padx=2,
                                     pady=1, fg='SpringGreen4')
        self.txt_prescription.grid(row=0, column=0)

        # ==============================================================================================================

        # =================== Display Frame Setup ======================================================================

        self.lbl_label = Label(display_frame, font=('Arial', 10, 'bold'),
                               text='Name of Tablets\tReference Number\tLot\tNumber of Tablets   Dosage \tIssued Date\t'
                                    'Exp. Date\tDaily Dose\tStorage Advise\tIns Number\tPatient Name\tDoB\tAddress ')
        self.lbl_label.grid(row=0, column=0)

        self.txt_display = Text(display_frame, font=('Helvetica', 12, 'bold'), width=157, height=9, padx=2, pady=2,
                                fg='blue')
        self.txt_display.grid(row=1, column=0)

        # ==============================================================================================================

        # ==================== Button Frame Setup ======================================================================

        self.btn_prescription = Button(button_frame, text='Prescription', font=('Helvetica', 12, 'bold'), width=30,
                                       padx=4, command= i_prescription, bg='azure3')
        self.btn_prescription.grid(row=0, column=0)

        self.btn_receipt = Button(button_frame, text='Prescription Data', font=('Helvetica', 12, 'bold'), width=30,
                                  padx=4, command=i_prescription_data, bg='azure3')
        self.btn_receipt.grid(row=0, column=1)

        self.btn_delete = Button(button_frame, text='Delete', font=('Helvetica', 12, 'bold'), width=30, padx=4,
                                 command=i_delete, bg='azure3')
        self.btn_delete.grid(row=0, column=2)

        self.btn_reset = Button(button_frame, text='Reset', font=('Helvetica', 12, 'bold'), width=30, padx=4,
                                command=i_reset, bg='azure3')
        self.btn_reset.grid(row=0, column=3)

        self.btn_exit = Button(button_frame, text='Exit', font=('Helvetica', 12, 'bold'), width=30, padx=4,
                               command=i_exit, bg='azure3')
        self.btn_exit.grid(row=0, column=4)

        # ==============================================================================================================


if __name__ == '__main__':
    space = Tk()
    application = Medical(space)
    space.mainloop()




