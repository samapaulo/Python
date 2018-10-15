from tkinter import*
import random
import time


space = Tk()
space.geometry("1500x720+0+0")
space.title("Restaurant Management System")
text_insert = StringVar()
operator = " "

Tops = Frame(space, width=1500, height=100, relief=RAISED)
Tops.pack(side=TOP)

f1 = Frame(space, width=900, height=620, relief=RAISED)
f1.pack(side=LEFT)


f2 = Frame(space, width=400, height=620, relief=RAISED)
f2.pack(side=RIGHT)

# ==========================Time========================================================================================
localtime = time.asctime(time.localtime(time.time()))
# ======================================================================================================================


# =========================Title =======================================================================================
lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Management System", fg="firebrick", bd=10,
                 anchor='w')
lblTitle.grid(row=0, column=0)
lblDateTime = Label(Tops, font=('arial', 15, 'bold'), text=localtime, fg="indigo", bd=10, anchor='w')
lblDateTime.grid(row=1, column=0)
# ======================================================================================================================


# ========================Calculator====================================================================================

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_insert.set(operator)


def btnClear():
    global operator
    operator = ''
    text_insert.set(0)


def btnEquals():
    global operator
    sumUp = str(eval(operator))
    text_insert.set(sumUp)
    operator = ''


numEntry = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_insert, bd=15, insertwidth=4, bg="azure1",
                 justify='right')
numEntry.grid(columnspan=4)

# =========================Number Pad===================================================================================

# -------------------------7-8-9-' + '----------------------------------------------------------------------------------

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="7", bg="azure1",
              command=lambda: btnClick(7)).grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="8", bg="azure1",
              command=lambda: btnClick(8)).grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="9", bg="azure1",
              command=lambda: btnClick(9)).grid(row=2, column=2)

addBtn = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 19, 'bold'), text="+", bg="azure1",
                command=lambda: btnClick('+')).grid(row=2, column=3)

# ------------------------4-5-6-' - '-----------------------------------------------------------------------------------

btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4", bg="azure1",
              command=lambda: btnClick(4)).grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5", bg="azure1",
              command=lambda: btnClick(5)).grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6", bg="azure1",
              command=lambda: btnClick(6)).grid(row=3, column=2)

minusBtn = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="-", bg="azure1",
                  command=lambda: btnClick('-')).grid(row=3, column=3)

# ---------------------3-2-1-' * '--------------------------------------------------------------------------------------

btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="3", bg="azure1",
              command=lambda: btnClick(3)).grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="2", bg="azure1",
              command=lambda: btnClick(2)).grid(row=4, column=1)

btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="1", bg="azure1",
              command=lambda: btnClick(1)).grid(row=4, column=2)

multiplyBtn = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="*", bg="azure1",
                     command=lambda: btnClick('*')).grid(row=4, column=3)

# --------------------0-' . '-'='-'/'-----------------------------------------------------------------------------------

btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="0", bg="azure1",
              command=lambda: btnClick(0)).grid(row=5, column=0)

periodBtn = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=".", bg="azure1",
                   command=lambda: btnClick('.')).grid(row=5, column=1)

equalsBtn = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="=", bg="azure1",
                   command=btnEquals).grid(row=5, column=2)

divideBtn = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 22, 'bold'), text="/", bg="azure1",
                   command=lambda: btnClick('/')).grid(row=5, column=3)

# -------------------C-E-Clear Buttons----------------------------------------------------------------------------------

fillerBtn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="(", bg="azure1",
                    command=lambda: btnClick('(')).grid(row=6, column=0)

fillerBtn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=")", bg="azure1",
                    command=lambda: btnClick(')')).grid(row=6, column=1)

clearBtn = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="c", bg="azure1",
                  command=btnClear).grid(row=6, column=2)

clearEntryBtn = Button(f2, padx=16, pady=18, bd=8, fg="black", font=('arial', 18, 'bold'), text="ce", bg="azure1",
                       command=btnClear).grid(row=6, column=3)

# ----------------------------------------------------------------------------------------------------------------------

# ==================Orders Data Entry===================================================================================

rand = IntVar(0)
Fries = IntVar(0)
Fillet = IntVar(0)
Burger = IntVar(0)
Chicken_Burger = IntVar(0)
Cheese_Burger = IntVar(0)
Drinks = IntVar(0)
Cost = IntVar(0)
Service_Charge = IntVar(0)
Subtotal = IntVar(0)
Tax = IntVar(0)
Total = IntVar(0)


