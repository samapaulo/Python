
from tkinter import *
from tkinter import ttk
from random import *
from time import *
from tkinter import messagebox

# ============ Form Setup ==============================================================================================

space = Tk()
space.title("Train Ticketing System")
space.geometry("1300x600+0+0")

# ======================================================================================================================

# =========== Frame Setup ==============================================================================================

topFrame = Frame(space, width=1300, height=100, bd=4, bg="steelblue")
topFrame.pack(side=TOP)

bottomFrame = Frame(space, width=1300, height=500, bd=1)
bottomFrame.pack(side=BOTTOM)

leftFrame = Frame(bottomFrame, width=900, height=500, bd=2)
leftFrame.pack(side=LEFT)

rightFrame = Frame(bottomFrame, width=500, height=500, bd=2)
rightFrame.pack(side=RIGHT)

topLeftFrame = Frame(leftFrame, width=900, height=250, bd=2)
topLeftFrame.pack(side=TOP)

bottomLeftFrame = Frame(leftFrame, width=900, height=250, bd=2)
bottomLeftFrame.pack(side=BOTTOM)

leftCornerFrame = Frame(bottomLeftFrame, width=450, height=250, bd=2)
leftCornerFrame.pack(side=LEFT)

midCornerFrame = Frame(bottomLeftFrame, width=350, height=250, bd=2)
midCornerFrame.pack(side=RIGHT)

upperRightFrame = Frame(rightFrame, width=500, height=100, bd=2)
upperRightFrame.pack(side=TOP)

lowerRightFrame = Frame(rightFrame, width=500, height=400, bd=2)
lowerRightFrame.pack(side=BOTTOM)

midRightFrame = Frame(lowerRightFrame, width=500, height=300, bd=2)
midRightFrame.pack(side=TOP)

bottomRightFrame = Frame(lowerRightFrame, width=500, height=100, bd=2)
bottomRightFrame.pack(side=BOTTOM)

# ======================================================================================================================

# ============ Titles ==================================================================================================

lblMainTitle = Label(topFrame, font=('Courier News', 70, 'bold'), text="Train Ticketing System", bg="steelblue",
                     anchor='w', width=1300)
lblMainTitle.grid(row=0, column=0)

# ======================================================================================================================

# ============= Variables ==============================================================================================

# ------------- Ticket Selection Variables -----------------------------------------------------------------------------

Class = StringVar()
rd_Class = IntVar()

Destination = StringVar()
Destination2 = StringVar()

chk_OneWay = IntVar(0)
ow = StringVar()
adultOneWay = IntVar(0)
childOneWay = IntVar(0)

chk_Return = IntVar(0)
rt = StringVar()
adultReturn = IntVar(0)
childReturn = IntVar(0)

chk_RoundTrip = IntVar(0)
rndtp = StringVar()
adultRoundTrip = IntVar(0)
childRoundTrip = IntVar(0)

Route = StringVar()
# ----------------------------------------------------------------------------------------------------------------------

# --------------- Date and Time variables ------------------------------------------------------------------------------

date1 = StringVar()
time1 = StringVar()
# ----------------------------------------------------------------------------------------------------------------------

# --------------- Cost Summation Variables -----------------------------------------------------------------------------

StateTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Receipt_Ref = StringVar()

# ----------------------------------------------------------------------------------------------------------------------

# --------------- Calculator Variables ---------------------------------------------------------------------------------

text_input = StringVar()
operator = ''

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================

# ============= Functions ==============================================================================================

# ------------- Calculator Functions -----------------------------------------------------------------------------------


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btnClear():
    global operator
    operator = ''
    text_input.set(0)


def btnEquals():
    global operator
    sum_up = str(eval(operator))
    text_input.set(sum_up)
    operator = ''

# ----------------------------------------------------------------------------------------------------------------------


# ------------- check button function ----------------------------------------------------------------------------------


