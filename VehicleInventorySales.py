from tkinter import *
from tkinter import ttk
from tkinter import messagebox

space = Tk()
space.geometry("1400x750+0+0")
space.title("Vehicle Trading Management System")
space.configure(background="gray")

# ============= Frame Setup ============================================================================================

TopFrame = Frame(space, width=1400, height=100, bd=10, bg='azure3')
TopFrame.pack(side=TOP)

# --------------- Left Frame -------------------------------------------------------------------------------------------

leftFrame = Frame(space, width=1000, height=6500, relief="raise")
leftFrame.pack(side=LEFT)

# ----------------------------------------------------------------------------------------------------------------------

# ------------- Top Left Fame ------------------------------------------------------------------------------------------

topLeftFrame = Frame(leftFrame, width=1000, height=320, bg='azure3')
topLeftFrame.pack(side=TOP)

cornerLeftFrame = Frame(topLeftFrame, width=500, height=300, bd=7, bg='azure3')
cornerLeftFrame.pack(side=LEFT)

middleLeftFrame = Frame(topLeftFrame, width=500, height=300, bd=7, bg='azure3')
middleLeftFrame.pack(side=RIGHT)

# ----------------------------------------------------------------------------------------------------------------------

# -------------- Bottom Left Frame -------------------------------------------------------------------------------------

bottomLeftFrame = Frame(leftFrame, width=1000, height=330, bg='azure3')
bottomLeftFrame.pack(side=BOTTOM)

cornerBottomFrame = Frame(bottomLeftFrame, width=500, height=330, bd=7, bg='azure3')
cornerBottomFrame.pack(side=LEFT)

middleBottomFrame = Frame(bottomLeftFrame, width=500, height=330, bd=7, bg='azure3')
middleBottomFrame.pack(side=RIGHT)

# -------------- Right Frame -------------------------------------------------------------------------------------------

rightFrame = Frame(space, width=400, height=650, bd=7, bg='azure3')
rightFrame.pack(side=RIGHT)

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================

# ==============  Display Label ========================================================================================

lblTitle = Label(TopFrame, font=("Courier New", 44, 'bold'), text="Vehicle Sales Trading Management System", bd=10,
                 anchor='w', bg='azure3')
lblTitle.grid(row=0, column=0)

# ======================================================================================================================

# ============== Variables =============================================================================================

# --------------- Customer Data Variables ------------------------------------------------------------------------------

CustomerName = StringVar()
Address = StringVar()
City = StringVar()
State = StringVar()
ZipCode = StringVar()
Telephone = StringVar()

# --------------- Car Selection Variables ------------------------------------------------------------------------------

CarChoice = StringVar()
CarPrice = StringVar()
TradeInMiles = StringVar()
TradeInVal = StringVar()

CarPrice.set("0")
TradeInVal.set("0")

# --------------- Vehicle Features Variables ---------------------------------------------------------------------------

Modifications = StringVar()
Stereo = StringVar()
LeatherInterior = StringVar()
CustomDetails = StringVar()
GPS = StringVar()

checkboxMod = IntVar()
checkboxStereo = IntVar()
checkboxLeather = IntVar()
checkboxCustom = IntVar()
checkboxGPS = IntVar()

Modifications.set("0")
Stereo.set("0")
LeatherInterior.set("0")
CustomDetails.set("0")
GPS.set("0")

# -------------- Sales Cost  Variables ---------------------------------------------------------------------------------

VAT = StringVar()
Discount = StringVar()
SubTotal = StringVar()
Tax = StringVar()
Total = StringVar()

checkboxVAT = IntVar()
checkboxDiscount = IntVar()

# ------------ Receipt Variables ---------------------------------------------------------------------------------------

Receipt = StringVar()

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================

# ============== Functions =============================================================================================

# -------------- Car Cost ----------------------------------------------------------------------------------------------


