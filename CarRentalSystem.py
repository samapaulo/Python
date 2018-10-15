from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import *
import datetime
import time

# ============== Form Set Up ===========================================================================================

space = Tk()
space.title("Car Rental System")
space.geometry("1400x750+0+0")

# ======================================================================================================================

# ============= Frame Set Up ===========================================================================================

topFrame = Frame(space, width=1400, height=110, bd=2)
topFrame.pack(side=TOP)

bottomFrame = Frame(space, width=1400, height=650)
bottomFrame.pack(side=BOTTOM)

leftMainFrame = Frame(bottomFrame, width=1000, height=650, bd=2, relief="raise")
leftMainFrame.pack(side=LEFT)

rightMainFrame = Frame(bottomFrame, width=400, height=650, relief="raise")
rightMainFrame.pack(side=RIGHT)

rightFrame1 = Frame(rightMainFrame, width=400, height=325, bd=2, relief='raise')
rightFrame1.pack(side=TOP)

rightFrame2 = Frame(rightMainFrame, width=400, height=325, bd=2, relief='raise')
rightFrame2.pack(side=BOTTOM)

leftTopFrame = Frame(leftMainFrame, width=1000, height=234, bd=5, relief="raise")
leftTopFrame.pack(side=TOP)

leftFrame2 = Frame(leftMainFrame, width=1000, height=466, relief="raise")
leftFrame2.pack(side=BOTTOM)

leftMidFrame = Frame(leftFrame2, width=1000, height=233, bd=5, relief='raise')
leftMidFrame.pack(side=TOP)

leftBottomFrame = Frame(leftFrame2, width=1000, height=233, relief='raise')
leftBottomFrame.pack(side=BOTTOM)

leftBottomFrame1 = Frame(leftBottomFrame, width=1000, height=150, bd=5, relief='raise')
leftBottomFrame1.pack(side=TOP)

leftBottomFrame2 = Frame(leftBottomFrame, width=1000, height=73, bd=5, relief='raise')
leftBottomFrame2.pack(side=BOTTOM)

# ======================================================================================================================

# ============= Title ==================================================================================================

lblTitle = Label(topFrame,font=("Courier News", 55, 'bold'), text="Car Rental System", bd=10, anchor='w')
lblTitle.grid(row=0, column=0)

# ======================================================================================================================

# ============= Variable Declaration ===================================================================================

# ------------- Customer Profile and Registration ----------------------------------------------------------------------

Title = StringVar()
FirstName = StringVar()
Surname = StringVar()
Customer = StringVar()
Street = StringVar()
City = StringVar()
ZipCode = StringVar()
LicenseNo = StringVar()
IssueDate = StringVar()
IssueBy = StringVar()
RegistrationNo = StringVar()
DailyRentalRate = StringVar()

# ----------------------------------------------------------------------------------------------------------------------

# ---------- Vehicle Data ----------------------------------------------------------------------------------------------

EngineSize = StringVar()
Style = StringVar()
RegisteredYear = StringVar()
ClassID = StringVar()
CarDescription = StringVar()
MilesBefore = StringVar()
MilesAfter = StringVar()
Make = StringVar()
Model = StringVar()
EngineMake = StringVar()
CarColor = StringVar()
CarInsurance = StringVar()

# ----------------------------------------------------------------------------------------------------------------------

# ---------- Customer Transaction --------------------------------------------------------------------------------------

Receipt_Ref = StringVar()
CustomerID = StringVar()
DaysRented = StringVar()
Discount = StringVar()
NumberOfDays = StringVar()
InvoiceID = StringVar()
Total = StringVar()

# ----------------------------------------------------------------------------------------------------------------------

# ----------- Features and Selections ----------------------------------------------------------------------------------

Style1 = IntVar()
ClassID1 = IntVar()
InvoiceID1 = IntVar()
DailyRate = IntVar()
Automatic = IntVar()
AirCondition = IntVar()
InsuranceSold = IntVar()
CustomerDetails = IntVar()

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================

# ============= Date of Order ==========================================================================================

IssueDate.set(time.strftime("%b %d, %Y"))
# ======================================================================================================================

# ============= Button Functions =======================================================================================

# ------------- Exit Button --------------------------------------------------------------------------------------------


def q_exit():
    m_exit = messagebox.askyesno("Exit System","Do you want to quit the system?")
    if m_exit > 0:
        space.destroy()
        return

# ----------------------------------------------------------------------------------------------------------------------

# ------------- Reset Button -------------------------------------------------------------------------------------------