def check_button():
    if chk_OneWay.get() == 1:
        txtAdultOneWay.configure(state=NORMAL)
        txtChildOneWay.configure(state=NORMAL)
    elif chk_OneWay.get() == 0:
        txtAdultOneWay.configure(state=DISABLED)
        txtChildOneWay.configure(state=DISABLED)
        chk_OneWay.set(0)
        adultOneWay.set(0)
        childOneWay.set(0)
    if chk_Return.get() == 1:
        txtAdultReturn.configure(state=NORMAL)
        txtChildReturn.configure(state=NORMAL)
    elif chk_Return.get() == 0:
        txtAdultReturn.configure(state=DISABLED)
        txtChildReturn.configure(state=DISABLED)
        chk_Return.set(0)
        adultReturn.set(0)
        childReturn.set(0)
    if chk_RoundTrip.get() == 1:
        txtAdultRoundTrip.configure(state=NORMAL)
        txtChildRoundTrip.configure(state=NORMAL)
    elif chk_RoundTrip.get() == 0:
        txtAdultRoundTrip.configure(state=DISABLED)
        txtChildRoundTrip.configure(state=DISABLED)
        chk_RoundTrip.set(0)
        adultRoundTrip.set(0)
        childRoundTrip.set(0)

# ----------------------------------------------------------------------------------------------------------------------

# ------------- Convert, Clear, Reset & Exit functions -----------------------------------------------------------------


def convert():

    date1.set(strftime("%b,%d %Y"))
    time1.set(strftime("%H:%M:%S"))

    if Destination.get() != "":
        Route.set("Direct")
        if rd_Class.get() == 1:
            adultTicketPrice = 7.50
            childTicketPrice = 4.50
            Class.set("Standard")
        elif rd_Class.get() == 2:
            adultTicketPrice = 5.50
            childTicketPrice = 2.50
            Class.set("Economy")
        elif rd_Class.get() == 3:
            adultTicketPrice = 15.50
            childTicketPrice = 10.50
            Class.set("Business")
        else:
            messagebox.showerror("No Class Selection", "You have not chosen a class")
            return
    else:
        messagebox.showerror("No Initial Destination", " Please select the first destination")
        return

    if Destination2.get() != "" and Destination.get() != "":
        Route.set("Connection")
        if rd_Class.get() == 1:
            adultTicketPrice += 5.50
            childTicketPrice += 2.50
        elif rd_Class.get() == 2:
            adultTicketPrice += 3.50
            childTicketPrice += 1.50
        elif rd_Class.get() == 3:
            adultTicketPrice += 10.50
            childTicketPrice += 7.50

    if chk_OneWay.get() == 1:
        ow.set("One Way")
    else:
        ow.set("")
    if chk_Return.get() == 1:
        rt.set("Return")
    else:
        rt.set("")
    if chk_RoundTrip.get() == 1:
        rndtp.set("Round Trip")
    else:
        rndtp.set("")

    total_adult_price = adultOneWay.get() + adultReturn.get() + 2*adultRoundTrip.get()
    total_child_price = childOneWay.get() + childReturn.get() + 2*childRoundTrip.get()

    total_ticket_price = adultTicketPrice * float(total_adult_price) + childTicketPrice * float(total_child_price)

    tax = total_ticket_price * 0.0882

    cost_total = total_ticket_price + tax

    SubTotal.set("$" + '%.2f' % total_ticket_price)
    StateTax.set("$" + '%.2f' % tax)
    TotalCost.set("$" + '%.2f' % cost_total)

    x = randint(100, 39999999)
    random_ref = str(x)
    Receipt_Ref.set(random_ref)


def reset():
    Class.set("")

    rd_Class.set(0)

    Destination.set("")
    Destination2.set("")

    adultOneWay.set(0)
    childOneWay.set(0)
    adultReturn.set(0)
    childReturn.set(0)
    adultRoundTrip.set(0)
    childRoundTrip.set(0)
    chk_OneWay.set(0)
    chk_Return.set(0)
    chk_RoundTrip.set(0)

    date1.set("")
    time1.set("")

    StateTax.set("0")
    SubTotal.set("0")
    TotalCost.set("0")
    Receipt_Ref.set("")

    text_input.set("")