def car_cost():
    if CarChoice.get() == '':
        mycarcost = float(0)
        CarPrice.set(mycarcost)
    elif CarChoice.get() == 'Toyota C-HR':
        mycarcost = float(26000)
        CarPrice.set(mycarcost)
    elif CarChoice.get() == 'Toyota Camry':
        mycarcost = float(25200)
        CarPrice.set(mycarcost)
    elif CarChoice.get() == 'Honda HR-V':
        mycarcost = float(19670)
        CarPrice.set(mycarcost)
    elif CarChoice.get() == 'Honda CR-V':
        mycarcost = float(24250)
        CarPrice.set(mycarcost)
    elif CarChoice.get() == 'Volkswagen Tiguan':
        mycarcost = float(24595)
        CarPrice.set(mycarcost)
    elif CarChoice.get() == 'Mercedes Benz GLC 350e':
        mycarcost = float(49990)
        CarPrice.set(mycarcost)

    if float(CarPrice.get()) > 15000.0 <= 20000.0 and TradeInMiles.get() == '':
        car_value = float(0)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 15000.0 <= 20000.0 and TradeInMiles.get() == '200001 - 350000':
        car_value = float(550)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 15000.0 <= 20000.0 and TradeInMiles.get() == '170001 - 200000':
        car_value = float(1100)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 15000.0 <= 20000.0 and TradeInMiles.get() == '120001 - 170000':
        car_value = float(1900)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 15000.0 <= 20000.0 and TradeInMiles.get() == '100001 - 120000':
        car_value = float(2500)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 15000.0 <= 20000.0 and TradeInMiles.get() == '50000 - 100000':
        car_value = float(3000)
        TradeInVal.set(car_value)

    if float(CarPrice.get()) > 20000.0 <= 25000.0 and TradeInMiles.get() == '':
        car_value = float(0)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 20000.0 <= 25000.0 and TradeInMiles.get() == '200001 - 350000':
        car_value = float(800)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 20000.0 <= 25000.0 and TradeInMiles.get() == '170001 - 200000':
        car_value = float(1500)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 20000.0 <= 25000.0 and TradeInMiles.get() == '120001 - 170000':
        car_value = float(2100)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 20000.0 <= 25000.0 and TradeInMiles.get() == '100001 - 120000':
        car_value = float(3100)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 20000.0 <= 25000.0 and TradeInMiles.get() == '50000 - 100000':
        car_value = float(3800)
        TradeInVal.set(car_value)

    if float(CarPrice.get()) > 25000.0 <= 30000.0 and TradeInMiles.get() == '':
        car_value = float(0)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 25000.0 <= 30000.0 and TradeInMiles.get() == '200001 - 350000':
        car_value = float(850)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 25000.0 <= 30000.0 and TradeInMiles.get() == '170001 - 200000':
        car_value = float(1850)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 25000.0 <= 30000.0 and TradeInMiles.get() == '120001 - 170000':
        car_value = float(2570)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 25000.0 <= 30000.0 and TradeInMiles.get() == '100001 - 120000':
        car_value = float(3700)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 25000.0 <= 30000.0 and TradeInMiles.get() == '50000 - 100000':
        car_value = float(4250)
        TradeInVal.set(car_value)

    if float(CarPrice.get()) > 45000.0 <= 50000.0 and TradeInMiles.get() == '':
        car_value = float(0)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 45000.0 <= 50000.0 and TradeInMiles.get() == '200001 - 350000':
        car_value = float(1500)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 45000.0 <= 50000.0 and TradeInMiles.get() == '170001 - 200000':
        car_value = float(2950)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 45000.0 <= 50000.0 and TradeInMiles.get() == '120001 - 170000':
        car_value = float(3500)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 45000.0 <= 50000.0 and TradeInMiles.get() == '100001 - 120000':
        car_value = float(4200)
        TradeInVal.set(car_value)
    elif float(CarPrice.get()) > 45000.0 <= 50000.0 and TradeInMiles.get() == '50000 - 100000':
        car_value = float(5300)
        TradeInVal.set(car_value)

# ----------------------------------------------------------------------------------------------------------------------

# -------------- Features function -------------------------------------------------------------------------------------


def features():
    if checkboxMod.get() == 1:
        Modifications.set(2200)
    elif checkboxMod.get() == 0:
        Modifications.set(0)
    if checkboxCustom.get() == 1:
        CustomDetails.set(1100)
    elif checkboxCustom.get() == 0:
        CustomDetails.set(0)
    if checkboxStereo.get() == 1:
        Stereo.set(1000)
    elif checkboxStereo.get() == 0:
        Stereo.set(0)
    if checkboxLeather.get() == 1:
        LeatherInterior.set(1200)
    elif checkboxLeather.get() == 0:
        LeatherInterior.set(0)
    if checkboxGPS.get() == 1:
        GPS.set(750)
    elif checkboxGPS.get() == 0:
        GPS.set(0)