def total_entry():
    x = random.randint(7908, 511987)
    randomEntry = str(x)
    rand.set(randomEntry)

    cost_fries = float(Fries.get())
    cost_fillet = float(Fillet.get())
    cost_burger = float(Burger.get())
    cost_cheeseBgr = float(Cheese_Burger.get())
    cost_chickenBgr = float(Chicken_Burger.get())
    cost_drinks = float(Drinks.get())

    calc_fries = cost_fries * 1.15
    calc_fillet = cost_fillet * 3.95
    calc_burger = cost_burger * 2.17
    calc_cheeseBgr = cost_cheeseBgr * 2.45
    calc_chickenBgr = cost_chickenBgr * 2.35
    calc_drinks = cost_drinks * 0.99

    cost_meal = "$", str('%.2f' % (calc_fries + calc_fillet + calc_burger + calc_drinks
                                   + calc_cheeseBgr + calc_chickenBgr))

    tax_payable = ((calc_fries + calc_fillet + calc_burger + calc_drinks + calc_cheeseBgr
                    + calc_chickenBgr) * 0.0875)

    total_cost = (calc_fries + calc_fillet + calc_burger + calc_drinks + calc_cheeseBgr
                  + calc_chickenBgr)

    ser_charge = ((calc_fries + calc_fillet + calc_burger + calc_drinks + calc_cheeseBgr
                   + calc_chickenBgr)/99)

    service_chrg = "$", str('%.2f' % ser_charge)

    overall_cost = "$", str('%.2f' % (tax_payable + total_cost + ser_charge))

    paid_tax = "$", str('%.2f' % tax_payable)

    Service_Charge.set(service_chrg)
    Cost.set(cost_meal)
    Tax.set(paid_tax)
    Subtotal.set(cost_meal)
    Total.set(overall_cost)


def q_exit():
    space.destroy()


def reset():
    rand.set(0)
    Fries.set(0)
    Fillet.set(0)
    Burger.set(0)
    Chicken_Burger.set(0)
    Cheese_Burger.set(0)
    Drinks.set(0)
    Cost.set(0)
    Service_Charge.set(0)
    Subtotal .set(0)
    Tax.set(0)
    Total.set(0)


# ------------------Order Info 1 ---------------------------------------------------------------------------------------

lblentry = Label(f1, font=('arial', 16, 'bold'), text='Entry ID', bd=16, anchor='w')
lblentry.grid(row=0, column=0)
txtentry = Label(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=2, width=20, justify='right')
txtentry.grid(row=0, column=1)


lblfries = Label(f1, font=('arial', 16, 'bold'), text='Large Fries', bd=16, anchor='w')
lblfries.grid(row=1, column=0)
txtfries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg="azure1", justify='right')
txtfries.grid(row=1, column=1)


lblfillet = Label(f1, font=('arial', 16, 'bold'), text='Fillet-o-Fish', bd=16, anchor='w')
lblfillet.grid(row=2, column=0)
txtfillet = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fillet, bd=10, insertwidth=4, bg="azure1",
                  justify='right')
txtfillet.grid(row=2, column=1)


lblburger = Label(f1, font=('arial', 16, 'bold'), text='Burger', bd=16, anchor='w')
lblburger.grid(row=3, column=0)
txtburger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4,
                  bg="azure1", justify='right')
txtburger.grid(row=3, column=1)


lblchickenBgr = Label(f1, font=('arial', 16, 'bold'), text='Chicken Burger', bd=16, anchor='w')
lblchickenBgr.grid(row=4, column=0)
txtchickenBgr = Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken_Burger, bd=10, insertwidth=4,
                      bg="azure1", justify='right')
txtchickenBgr.grid(row=4, column=1)


lblcheeseBgr = Label(f1, font=('arial', 16, 'bold'), text='Cheese Burger', bd=16, anchor='w')
lblcheeseBgr.grid(row=5, column=0)
txtcheeseBgr = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cheese_Burger, bd=10, insertwidth=4,
                     bg="azure1", justify='right')
txtcheeseBgr.grid(row=5, column=1)

# ---------------Order Info2--------------------------------------------------------------------------------------------

lbldrinks = Label(f1, font=('arial', 16, 'bold'), text='Drinks', bd=16, anchor='w')
lbldrinks.grid(row=1, column=2)
txtdrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="azure1",
                  justify='right')
txtdrinks.grid(row=1, column=3)

lblcost = Label(f1, font=('arial', 16, 'bold'), text='Cost of Meal', bd=16, anchor='w')
lblcost.grid(row=2, column=2)
txtcost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="azure1", justify='right')
txtcost.grid(row=2, column=3)


lblservicechrg = Label(f1, font=('arial', 16, 'bold'), text='Service Charge', bd=16, anchor='w')
lblservicechrg.grid(row=3, column=2)
txtservicechrg = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4, bg="azure1",
                       justify='right')
txtservicechrg.grid(row=3, column=3)


lbltax = Label(f1, font=('arial', 16, 'bold'), text='Sales Tax', bd=16, anchor='w')
lbltax.grid(row=4, column=2)
txttax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4,
               bg="azure1", justify='right')
txttax.grid(row=4, column=3)


lblsubtotal = Label(f1, font=('arial', 16, 'bold'), text='Subtotal', bd=16, anchor='w')
lblsubtotal.grid(row=5, column=2)
txtsubtotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Subtotal, bd=10, insertwidth=4, bg="azure1",
                    justify='right')
txtsubtotal.grid(row=5, column=3)


lbltotal = Label(f1, font=('arial', 16, 'bold'), text='Total Cost', bd=16, anchor='w')
lbltotal.grid(row=6, column=2)
txttotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="azure1", justify='right')
txttotal.grid(row=6, column=3)


# ==========================Buttons=====================================================================================

btntotal = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10, text="Total",
                  bg='azure1', command=total_entry).grid(row=7, column=1)


btnreset = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10, text="Reset",
                  bg='azure1', command=reset).grid(row=7, column=2)


btnexit = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10, text="Exit", bg='azure1',
                 command=q_exit).grid(row=7, column=3)

space.mainloop()