def i_exit():
    m_exit = messagebox.askyesno("Exit System", " Do you want to quit?")
    if m_exit > 0:
        space.destroy()
        return
# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================

# ============= Form Setup =============================================================================================

# ------------- Passenger Class Selection ------------------------------------------------------------------------------


lblClass = Label(topLeftFrame, font=('Helvetica', 15, 'bold'), text="Class", width=11, anchor='w')
lblClass.grid(row=0, column=0, sticky=W)
rdStandard = Radiobutton(topLeftFrame, font=('Helvetica', 15, 'bold'), text='Standard', variable=rd_Class, value=1)
rdStandard.grid(row=1, column=0, sticky=W)
rdEconomy = Radiobutton(topLeftFrame, font=('Helvetica', 15, 'bold'), text='Economy', variable=rd_Class, value=2)
rdEconomy.grid(row=2, column=0, sticky=W)
rdBusiness = Radiobutton(topLeftFrame, font=('Helvetica', 15, 'bold'), text='Business', variable=rd_Class, value=3)
rdBusiness.grid(row=3, column=0, sticky=W)

# ----------------------------------------------------------------------------------------------------------------------

# ------------------ Destination----------------------------------------------------------------------------------------

lblSelect = Label(topLeftFrame, font=('Helvetica', 15, 'bold'), text="Select Destination")
lblSelect.grid(row=0, column=1, sticky=W, columnspan=2)

lblDestination = Label(topLeftFrame, font=('Helvetica', 15, 'bold'), text="Destination")
lblDestination.grid(row=1, column=1, sticky=W)
cmbDestination = ttk.Combobox(topLeftFrame, font=('Helvetica', 15, 'bold'), textvariable=Destination, width=12,
                              state='readonly')
cmbDestination['value'] = ('', 'Brooklyn', 'Queens', 'Broadway', 'Wall Street', 'Harlem', 'The Bronx')
cmbDestination.current(0)
cmbDestination.grid(row=1, column=2)

lblDestination2 = Label(topLeftFrame, font=('Helvetica', 15, 'bold'), text="Other Destination")
lblDestination2.grid(row=3, column=1, sticky=W)
cmbDestination2 = ttk.Combobox(topLeftFrame, font=('Helvetica', 15, 'bold'), textvariable=Destination2, width=12,
                               state='readonly')
cmbDestination2['value'] = ('', 'Staten Island', 'The Hamptons', 'Connecticut', 'Newark')
cmbDestination2.current(0)
cmbDestination2.grid(row=3, column=2)

# ----------------------------------------------------------------------------------------------------------------------

# ----------------- Tickets --------------------------------------------------------------------------------------------

lblTicket = Label(topLeftFrame, font=('Helvetica', 15, 'bold'), text="Ticket Type")
lblTicket.grid(row=0, column=3, sticky=W)

lblAdult = Label(topLeftFrame, font=('Helvetica', 15, 'bold'), text="Adult")
lblAdult.grid(row=0, column=4, sticky=W)

lblChild = Label(topLeftFrame, font=('Helvetica', 15, 'bold'), text="Child")
lblChild.grid(row=0, column=5, sticky=W)

chkOneWay = Checkbutton(topLeftFrame, font=('Helvetica', 15, 'bold'), text='One Way', variable=chk_OneWay, onvalue=1,
                        offvalue=0, command=check_button)
chkOneWay.grid(row=1, column=3, sticky=W)
txtAdultOneWay = Entry(topLeftFrame, font=('Helvetica', 15, 'bold'), textvariable=adultOneWay, width=7, justify='right',
                       state=DISABLED)