# ----------------------------------------------------------------------------------------------------------------------

# -------------- Total Calculation Function ----------------------------------------------------------------------------


def calc_func():
    if checkboxVAT.get() == 1:
        VAT.set("5% of Purchase")
        VAT_val = 0.05
    elif checkboxVAT.get() == 0:
        VAT.set("No")
        VAT_val = 0
    if checkboxDiscount.get() == 1:
        Discount.set("5% of Costs")
        discount_val = 0.05
    elif checkboxDiscount.get() == 0:
        Discount.set("No")
        discount_val = 0

    subtotal_calc = (float(CarPrice.get()) - float(TradeInVal.get())) + float(Modifications.get()) + float(Stereo.get())
    + float(LeatherInterior.get()) + float(CustomDetails.get()) + float(GPS.get())

    subtotal_val = subtotal_calc - (subtotal_calc * discount_val)

    tax_val = (subtotal_val * 0.0865) + (subtotal_val * VAT_val)
    total_val = subtotal_val + tax_val

    SubTotal.set("$ "+str('%.2f' % subtotal_val))
    Tax.set("$ "+str('%.2f' % tax_val))
    Total.set("$ "+str('%.2f' % total_val))
# ----------------------------------------------------------------------------------------------------------------------

# -------------- Total Cost Function -----------------------------------------------------------------------------------


def total_cost():
    car_cost()
    features()
    calc_func()

# ----------------------------------------------------------------------------------------------------------------------

# -------------- Receipt Function --------------------------------------------------------------------------------------


def receipt():
    txtReceipt.delete("1.0", END)
    txtReceipt.insert(END, 'Sales:\t' + "Vehicle Purchase Invoice \n")
    txtReceipt.insert(END, '#################################' "\n")
    txtReceipt.insert(END, 'Customer Name:\t' + CustomerName.get() + "\n")
    txtReceipt.insert(END, 'Customer Address:\t' + Address.get() + "\n" + "\t" + City.get() + ", " + State.get() +
                      ", " + ZipCode.get() + "\n")
    txtReceipt.insert(END, 'Customer Phone Number:\t' + Telephone.get() + "\n")
    txtReceipt.insert(END, '=================================' "\n")
    txtReceipt.insert(END, 'Vehicle Selected:\t' + CarChoice.get() + "\n")
    txtReceipt.insert(END, 'Vehicle Price:\t' + CarPrice.get() + "\n")
    txtReceipt.insert(END, 'Trade-In Mileage:\t' + TradeInMiles.get() + "\n")
    txtReceipt.insert(END, 'Trade-In Value:\t' + TradeInVal.get() + "\n")
    txtReceipt.insert(END, '=================================' "\n")
    txtReceipt.insert(END, 'Modifications:\t' + Modifications.get() + "\n")
    txtReceipt.insert(END, 'Stereo:\t' + Stereo.get() + "\n")
    txtReceipt.insert(END, 'Leather Interior:\t' + LeatherInterior.get() + "\n")
    txtReceipt.insert(END, 'Custom Details:\t' + CustomDetails.get() + "\n")
    txtReceipt.insert(END, 'GPS Install:\t' + GPS.get() + "\n")
    txtReceipt.insert(END, '=================================' "\n")
    txtReceipt.insert(END, 'VAT:\t' + VAT.get() + "\n")
    txtReceipt.insert(END, 'Discount:\t' + Discount.get() + "\n")
    txtReceipt.insert(END, 'SubTotal:\t' + SubTotal.get() + "\n")
    txtReceipt.insert(END, 'Tax:\t' + Tax.get() + "\n")
    txtReceipt.insert(END, 'Total:\t' + Total.get() + "\n")
    txtReceipt.insert(END, '=================================' "\n")

# ----------------------------------------------------------------------------------------------------------------------

# -------------- Reset Function ----------------------------------------------------------------------------------------