def reset():
    Title.set("")
    FirstName.set("")
    Surname.set("")
    Customer.set("")
    Street.set("")
    City.set("")
    ZipCode.set("")
    LicenseNo.set("")
    IssueDate.set("")
    IssueBy.set("")
    RegistrationNo.set("")
    DailyRentalRate.set("")
    EngineSize.set("")
    Style.set("")
    RegisteredYear.set("")
    Receipt_Ref.set("")
    ClassID.set("")
    CarDescription.set("")
    MilesBefore.set("")
    MilesAfter.set("")
    Make.set("")
    Model.set("")
    EngineMake.set("")
    CarColor.set("")
    CarInsurance.set("")
    CustomerID.set("")
    DaysRented.set("")
    Discount.set("")
    NumberOfDays.set("")
    InvoiceID.set("")
    Total.set("")
    txtReceipt.delete("1.0", END)

    Style1.set(0)
    ClassID1.set(0)
    InvoiceID1.set(0)
    DailyRate.set(0)
    Automatic.set(0)
    AirCondition.set(0)
    InsuranceSold.set(0)
    CustomerDetails.set(0)
# ----------------------------------------------------------------------------------------------------------------------

# ------------  Receipt Button -----------------------------------------------------------------------------------------


def receipt():
    txtReceipt.delete("1.0", END)
    x = randint(45, 2000000)
    random_ref = str(x)
    Receipt_Ref.set("BILL" + random_ref)

    txtReceipt.insert(END, 'Receipt Ref:\t' + Receipt_Ref.get() + '\nDate:\t' + IssueDate.get()+"\n\n")
    txtReceipt.insert(END, 'Car Rental Services \n\n')
    txtReceipt.insert(END, 'Customer ID: \t' + CustomerID.get() + '\n')
    txtReceipt.insert(END, 'Days Rented: \t\t' + DaysRented.get() + '\n')
    txtReceipt.insert(END, 'Number of Days: \t\t' + NumberOfDays.get() + '\n')
    txtReceipt.insert(END, 'Invoice ID: \t\t' + InvoiceID.get() + '\n')
    txtReceipt.insert(END, 'Discount: \t\t' + Discount.get() + '\n')
    txtReceipt.insert(END, 'Total: \t\t' + Total.get() + '\n')

# ----------------------------------------------------------------------------------------------------------------------

# -------------- Total Button (Car Rental Cost) ------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------


def total():
    num_of_days = float(NumberOfDays.get())
    car_discount = float(Discount.get())
    daily_rate = float(DailyRentalRate.get())

    cost_of_rental = "$", str('%.2f' % ((num_of_days * daily_rate) * (100 - car_discount)/100))
    Total.set(cost_of_rental)

    ID = randint(30, 335000)
    random_id = str(ID)
    CustomerID.set("CAR" + random_id)

    inv = randint(10, 557895)
    inv_id = str(inv)
    InvoiceID.set("INV" + inv_id)

# ======================================================================================================================


# ============= Customer Profile and Registration Setup ================================================================


lblTitle = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=10, bd=15, text='Title', anchor='w')
lblTitle.grid(row=0, column=0)
txtTitle = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=10, bd=8, justify='left', textvariable=Title)
txtTitle.grid(row=0, column=1)

lblFirstName = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=11, bd=15, text='First Name', anchor='w')
lblFirstName.grid(row=0, column=2)
txtFirstName = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=22, bd=8, justify='left',
                     textvariable=FirstName)
txtFirstName.grid(row=0, column=3)

lblSurname = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Surname', anchor='w')
lblSurname.grid(row=0, column=4)
txtSurname = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left', textvariable=Surname)
txtSurname.grid(row=0, column=5)

lblCustomer = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=10, bd=15, text='Customer?', anchor='w')
lblCustomer.grid(row=1, column=0)
txtCustomer = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=10, bd=8, justify='left', textvariable=Customer)
txtCustomer.grid(row=1, column=1)

lblStreet = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=11, bd=15, text='Street', anchor='w')
lblStreet.grid(row=1, column=2)
txtStreet = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=22, bd=8, justify='left', textvariable=Street)
txtStreet.grid(row=1, column=3)

lblCity = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='City', anchor='w')
lblCity.grid(row=1, column=4)
txtCity = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left', textvariable=City)
txtCity.grid(row=1, column=5)

lblZipCode = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=10, bd=15, text='Post / ZipCode', anchor='w')
lblZipCode.grid(row=2, column=0)
txtZipCode = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=10, bd=8, justify='left', textvariable=ZipCode)
txtZipCode.grid(row=2, column=1)