txtAdultOneWay.grid(row=1, column=4)
txtChildOneWay = Entry(topLeftFrame, font=('Helvetica', 15, 'bold'), textvariable=childOneWay, width=7, justify='right',
                       state=DISABLED)
txtChildOneWay.grid(row=1, column=5)

chkReturn = Checkbutton(topLeftFrame, font=('Helvetica', 15, 'bold'), text='Return', variable=chk_Return, onvalue=1,
                        offvalue=0, command=check_button)
chkReturn.grid(row=2, column=3, sticky=W)
txtAdultReturn = Entry(topLeftFrame, font=('Helvetica', 15, 'bold'), textvariable=adultReturn, width=7, justify='right',
                       state=DISABLED)
txtAdultReturn.grid(row=2, column=4)
txtChildReturn = Entry(topLeftFrame, font=('Helvetica', 15, 'bold'), textvariable=childReturn, width=7, justify='right',
                       state=DISABLED)
txtChildReturn.grid(row=2, column=5)

chkRoundTrip = Checkbutton(topLeftFrame, font=('Helvetica', 15, 'bold'), text='Round Trip', variable=chk_RoundTrip,
                           onvalue=1, offvalue=0, command=check_button)
chkRoundTrip.grid(row=3, column=3, sticky=W)
txtAdultRoundTrip = Entry(topLeftFrame, font=('Helvetica', 15, 'bold'), textvariable=adultRoundTrip, width=7,
                          justify='right', state=DISABLED)
txtAdultRoundTrip.grid(row=3, column=4)
txtChildRoundTrip = Entry(topLeftFrame, font=('Helvetica', 15, 'bold'), textvariable=childRoundTrip, width=7,
                          justify='right', state=DISABLED)
txtChildRoundTrip.grid(row=3, column=5)

# ----------------------------------------------------------------------------------------------------------------------

# ---------------- Cost Summation --------------------------------------------------------------------------------------

lblSubTotal = Label(leftCornerFrame, font=('Helvetica', 15, 'bold'), text='SubTotal', bd=16, anchor='w')
lblSubTotal.grid(row=0, column=2)
txtSubTotal = Entry(leftCornerFrame, font=('Helvetica', 20, 'bold'), textvariable=SubTotal, bd=4, insertwidth=15,
                    bg='#ffffff', justify='right')
txtSubTotal.grid(row=0, column=3)

lblStateTax = Label(leftCornerFrame, font=('Helvetica', 15, 'bold'), text='State Tax', bd=16, anchor='w')
lblStateTax.grid(row=1, column=2)
txtStateTax = Entry(leftCornerFrame, font=('Helvetica', 20, 'bold'), textvariable=StateTax, bd=4, insertwidth=15,
                    bg='#ffffff', justify='right')
txtStateTax.grid(row=1, column=3)

lblTotalCost = Label(leftCornerFrame, font=('Helvetica', 15, 'bold'), text='Total', bd=16, anchor='w')
lblTotalCost.grid(row=2, column=2)
txtTotalCost = Entry(leftCornerFrame, font=('Helvetica', 20, 'bold'), textvariable=TotalCost, bd=4, insertwidth=15,
                     bg='#ffffff', justify='right')
txtTotalCost.grid(row=2, column=3)

# ----------------------------------------------------------------------------------------------------------------------

# ---------------- Calculator ------------------------------------------------------------------------------------------

txtDisplay = Entry(midCornerFrame, font=('Helvetica', 23, 'bold'), textvariable=text_input, bd=4, justify='right',
                   bg='lightgreen', insertwidth=9)
txtDisplay.grid(columnspan=4)

# -------------------------7-8-9-' + '----------------------------------------------------------------------------------

btn7 = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="7", bg="azure1",
              command=lambda: btnClick(7)).grid(row=2, column=0)

btn8 = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="8", bg="azure1",
              command=lambda: btnClick(8)).grid(row=2, column=1)

btn9 = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="9", bg="azure1",
              command=lambda: btnClick(9)).grid(row=2, column=2)