def i_reset():
    CustomerName.set("")
    Address.set("")
    City.set("")
    State.set("")
    ZipCode.set("")
    Telephone.set("")

    Modifications.set("0")
    Stereo.set("0")
    LeatherInterior.set("0")
    CustomDetails.set("0")
    GPS.set("0")

    checkboxMod.set(0)
    checkboxStereo.set(0)
    checkboxLeather.set(0)
    checkboxCustom.set(0)
    checkboxGPS.set(0)

    CarChoice.set("")
    TradeInMiles.set("")
    CarPrice.set("0")
    TradeInVal.set("0")

    VAT.set("")
    Discount.set("")
    checkboxVAT.set(0)
    checkboxDiscount.set(0)
    SubTotal.set("0")
    Tax.set("0")
    Total.set("0")

    txtReceipt.delete("1.0", END)

# ----------------------------------------------------------------------------------------------------------------------

# -------------- Exit Function -----------------------------------------------------------------------------------------


def i_exit():
    t_exit = messagebox.askyesno("Vehicle Trading system", "Confirm if you want to exit")
    if t_exit > 0:
        space.destroy()
        return

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================

# ============== Customer Profile ===== Box 1 ==========================================================================


lblName = Label(cornerLeftFrame, font=('Helvetica', 16, 'bold'), text='Name', fg='black', width=13, bd=10, anchor='w',
                bg='azure3')
lblName.grid(row=0, column=0)
txtName = Entry(cornerLeftFrame, font=('Helvetica', 16, 'bold'), bg='white', width=25, bd=10, justify='left',
                textvariable=CustomerName)
txtName.grid(row=0, column=1)

lblAddress = Label(cornerLeftFrame, font=('Helvetica', 16, 'bold'), text='Address', fg='black', width=13, bd=10,
                   anchor='w', bg='azure3')
lblAddress.grid(row=1, column=0)
txtAddress = Entry(cornerLeftFrame, font=('Helvetica', 16, 'bold'), bg='white', width=25, bd=10, justify='left',
                   textvariable=Address)
txtAddress.grid(row=1, column=1)

lblCity = Label(cornerLeftFrame, font=('Helvetica', 16, 'bold'), text='City', fg='black', width=13, bd=10, anchor='w',
                bg='azure3')
lblCity.grid(row=2, column=0)
txtCity = Entry(cornerLeftFrame, font=('Helvetica', 16, 'bold'), bg='white', width=25, bd=10, justify='left',
                textvariable=City)
txtCity.grid(row=2, column=1)

lblState = Label(cornerLeftFrame, font=('Helvetica', 16, 'bold'), text='State/Province', fg='black', width=13, bd=10,
                 anchor='w', bg='azure3')
lblState.grid(row=3, column=0)
txtState = Entry(cornerLeftFrame, font=('Helvetica', 16, 'bold'), bg='white', width=25, bd=10, justify='left',
                 textvariable=State)
txtState.grid(row=3, column=1)

lblZipCode = Label(cornerLeftFrame, font=('Helvetica', 16, 'bold'), text='Zip/Postal Code', fg='black', width=13, bd=10,
                   anchor='w', bg='azure3')
lblZipCode.grid(row=4, column=0)
txtZipCode = Entry(cornerLeftFrame, font=('Helvetica', 16, 'bold'), bg='white', width=25, bd=10, justify='left',
                   textvariable=ZipCode)
txtZipCode.grid(row=4, column=1)

lblTelephone = Label(cornerLeftFrame, font=('Helvetica', 16, 'bold'), text='Phone Number(s)', fg='black', width=13,
                     bd=10, anchor='w', bg='azure3')
lblTelephone.grid(row=5, column=0)
txtTelephone = Entry(cornerLeftFrame, font=('Helvetica', 16, 'bold'), bg='white', width=25, bd=10, justify='left',
                     textvariable=Telephone)
txtTelephone.grid(row=5, column=1)

# =============== Vehicle Selection ======== Box 2 =====================================================================

lblCarChoice = Label(middleLeftFrame, font=('Helvetica', 16, 'bold'), text='Choose a Car', fg='black', width=12, bd=32,
                     anchor='w', bg='azure3')
lblCarChoice.grid(row=0, column=0)
cmbCarChoice = ttk.Combobox(middleLeftFrame, font=('Helvetica', 16, 'bold'), width=15, state='readonly',
                            textvariable=CarChoice)
cmbCarChoice['value'] = ('', 'Toyota C-HR', 'Toyota Camry', 'Honda HR-V', 'Honda CR-V', 'Volkswagen Tiguan',
                         'Mercedes Benz GLC 350e')
cmbCarChoice.current(0)
cmbCarChoice.grid(row=1, column=0)