lblLicenseNo = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=11, bd=15, text='License No.', anchor='w')
lblLicenseNo.grid(row=2, column=2)
txtLicenseNo = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=22, bd=8, justify='left',
                     textvariable=LicenseNo)
txtLicenseNo.grid(row=2, column=3)

lblIssueDate = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Issue Date', anchor='w')
lblIssueDate.grid(row=2, column=4)
txtIssueDate = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                     textvariable=IssueDate)
txtIssueDate.grid(row=2, column=5)

lblIssueBy = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=10, bd=15, text='Issue By', anchor='w')
lblIssueBy.grid(row=3, column=0)
txtIssueBy = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=10, bd=8, justify='left', textvariable=IssueBy)
txtIssueBy.grid(row=3, column=1)

lblRegistrationNo = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=11, bd=15, text='Registration No.',
                          anchor='w')
lblRegistrationNo.grid(row=3, column=2)
txtRegistrationNo = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=22, bd=8, justify='left',
                          textvariable=RegistrationNo)
txtRegistrationNo.grid(row=3, column=3)

lblDailyRentalRate = Label(leftTopFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Daily Rental Rate',
                           anchor='w')
lblDailyRentalRate.grid(row=3, column=4)
txtDailyRentalRate = Entry(leftTopFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                           textvariable=DailyRentalRate)
txtDailyRentalRate.grid(row=3, column=5)

# ======================================================================================================================

# ============= Vehicle Data Setup =====================================================================================

lblEngineSize = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Engine Size', anchor='w')
lblEngineSize.grid(row=0, column=0)
txtEngineSize = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                      textvariable=EngineSize)
txtEngineSize.grid(row=0, column=1)

lblStyle = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Style', anchor='w')
lblStyle.grid(row=0, column=2)
txtStyle = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left', textvariable=Style)
txtStyle.grid(row=0, column=3)

lblRegisteredYear = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Registered Year',
                          anchor='w')
lblRegisteredYear.grid(row=0, column=4)
txtRegisteredYear = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                          textvariable=RegisteredYear)
txtRegisteredYear.grid(row=0, column=5)

lblClassID = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Class ID', anchor='w')
lblClassID.grid(row=1, column=0)
txtClassID = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left', textvariable=ClassID)
txtClassID.grid(row=1, column=1)

lblCarDescription = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Car Description',
                          anchor='w')
lblCarDescription.grid(row=1, column=2)
txtCarDescription = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                          textvariable=CarDescription)
txtCarDescription.grid(row=1, column=3)

lblMilesBefore = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Miles Before', anchor='w')
lblMilesBefore.grid(row=1, column=4)
txtMilesBefore = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                       textvariable=MilesBefore)
txtMilesBefore.grid(row=1, column=5)

lblMilesAfter = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Miles After', anchor='w')
lblMilesAfter.grid(row=2, column=0)
txtMilesAfter = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                      textvariable=MilesAfter)
txtMilesAfter.grid(row=2, column=1)

lblMake = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Make', anchor='w')
lblMake.grid(row=2, column=2)
txtMake = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left', textvariable=Make)
txtMake.grid(row=2, column=3)

lblModel = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Model', anchor='w')
lblModel.grid(row=2, column=4)
txtModel = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left', textvariable=Model)
txtModel.grid(row=2, column=5)

lblEngineMake = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Engine Make', anchor='w')
lblEngineMake.grid(row=3, column=0)
txtEngineMake = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                      textvariable=EngineMake)
txtEngineMake.grid(row=3, column=1)

lblCarColor = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Car Color', anchor='w')
lblCarColor.grid(row=3, column=2)
txtCarColor = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                    textvariable=CarColor)
txtCarColor.grid(row=3, column=3)