addBtn = Button(midCornerFrame, padx=30, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="+", bg="azure1",
                command=lambda: btnClick('+')).grid(row=2, column=3)

# ------------------------4-5-6-' - '-----------------------------------------------------------------------------------

btn4 = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="4", bg="azure1",
              command=lambda: btnClick(4)).grid(row=3, column=0)

btn5 = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="5", bg="azure1",
              command=lambda: btnClick(5)).grid(row=3, column=1)

btn6 = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="6", bg="azure1",
              command=lambda: btnClick(6)).grid(row=3, column=2)

minusBtn = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="-", bg="azure1",
                  command=lambda: btnClick('-')).grid(row=3, column=3)

# ---------------------3-2-1-' * '--------------------------------------------------------------------------------------

btn3 = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="3", bg="azure1",
              command=lambda: btnClick(3)).grid(row=4, column=0)

btn2 = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="2", bg="azure1",
              command=lambda: btnClick(2)).grid(row=4, column=1)

btn1 = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="1", bg="azure1",
              command=lambda: btnClick(1)).grid(row=4, column=2)

multiplyBtn = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="*",
                     bg="azure1", command=lambda: btnClick('*')).grid(row=4, column=3)

# --------------------0-' . '-'='-'/'-----------------------------------------------------------------------------------

btn0 = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="0", bg="azure1",
              command=lambda: btnClick(0)).grid(row=5, column=0)

periodBtn = Button(midCornerFrame, padx=34, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text=".",
                   bg="azure1", command=lambda: btnClick('.')).grid(row=5, column=1)

equalsBtn = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="=",
                   bg="azure1", command=btnEquals).grid(row=5, column=2)

divideBtn = Button(midCornerFrame, padx=33, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="/",
                   bg="azure1", command=lambda: btnClick('/')).grid(row=5, column=3)

# -------------------C-E-Clear Buttons----------------------------------------------------------------------------------

parenthesisBtn1 = Button(midCornerFrame, padx=34, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="(",
                         bg="azure1", command=lambda: btnClick('(')).grid(row=6, column=0)

parenthesisBtn2 = Button(midCornerFrame, padx=34, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text=")",
                         bg="azure1", command=lambda: btnClick(')')).grid(row=6, column=1)

clearBtn = Button(midCornerFrame, padx=32, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="c",
                  bg="azure1", command=btnClear).grid(row=6, column=2)

clearEntryBtn = Button(midCornerFrame, padx=26, pady=10, bd=2, fg="black", font=('arial', 12, 'bold'), text="ce",
                       bg="azure1", command=btnClear).grid(row=6, column=3)

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================

# =========== Receipt Form Setup =======================================================================================

lblTravelTitle = Label(upperRightFrame, font=('Courier News', 30, 'bold'), text="Travel Ticketing System", width=500,
                       bg="azure3", anchor='w')
lblTravelTitle.grid(row=0, column=0)


lblClassRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="Class", width=9, relief="sunken",
                     justify="center")
lblClassRcpt.grid(row=0, column=0)
txtClassRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                     textvariable=Class)
txtClassRcpt.grid(row=1, column=0)

lblTicketRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="Ticket", width=9, relief="sunken",
                      justify="center")
lblTicketRcpt.grid(row=0, column=1)
txtTicket1Rcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                       textvariable=ow)
txtTicket1Rcpt.grid(row=1, column=1)
txtTicket2Rcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                       textvariable=rt)
txtTicket2Rcpt.grid(row=2, column=1)
txtTicket3Rcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                       textvariable=rndtp)
txtTicket3Rcpt.grid(row=3, column=1)

lblAdultRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="Adult", width=9, relief="sunken",
                     justify="center")
lblAdultRcpt.grid(row=0, column=2)
txtAdult1Rcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                      textvariable=adultOneWay)
txtAdult1Rcpt.grid(row=1, column=2)
txtAdult2Rcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                      textvariable=adultReturn)
txtAdult2Rcpt.grid(row=2, column=2)
txtAdult3Rcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                      textvariable=adultRoundTrip)
txtAdult3Rcpt.grid(row=3, column=2)

lblChildRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="Child", width=9, relief="sunken",
                     justify="center")
lblChildRcpt.grid(row=0, column=3)
txtChild1Rcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                      textvariable=childOneWay)
txtChild1Rcpt.grid(row=1, column=3)
txtChild2Rcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                      textvariable=childReturn)
txtChild2Rcpt.grid(row=2, column=3)
txtChild3Rcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                      textvariable=childRoundTrip)
txtChild3Rcpt.grid(row=3, column=3)

lblblank0 = Label(midRightFrame).grid(row=4, column=0, columnspan=4)

lblFromRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="From", width=9, relief="sunken",
                    justify="center")
lblFromRcpt.grid(row=5, column=0)
txtFromRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                    text='Central Stn')
txtFromRcpt.grid(row=5, column=1)

lblToRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="To", width=9, relief="sunken",
                  justify="center")
lblToRcpt.grid(row=6, column=0)
txtToRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                  textvariable=Destination)
txtToRcpt.grid(row=6, column=1)

lblOtherDestRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="Other Dest.", width=9, relief="sunken",
                         justify="center")
lblOtherDestRcpt.grid(row=7, column=0)
txtOtherDestRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                         textvariable=Destination2)
txtOtherDestRcpt.grid(row=7, column=1)

lblPriceRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="Price", width=9, relief="sunken",
                     justify="center")
lblPriceRcpt.grid(row=8, column=0)
txtPriceRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                     textvariable=TotalCost)
txtPriceRcpt.grid(row=8, column=1)

lblblank1 = Label(midRightFrame).grid(row=9, column=0, columnspan=4)

lblRefRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="Ref_Num", width=9, relief="sunken",
                   justify="center")
lblRefRcpt.grid(row=10, column=0)
txtRefRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                   textvariable=Receipt_Ref)
txtRefRcpt.grid(row=11, column=0)

lblTimeRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="Time", width=9, relief="sunken",
                    justify="center")
lblTimeRcpt.grid(row=10, column=1)
txtTimeRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", textvariable=time1,
                    justify="center")
txtTimeRcpt.grid(row=11, column=1)

lblDateRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="Date", width=9, relief="sunken",
                    justify="center")
lblDateRcpt.grid(row=10, column=2)
txtDateRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", textvariable=date1,
                    justify="center")
txtDateRcpt.grid(row=11, column=2)

lblRouteRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), text="Route", width=9, relief="sunken",
                     justify="center")
lblRouteRcpt.grid(row=10, column=3)
txtRouteRcpt = Label(midRightFrame, font=('Helvetica', 15, 'bold'), width=9, relief="sunken", justify="center",
                     textvariable=Route)
txtRouteRcpt.grid(row=11, column=3)

# ======================================================================================================================

# =============== Buttons Setup ========================================================================================

btnTotal = Button(bottomRightFrame, width=9, height=1, text='Convert', padx=2, pady=2, bd=2, fg="black",
                  font=('Helvetica', 15, 'bold'), command=convert).grid(row=0, column=0)
btnClear = Button(bottomRightFrame, width=9, height=1, text='Clear', padx=2, pady=2, bd=2, fg="black",
                  font=('Helvetica', 15, 'bold'), command=reset).grid(row=0, column=1)
btnReset = Button(bottomRightFrame, width=9, height=1, text='Reset', padx=2, pady=2, bd=2, fg="black",
                  font=('Helvetica', 15, 'bold'), command=reset).grid(row=0, column=2)
btnExit = Button(bottomRightFrame, width=9, height=1, text='Exit', padx=2, pady=2, bd=2, fg="black",
                 font=('Helvetica', 15, 'bold'), command=i_exit).grid(row=0, column=3)

# ======================================================================================================================

# =========== main function ============================================================================================

space.mainloop()