lblCarPrice = Label(middleLeftFrame, font=('Helvetica', 16, 'bold'), text='Car Price', fg='black', width=12, bd=32,
                    anchor='w', bg='azure3')
lblCarPrice.grid(row=2, column=0)
txtCarPrice = Entry(middleLeftFrame, font=('Helvetica', 16, 'bold'), bg='white', width=12, bd=16, justify='left',
                    textvariable=CarPrice)
txtCarPrice.grid(row=3, column=0)

lblTradeInMiles = Label(middleLeftFrame, font=('Helvetica', 16, 'bold'), text='Trade-In Mileage', fg='black',
                        width=12, bd=32, anchor='w', bg='azure3')
lblTradeInMiles.grid(row=0, column=1)
cmbTradeInMiles = ttk.Combobox(middleLeftFrame, font=('Helvetica', 16, 'bold'), width=15, state='readonly',
                               textvariable=TradeInMiles)
cmbTradeInMiles['value'] = ('', '200001 - 350000', '170001 - 200000', '120001 - 170000', '100001 - 120000',
                            '50000 - 100000')
cmbTradeInMiles.current(0)
cmbTradeInMiles.grid(row=1, column=1)

lblTradeInVal = Label(middleLeftFrame, font=('Helvetica', 16, 'bold'), text='Max Trade-In Value', fg='black', width=12,
                      bd=32, anchor='w', bg='azure3')
lblTradeInVal.grid(row=2, column=1)
txtTradeInVal = Entry(middleLeftFrame, font=('Helvetica', 16, 'bold'), bg='white', width=12, bd=16, justify='left',
                      textvariable=TradeInVal)
txtTradeInVal.grid(row=3, column=1)

# =============== Vehicle Modifications ====== Box 3 ===================================================================

lblModifications = Checkbutton(cornerBottomFrame, font=('Helvetica', 16, 'bold'), text='Modifications', fg='black',
                               width=13, bd=12, anchor='w', onvalue=1, offvalue=0, variable=checkboxMod, bg='azure3')
lblModifications.grid(row=0, column=0)
txtModifications = Entry(cornerBottomFrame, font=('Helvetica', 16, 'bold'), bg='white', width=23, bd=10, justify='left',
                         textvariable=Modifications)
txtModifications.grid(row=0, column=1)

lblStereo = Checkbutton(cornerBottomFrame, font=('Helvetica', 16, 'bold'), text='Stereo Systems', fg='black',
                        width=13, bd=12, anchor='w', onvalue=1, offvalue=0, variable=checkboxStereo, bg='azure3')
lblStereo.grid(row=1, column=0)
txtStereo = Entry(cornerBottomFrame, font=('Helvetica', 16, 'bold'), bg='white', width=23, bd=10, justify='left',
                  textvariable=Stereo)
txtStereo.grid(row=1, column=1)

lblLeatherInterior = Checkbutton(cornerBottomFrame, font=('Helvetica', 16, 'bold'), text='Leather Interior', fg='black',
                                 width=13, bd=12, anchor='w', onvalue=1, offvalue=0, variable=checkboxLeather,
                                 bg='azure3')
lblLeatherInterior.grid(row=2, column=0)
txtLeatherInterior = Entry(cornerBottomFrame, font=('Helvetica', 16, 'bold'), bg='white', width=23, bd=10,
                           justify='left', textvariable=LeatherInterior)
txtLeatherInterior.grid(row=2, column=1)

lblCustomDetails = Checkbutton(cornerBottomFrame, font=('Helvetica', 16, 'bold'), text='Custom Details', fg='black',
                               width=13, bd=12, anchor='w', onvalue=1, offvalue=0, variable=checkboxCustom, bg='azure3')
lblCustomDetails.grid(row=3, column=0)
txtCustomDetails = Entry(cornerBottomFrame, font=('Helvetica', 16, 'bold'), bg='white', width=23, bd=10, justify='left',
                         textvariable=CustomDetails)
txtCustomDetails.grid(row=3, column=1)

lblGPS = Checkbutton(cornerBottomFrame, font=('Helvetica', 16, 'bold'), text='Global Positioning', fg='black', width=13,
                     bd=12, anchor='w', onvalue=1, offvalue=0, variable=checkboxGPS, bg='azure3')