lblCarInsurance = Label(leftMidFrame, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Car Insurance?', anchor='w')
lblCarInsurance.grid(row=3, column=4)
txtCarInsurance = Entry(leftMidFrame, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                        textvariable=CarInsurance)
txtCarInsurance.grid(row=3, column=5)

# ======================================================================================================================

# ============= Rental Transaction Setup ===============================================================================

lblCustomerID = Label(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Customer ID', anchor='w')
lblCustomerID.grid(row=0, column=0)
txtCustomerID = Entry(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                      textvariable=CustomerID)
txtCustomerID.grid(row=0, column=1)

lblDaysRented = Label(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Days Rented', anchor='w')
lblDaysRented.grid(row=0, column=2)
txtDaysRented = Entry(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                      textvariable=DaysRented)
txtDaysRented.grid(row=0, column=3)

lblDiscount = Label(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Discount %', anchor='w')
lblDiscount.grid(row=0, column=4)
txtDiscount = Entry(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                    textvariable=Discount)
txtDiscount.grid(row=0, column=5)

lblNumberOfDays = Label(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Number Of Days',
                        anchor='w')
lblNumberOfDays.grid(row=1, column=0)
txtNumberOfDays = Entry(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                        textvariable=NumberOfDays)
txtNumberOfDays.grid(row=1, column=1)

lblInvoiceID = Label(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Invoice ID',
                     anchor='w')
lblInvoiceID.grid(row=1, column=2)
txtInvoiceID = Entry(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                     textvariable=InvoiceID)
txtInvoiceID.grid(row=1, column=3)

lblTotal = Label(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=12, bd=15, text='Total', anchor='w')
lblTotal.grid(row=1, column=4)
txtTotal = Entry(leftBottomFrame1, font=('Helvetica', 14, 'bold'), width=14, bd=8, justify='left',
                 textvariable=Total)
txtTotal.grid(row=1, column=5)

# ======================================================================================================================

# ============= Buttons Setup ==========================================================================================

btnTotal = Button(leftBottomFrame2, font=('Helvetica', 14, 'bold'), width=20, bd=11, text='Total', command=total)
btnTotal.grid(row=0, column=0)

btnReceipt = Button(leftBottomFrame2, font=('Helvetica', 14, 'bold'), width=19, bd=11, text='Receipt', command=receipt)
btnReceipt.grid(row=0, column=1)

btnReset = Button(leftBottomFrame2, font=('Helvetica', 14, 'bold'), width=20, bd=11, text='Reset', command=reset)
btnReset.grid(row=0, column=2)

btnExit = Button(leftBottomFrame2, font=('Helvetica', 14, 'bold'), width=19, bd=11, text='Exit', command=q_exit)
btnExit.grid(row=0, column=3)

# ======================================================================================================================

# ============= Checkbox Setup =========================================================================================

lblStyle_cb = Checkbutton(rightFrame1, font=('Helvetica', 14, 'bold'), width=26, bd=1, text='Style', anchor='w',
                          onvalue=1, offvalue=0, variable=Style1)
lblStyle_cb.grid(row=0, column=0)

lblClassID1_cb = Checkbutton(rightFrame1, font=('Helvetica', 14, 'bold'), width=26, bd=2, text='Class ID', anchor='w',
                             onvalue=1, offvalue=0, variable=ClassID1)
lblClassID1_cb.grid(row=1, column=0)

lblInvoiceID1_cb = Checkbutton(rightFrame1, font=('Helvetica', 14, 'bold'), width=26, bd=2, text='Invoice ID',
                               anchor='w', onvalue=1, offvalue=0, variable=InvoiceID1)
lblInvoiceID1_cb.grid(row=2, column=0)

lblDailyRate_cb = Checkbutton(rightFrame1, font=('Helvetica', 14, 'bold'), width=26, bd=2, text='Daily Rate',
                              anchor='w', onvalue=1, offvalue=0, variable=DailyRate)
lblDailyRate_cb.grid(row=3, column=0)

lblAutomatic_cb = Checkbutton(rightFrame1, font=('Helvetica', 14, 'bold'), width=26, bd=2, text='Automatic', anchor='w',
                              onvalue=1, offvalue=0, variable=Automatic)
lblAutomatic_cb.grid(row=4, column=0)

lblAirCondition_cb = Checkbutton(rightFrame1, font=('Helvetica', 14, 'bold'), width=26, bd=2, text='Air Condition',
                                 anchor='w', onvalue=1, offvalue=0, variable=AirCondition)
lblAirCondition_cb.grid(row=5, column=0)

lblInsuranceSold_cb = Checkbutton(rightFrame1, font=('Helvetica', 14, 'bold'), width=26, bd=2, text='Insurance Sold',
                                  anchor='w', onvalue=1, offvalue=0, variable=InsuranceSold)
lblInsuranceSold_cb.grid(row=6, column=0)

lblCustomerDetails_cb = Checkbutton(rightFrame1, font=('Helvetica', 14, 'bold'), width=26, bd=2, text='Customer Details'
                                    , anchor='w', onvalue=1, offvalue=0, variable=CustomerDetails)
lblCustomerDetails_cb.grid(row=7, column=0)

# ======================================================================================================================

# ============= Receipt Box Setup ======================================================================================

txtReceipt = Text(rightFrame2, font=('Helvetica', 16, 'bold'), bg='white', width=30, height=15)
txtReceipt.grid(row=0, column=0)

# ======================================================================================================================

# ============= Main Function Execution ================================================================================

space.mainloop()