lblGPS.grid(row=4, column=0)
txtGPS = Entry(cornerBottomFrame, font=('Helvetica', 16, 'bold'), bg='white', width=23, bd=10, justify='left',
               textvariable=GPS)
txtGPS.grid(row=4, column=1)

# --------------- Total and Receipt Buttons ----------------------------------------------------------------------------

btnTotalCost = Button(cornerBottomFrame, pady=8, bd=1, fg="black", font=('Helvetica', 16, 'bold'), width=13,
                      text='Total', bg="white", command=total_cost).grid(row=5, column=0)

btnReceipt = Button(cornerBottomFrame, pady=8, bd=1, fg="black", font=('Helvetica', 16, 'bold'), width=13,
                    text='Receipt', bg="white", command=receipt).grid(row=5, column=1)

# ----------------------------------------------------------------------------------------------------------------------

# ============== Sales Price Calculations ===== Box 4 ==================================================================

lblVAT = Checkbutton(middleBottomFrame, font=('Helvetica', 16, 'bold'), text='VAT', fg='black', width=14, bd=14,
                     anchor='w', onvalue=1, offvalue=0, variable=checkboxVAT, bg='azure3')
lblVAT.grid(row=0, column=0)
txtVAT = Entry(middleBottomFrame, font=('Helvetica', 16, 'bold'), bg='white', width=15, bd=10, justify='left',
               textvariable=VAT)
txtVAT.grid(row=0, column=1)

lblDiscount = Checkbutton(middleBottomFrame, font=('Helvetica', 16, 'bold'), text='Discount', fg='black', width=14,
                          bd=14, anchor='w', onvalue=1, offvalue=0, variable=checkboxDiscount, bg='azure3')
lblDiscount.grid(row=1, column=0)
txtDiscount = Entry(middleBottomFrame, font=('Helvetica', 16, 'bold'), bg='white', width=15, bd=10, justify='left',
                    textvariable=Discount)
txtDiscount.grid(row=1, column=1)

lblSubTotal = Label(middleBottomFrame, font=('Helvetica', 16, 'bold'), text='Subtotal', fg='black', width=14, bd=14,
                    anchor='w', bg='azure3')
lblSubTotal.grid(row=2, column=0)
txtSubTotal = Entry(middleBottomFrame, font=('Helvetica', 16, 'bold'), bg='white', width=15, bd=10, justify='left',
                    textvariable=SubTotal)
txtSubTotal.grid(row=2, column=1)

lblTax = Label(middleBottomFrame, font=('Helvetica', 16, 'bold'), text='Tax', fg='black', width=14, bd=14, anchor='w',
               bg='azure3')
lblTax.grid(row=3, column=0)
txtTax = Entry(middleBottomFrame, font=('Helvetica', 16, 'bold'), bg='white', width=15, bd=10, justify='left',
               textvariable=Tax)
txtTax.grid(row=3, column=1)

lblTotal = Label(middleBottomFrame, font=('Helvetica', 16, 'bold'), text='Total', fg='black', width=14, bd=13,
                 anchor='w', bg='azure3')
lblTotal.grid(row=4, column=0)
txtTotal = Entry(middleBottomFrame, font=('Helvetica', 16, 'bold'), bg='white', width=15, bd=10, justify='left',
                 textvariable=Total)
txtTotal.grid(row=4, column=1)

# --------------- Total and Receipt Buttons ----------------------------------------------------------------------------

btnReset = Button(middleBottomFrame, pady=8, bd=1, fg="black", font=('Helvetica', 16, 'bold'), width=13, text='Reset',
                  bg="white", command=i_reset).grid(row=5, column=0)

btnExit = Button(middleBottomFrame, pady=8, bd=1, fg="black", font=('Helvetica', 16, 'bold'), width=13, text='Exit',
                 bg="white", command=i_exit).grid(row=5, column=1)

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================

# =============== Receipt  Display ===== Right Frame ===================================================================

lblReceipt = Label(rightFrame, font=('Helvetica', 16, 'bold'), text='Receipt', fg='black', bd=2, anchor='w',
                   bg='azure3')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(rightFrame, font=('Helvetica', 16, 'bold'), bg='white', width=33, height=25, bd=2)
txtReceipt.grid(row=1, column=0)

# ======================================================================================================================

# =============== Execution Function ===================================================================================

space.mainloop()
