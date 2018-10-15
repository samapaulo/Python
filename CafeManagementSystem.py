from tkinter import *
from tkinter import messagebox
from random import *
from time import *

# ================ Form Setup ==========================================================================================

space = Tk()
space.title("Cafe Management System")
space.geometry("1200x650+0+0")

# ================ Frame Setup =========================================================================================

topFrame = Frame(space, width=1200, height=125, bd=4)
topFrame.pack(side=TOP)

bottomFrame = Frame(space, width=1200, height=525, bd=4)
bottomFrame.pack(side=BOTTOM)

leftFrame = Frame(bottomFrame, width=700, height=525, bd=4)
leftFrame.pack(side=LEFT)

rightFrame = Frame(bottomFrame, width=700, height=525, bd=4)
rightFrame.pack(side=RIGHT)

topLeftFrame = Frame(leftFrame, width=700, height=375, bd=8)
topLeftFrame.pack(side=TOP)

bottomLeftFrame = Frame(leftFrame, width=700, height=150, bd=8)
bottomLeftFrame.pack(side=BOTTOM)

topRightFrame = Frame(rightFrame, width=500, height=450, bd=4)
topRightFrame.pack(side=TOP)

bottomRightFrame = Frame(rightFrame, width=500, height=75, bd=4)
bottomRightFrame.pack(side=BOTTOM)

# ======================================================================================================================

# ============= Title ==================================================================================================

lblTitle = Label(topFrame, font=("Courier New", 67, 'bold'), text="Cafe Management System", bd=10, fg='darkred',
                 bg='lightsteelblue', anchor='w')
lblTitle.grid(row=0, column=0)

# ======================================================================================================================

# =============== Variable Declarations ================================================================================

# --------------- Beverage Menu Item Variables -------------------------------------------------------------------------

Latte = IntVar(0)
Espresso = IntVar(0)
IcedLatte = IntVar(0)
ValeCoffee = IntVar(0)
Cappuccino = IntVar(0)
AfricanCoffee = IntVar(0)
AmericanCoffee = IntVar(0)
IcedCappuccino = IntVar(0)

e_Latte = IntVar(0)
e_Espresso = IntVar(0)
e_IcedLatte = IntVar(0)
e_ValeCoffee = IntVar(0)
e_Cappuccino = IntVar(0)
e_AfricanCoffee = IntVar(0)
e_AmericanCoffee = IntVar(0)
e_IcedCappuccino = IntVar(0)

# ----------------------------------------------------------------------------------------------------------------------

# -------------- Pastry Menu Item Variables ----------------------------------------------------------------------------

CoffeeCake = IntVar(0)
RedVelvetCake = IntVar(0)
BlackForestCake = IntVar(0)
BostonCreamCake = IntVar(0)
LagosChocCake = IntVar(0)
KilburnChocCake = IntVar(0)
CarltonHillChocCake = IntVar(0)
QueensParkChocCake = IntVar(0)

e_CoffeeCake = IntVar(0)
e_RedVelvetCake = IntVar(0)
e_BlackForestCake = IntVar(0)
e_BostonCreamCake = IntVar(0)
e_LagosChocCake = IntVar(0)
e_KilburnChocCake = IntVar(0)
e_CarltonHillChocCake = IntVar(0)
e_QueensParkChocCake = IntVar(0)

# ----------------------------------------------------------------------------------------------------------------------

# --------------- Cost Variables ---------------------------------------------------------------------------------------

DrinksCost = StringVar()
CakesCost = StringVar()
SrvCharge = StringVar()
ServiceCharge = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Receipt_Ref = StringVar()

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================

# =============== Check Button functions ===============================================================================


def check_button():
    if Latte.get() == 1:
        txtLatte.configure(state=NORMAL)
    elif Latte.get() == 0:
        txtLatte.configure(state=DISABLED)
        e_Latte.set(0)
    if IcedLatte.get() == 1:
        txtIcedLatte.configure(state=NORMAL)
    elif IcedLatte.get() == 0:
        txtIcedLatte.configure(state=DISABLED)
        e_IcedLatte.set(0)
    if Espresso.get() == 1:
        txtEspresso.configure(state=NORMAL)
    elif Espresso.get() == 0:
        txtEspresso.configure(state=DISABLED)
        e_Espresso.set(0)
    if ValeCoffee.get() == 1:
        txtValeCoffee.configure(state=NORMAL)
    elif ValeCoffee.get() == 0:
        txtValeCoffee.configure(state=DISABLED)
        e_ValeCoffee.set(0)
    if Cappuccino.get() == 1:
        txtCappuccino.configure(state=NORMAL)
    elif Cappuccino.get() == 0:
        txtCappuccino.configure(state=DISABLED)
        e_Cappuccino.set(0)
    if AfricanCoffee.get() == 1:
        txtAfricanCoffee.configure(state=NORMAL)
    elif AfricanCoffee.get() == 0:
        txtAfricanCoffee.configure(state=DISABLED)
        e_AfricanCoffee.set(0)
    if AmericanCoffee.get() == 1:
        txtAmericanCoffee.configure(state=NORMAL)
    elif AmericanCoffee.get() == 0:
        txtAmericanCoffee.configure(state=DISABLED)
        e_AmericanCoffee.set(0)
    if IcedCappuccino.get() == 1:
        txtIcedCappuccino.configure(state=NORMAL)
    elif IcedCappuccino.get() == 0:
        txtIcedCappuccino.configure(state=DISABLED)
        e_IcedCappuccino.set(0)
    if CoffeeCake.get() == 1:
        txtCoffeeCake.configure(state=NORMAL)
    elif CoffeeCake.get() == 0:
        txtCoffeeCake.configure(state=DISABLED)
        e_CoffeeCake.set(0)
    if RedVelvetCake.get() == 1:
        txtRedVelvetCake.configure(state=NORMAL)
    elif RedVelvetCake.get() == 0:
        txtRedVelvetCake.configure(state=DISABLED)
        e_RedVelvetCake.set(0)
    if BlackForestCake.get() == 1:
        txtBlackForestCake.configure(state=NORMAL)
    elif BlackForestCake.get() == 0:
        txtBlackForestCake.configure(state=DISABLED)
        e_BlackForestCake.set(0)
    if BostonCreamCake.get() == 1:
        txtBostonCreamCake.configure(state=NORMAL)
    elif BostonCreamCake.get() == 0:
        txtBostonCreamCake.configure(state=DISABLED)
        e_BostonCreamCake.set(0)
    if LagosChocCake.get() == 1:
        txtLagosChocCake.configure(state=NORMAL)
    elif LagosChocCake.get() == 0:
        txtLagosChocCake.configure(state=DISABLED)
        e_LagosChocCake.set(0)
    if KilburnChocCake.get() == 1:
        txtKilburnChocCake.configure(state=NORMAL)
    elif KilburnChocCake.get() == 0:
        txtKilburnChocCake.configure(state=DISABLED)
        e_KilburnChocCake.set(0)
    if CarltonHillChocCake.get() == 1:
        txtCarltonHillChocCake.configure(state=NORMAL)
    elif CarltonHillChocCake.get() == 0:
        txtCarltonHillChocCake.configure(state=DISABLED)
        e_CarltonHillChocCake.set(0)
    if QueensParkChocCake.get() == 1:
        txtQueensParkChocCake.configure(state=NORMAL)
    elif QueensParkChocCake.get() == 0:
        txtQueensParkChocCake.configure(state=DISABLED)
        e_QueensParkChocCake.set(0)

# ======================================================================================================================

# =============== Button Functions =====================================================================================

# --------------- Exit Button ------------------------------------------------------------------------------------------


def q_exit():
    m_exit = messagebox.askyesno("Exit System", "Do you want to quit?")
    if m_exit > 0:
        space.destroy()
        return

# ----------------------------------------------------------------------------------------------------------------------

# ------------- Reset Button -------------------------------------------------------------------------------------------


def reset():
    Latte.set(0)
    Espresso.set(0)
    IcedLatte.set(0)
    ValeCoffee.set(0)
    Cappuccino.set(0)
    AfricanCoffee.set(0)
    AmericanCoffee.set(0)
    IcedCappuccino.set(0)

    e_Latte.set(0)
    e_Espresso.set(0)
    e_IcedLatte.set(0)
    e_ValeCoffee.set(0)
    e_Cappuccino.set(0)
    e_AfricanCoffee.set(0)
    e_AmericanCoffee.set(0)
    e_IcedCappuccino.set(0)

    CoffeeCake.set(0)
    RedVelvetCake.set(0)
    BlackForestCake.set(0)
    BostonCreamCake.set(0)
    LagosChocCake.set(0)
    KilburnChocCake.set(0)
    CarltonHillChocCake.set(0)
    QueensParkChocCake.set(0)

    e_CoffeeCake.set(0)
    e_RedVelvetCake.set(0)
    e_BlackForestCake.set(0)
    e_BostonCreamCake.set(0)
    e_LagosChocCake.set(0)
    e_KilburnChocCake.set(0)
    e_CarltonHillChocCake.set(0)
    e_QueensParkChocCake.set(0)

    DrinksCost.set("0")
    CakesCost.set("0")
    SrvCharge.set("0")
    ServiceCharge.set("0")
    PaidTax.set("0")
    SubTotal.set("0")
    TotalCost.set("0")

    txtReceipt.delete("1.0", END)

    txtLatte.configure(state=DISABLED)
    txtIcedLatte.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtValeCoffee.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtAfricanCoffee.configure(state=DISABLED)
    txtAmericanCoffee.configure(state=DISABLED)
    txtIcedCappuccino.configure(state=DISABLED)
    txtCoffeeCake.configure(state=DISABLED)
    txtRedVelvetCake.configure(state=DISABLED)
    txtBlackForestCake.configure(state=DISABLED)
    txtBostonCreamCake.configure(state=DISABLED)
    txtLagosChocCake.configure(state=DISABLED)
    txtKilburnChocCake.configure(state=DISABLED)
    txtCarltonHillChocCake.configure(state=DISABLED)
    txtQueensParkChocCake.configure(state=DISABLED)


# ----------------------------------------------------------------------------------------------------------------------

# -------- Service Charge ----------------------------------------------------------------------------------------------

def service_charge():

    serve_chrg = float(0)

    if e_Latte.get() > 0:
        serve_chrg += e_Latte.get() * .03
    if e_IcedLatte.get() > 0:
        serve_chrg += e_IcedLatte.get() * .03
    if e_Espresso.get() > 0:
        serve_chrg += e_Espresso.get() * .03
    if e_ValeCoffee.get() > 0:
        serve_chrg += e_ValeCoffee.get() * .03
    if e_Cappuccino.get() > 0:
        serve_chrg += e_Cappuccino.get() * .03
    if e_AfricanCoffee.get() > 0:
        serve_chrg += e_AfricanCoffee.get() * .03
    if e_AmericanCoffee.get() > 0:
        serve_chrg += e_AmericanCoffee.get() * .03
    if e_IcedCappuccino.get() > 0:
        serve_chrg += e_IcedCappuccino.get() * .03
    if e_CoffeeCake.get() > 0:
        serve_chrg += e_CoffeeCake.get() * .07
    if e_RedVelvetCake.get() > 0:
        serve_chrg += e_RedVelvetCake.get() * .07
    if e_BlackForestCake.get() > 0:
        serve_chrg += e_BlackForestCake.get() * .07
    if e_BostonCreamCake.get() > 0:
        serve_chrg += e_BostonCreamCake.get() * .07
    if e_LagosChocCake.get() > 0:
        serve_chrg += e_LagosChocCake.get() * .07
    if e_KilburnChocCake.get() > 0:
        serve_chrg += e_KilburnChocCake.get() * .07
    if e_CarltonHillChocCake.get() > 0:
        serve_chrg += e_CarltonHillChocCake.get() * .07
    if e_QueensParkChocCake.get() > 0:
        serve_chrg += e_QueensParkChocCake.get() * .07

    SrvCharge.set(str("%.2f" % serve_chrg))

# ----------------------------------------------------------------------------------------------------------------------

# --------------- Total Function ---------------------------------------------------------------------------------------


def cost_total():

    drink1 = float(e_Latte.get())
    drink2 = float(e_IcedLatte.get())
    drink3 = float(e_Espresso.get())
    drink4 = float(e_ValeCoffee.get())
    drink5 = float(e_Cappuccino.get())
    drink6 = float(e_AfricanCoffee.get())
    drink7 = float(e_AmericanCoffee.get())
    drink8 = float(e_IcedCappuccino.get())
    
    cake1 = float(e_CoffeeCake.get())
    cake2 = float(e_RedVelvetCake.get())
    cake3 = float(e_BlackForestCake.get())
    cake4 = float(e_BostonCreamCake.get())
    cake5 = float(e_LagosChocCake.get())
    cake6 = float(e_KilburnChocCake.get())
    cake7 = float(e_CarltonHillChocCake.get())
    cake8 = float(e_QueensParkChocCake.get())
    
    price_drinks = (drink1 * 1.5) + (drink2 * 1.99) + (drink3 * 2.05) + (drink4 * 1.85) + (drink5 * 1.95) + \
                   (drink6 * 2.99) + (drink7 * 2.39) + (drink8 * 1.3)
    price_cakes = (cake1 * 2.45) + (cake2 * 2.55) + (cake3 * 2.85) + (cake4 * 3.85) + (cake5 * 2.95) + (cake6 * 3.99) + \
                  (cake7 * 3.45) + (cake8 * 3.95)

    DrinksCost.set("$" + str('%.2f' % price_drinks))
    CakesCost.set("$" + str('%.2f' % price_cakes))
    service_charge()
    subttl = price_drinks + price_cakes + float(SrvCharge.get())
    tax = subttl * 0.085
    ttl = subttl + tax

    ServiceCharge.set("$" + SrvCharge.get())
    SubTotal.set("$" + str("%.2f" % subttl))
    PaidTax.set("$" + str("%.2f" % tax))
    TotalCost.set("$" + str("%.2f" % ttl))

# ----------------------------------------------------------------------------------------------------------------------


# ---------------- Receipt function ------------------------------------------------------------------------------------

def receipt():
    txtReceipt.delete("1.0", END)
    x = randint(100, 39999999)
    random_ref = str(x)
    Receipt_Ref.set("BILL" + random_ref)

    txtReceipt.insert(END, 'Receipt Ref: \t' + Receipt_Ref.get() + '\t\t' + strftime("%b %d, %Y") + "\n\n")
    txtReceipt.insert(END, 'Items \t\t\t' + "Number of Items \n")

    if e_Latte.get() > 0:
        txtReceipt.insert(END, 'Latte \t\t\t' + str(e_Latte.get()) + "\n")
    if e_IcedLatte.get() > 0:
        txtReceipt.insert(END, 'Iced Latte \t\t\t' + str(e_IcedLatte.get()) + "\n")
    if e_Espresso.get() > 0:
        txtReceipt.insert(END, 'Espresso \t\t\t' + str(e_Espresso.get()) + "\n")
    if e_ValeCoffee.get() > 0:
        txtReceipt.insert(END, 'Vale Coffee \t\t\t' + str(e_ValeCoffee.get()) + "\n")
    if e_Cappuccino.get() > 0:
        txtReceipt.insert(END, 'Cappuccino \t\t\t' + str(e_Cappuccino.get()) + "\n")
    if e_AfricanCoffee.get() > 0:
        txtReceipt.insert(END, 'African Coffee \t\t\t' + str(e_AfricanCoffee.get()) + "\n")
    if e_AmericanCoffee.get() > 0:
        txtReceipt.insert(END, 'American Coffee \t\t\t' + str(e_AmericanCoffee.get()) + "\n")
    if e_IcedCappuccino.get() > 0:
        txtReceipt.insert(END, 'Iced Cappuccino \t\t\t' + str(e_IcedCappuccino.get()) + "\n")
    if e_CoffeeCake.get() > 0:
        txtReceipt.insert(END, 'Coffee Cake \t\t\t' + str(e_CoffeeCake.get()) + "\n")
    if e_RedVelvetCake.get() > 0:
        txtReceipt.insert(END, 'Red Velvet Cake \t\t\t' + str(e_RedVelvetCake.get()) + "\n")
    if e_BlackForestCake.get() > 0:
        txtReceipt.insert(END, 'Black Forest Cake \t\t\t' + str(e_BlackForestCake.get()) + "\n")
    if e_BostonCreamCake.get() > 0:
        txtReceipt.insert(END, 'Boston Cream Cake \t\t\t' + str(e_BostonCreamCake.get()) + "\n")
    if e_LagosChocCake.get() > 0:
        txtReceipt.insert(END, 'Lagos Chocolate Cake \t\t\t' + str(e_LagosChocCake.get()) + "\n")
    if e_KilburnChocCake.get() > 0:
        txtReceipt.insert(END, 'Kilburn Chocolate Cake \t\t\t' + str(e_KilburnChocCake.get()) + "\n")
    if e_CarltonHillChocCake.get() > 0:
        txtReceipt.insert(END, 'Carlton Hill Chocolate Cake \t\t\t' + str(e_CarltonHillChocCake.get()) + "\n")
    if e_QueensParkChocCake.get() > 0:
        txtReceipt.insert(END, 'Queens Park Chocolate Cake \t\t\t' + str(e_QueensParkChocCake.get()) + "\n")
    txtReceipt.insert(END, "========================================\n")
    txtReceipt.insert(END, 'Cost of Drinks \t' + DrinksCost.get() + '\t\tTax Paid \t' + PaidTax.get() + "\n\n")
    txtReceipt.insert(END, 'Cost of Cakes \t' + CakesCost.get() + '\t\tSubTotal \t' + SubTotal.get() + "\n\n")
    txtReceipt.insert(END, 'Service Charge \t' + ServiceCharge.get() + '\t\tTotal \t' + TotalCost.get() + "\n\n")


# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================

# =============== Cafe Menu Setup ======================================================================================

# --------------- Beverages --------------------------------------------------------------------------------------------


lblLatte = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, text='Latte', anchor='w', onvalue=1,
                       offvalue=0, variable=Latte, command=check_button)
lblLatte.grid(row=0, column=0)
txtLatte = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                 textvariable=e_Latte)
txtLatte.grid(row=0, column=1)

lblIcedLatte = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, text='Iced Latte', anchor='w',
                           onvalue=1, offvalue=0, variable=IcedLatte, command=check_button)
lblIcedLatte.grid(row=1, column=0)
txtIcedLatte = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                     textvariable=e_IcedLatte)
txtIcedLatte.grid(row=1, column=1)

lblEspresso = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, text='Espresso', anchor='w',
                          onvalue=1, offvalue=0, variable=Espresso, command=check_button)
lblEspresso.grid(row=2, column=0)
txtEspresso = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                    textvariable=e_Espresso)
txtEspresso.grid(row=2, column=1)

lblValeCoffee = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, text='Vale Coffee', anchor='w',
                            onvalue=1, offvalue=0, variable=ValeCoffee, command=check_button)
lblValeCoffee.grid(row=3, column=0)
txtValeCoffee = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                      textvariable=e_ValeCoffee)
txtValeCoffee.grid(row=3, column=1)

lblCappuccino = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, text='Cappuccino', anchor='w',
                            onvalue=1, offvalue=0, variable=Cappuccino, command=check_button)
lblCappuccino.grid(row=4, column=0)
txtCappuccino = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                      textvariable=e_Cappuccino)
txtCappuccino.grid(row=4, column=1)

lblAfricanCoffee = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, text='African Coffee',
                               anchor='w', onvalue=1, offvalue=0, variable=AfricanCoffee, command=check_button)
lblAfricanCoffee.grid(row=5, column=0)
txtAfricanCoffee = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                         textvariable=e_AfricanCoffee)
txtAfricanCoffee.grid(row=5, column=1)

lblAmericanCoffee = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, text='American Coffee',
                                anchor='w', onvalue=1, offvalue=0, variable=AmericanCoffee, command=check_button)
lblAmericanCoffee.grid(row=6, column=0)
txtAmericanCoffee = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                          textvariable=e_AmericanCoffee)
txtAmericanCoffee.grid(row=6, column=1)

lblIcedCappuccino = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, text='Iced Cappuccino',
                                anchor='w', onvalue=1, offvalue=0, variable=IcedCappuccino, command=check_button)
lblIcedCappuccino.grid(row=7, column=0)
txtIcedCappuccino = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                          textvariable=e_IcedCappuccino)
txtIcedCappuccino.grid(row=7, column=1)

# ----------------------------------------------------------------------------------------------------------------------

# --------------- Pastries ---------------------------------------------------------------------------------------------

lblCoffeeCake = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=23, bd=4, text='Coffee Cake', anchor='w',
                            onvalue=1, offvalue=0, variable=CoffeeCake, command=check_button)
lblCoffeeCake.grid(row=0, column=2)
txtCoffeeCake = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                      textvariable=e_CoffeeCake)
txtCoffeeCake.grid(row=0, column=3)

lblRedVelvetCake = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=23, bd=4, text='Red Velvet Cake',
                               anchor='w', onvalue=1, offvalue=0, variable=RedVelvetCake, command=check_button)
lblRedVelvetCake.grid(row=1, column=2)
txtRedVelvetCake = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                         textvariable=e_RedVelvetCake)
txtRedVelvetCake.grid(row=1, column=3)

lblBlackForestCake = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=23, bd=4, text='Black Forest Cake',
                                 anchor='w', onvalue=1, offvalue=0, variable=BlackForestCake, command=check_button)
lblBlackForestCake.grid(row=2, column=2)
txtBlackForestCake = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                           textvariable=e_BlackForestCake)
txtBlackForestCake.grid(row=2, column=3)

lblBostonCreamCake = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=23, bd=4, text='Boston Cream Cake',
                                 anchor='w', onvalue=1, offvalue=0, variable=BostonCreamCake, command=check_button)
lblBostonCreamCake.grid(row=3, column=2)
txtBostonCreamCake = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                           textvariable=e_BostonCreamCake)
txtBostonCreamCake.grid(row=3, column=3)

lblLagosChocCake = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=23, bd=4, text='Lagos Chocolate Cake',
                               anchor='w', onvalue=1, offvalue=0, variable=LagosChocCake, command=check_button)
lblLagosChocCake.grid(row=4, column=2)
txtLagosChocCake = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                         textvariable=e_LagosChocCake)
txtLagosChocCake.grid(row=4, column=3)

lblKilburnChocCake = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=23, bd=4, text='Kilburn Chocolate Cake'
                                 , anchor='w', onvalue=1, offvalue=0, variable=KilburnChocCake, command=check_button)
lblKilburnChocCake.grid(row=5, column=2)
txtKilburnChocCake = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                           textvariable=e_KilburnChocCake)
txtKilburnChocCake.grid(row=5, column=3)

lblCarltonHillChocCake = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=23, bd=4, text='Carlton Hill '
                                                                                                    'Chocolate Cake',
                                     anchor='w', onvalue=1, offvalue=0, variable=CarltonHillChocCake,
                                     command=check_button)
lblCarltonHillChocCake.grid(row=6, column=2)
txtCarltonHillChocCake = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                               textvariable=e_CarltonHillChocCake)
txtCarltonHillChocCake.grid(row=6, column=3)

lblQueensParkChocCake = Checkbutton(topLeftFrame, font=('Arial', 14, 'bold'), width=23, bd=4, text='Queen\'s Park '
                                                                                                   'Chocolate Cake',
                                    anchor='w', onvalue=1, offvalue=0, variable=QueensParkChocCake,
                                    command=check_button)
lblQueensParkChocCake.grid(row=7, column=2)
txtQueensParkChocCake = Entry(topLeftFrame, font=('Arial', 14, 'bold'), width=5, bd=4, justify='left', state=DISABLED,
                              textvariable=e_QueensParkChocCake)
txtQueensParkChocCake.grid(row=7, column=3)

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================

# =============== Cost Calculation Setup ===============================================================================

lblDrinksCost = Label(bottomLeftFrame, font=('Arial', 14, 'bold'), width=12, bd=4, text='Cost of Drinks', anchor='w')
lblDrinksCost.grid(row=0, column=0)
txtDrinksCost = Entry(bottomLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, justify='left',
                      textvariable=DrinksCost)
txtDrinksCost.grid(row=0, column=1)

lblCakeCost = Label(bottomLeftFrame, font=('Arial', 14, 'bold'), width=12, bd=4, text='Cost of Cakes', anchor='w')
lblCakeCost.grid(row=1, column=0)
txtCakeCost = Entry(bottomLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, justify='left', textvariable=CakesCost)
txtCakeCost.grid(row=1, column=1)

lblServiceCharge = Label(bottomLeftFrame, font=('Arial', 14, 'bold'), width=12, bd=4, text='Service Charge', anchor='w')
lblServiceCharge.grid(row=2, column=0)
txtServiceCharge = Entry(bottomLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, justify='left',
                         textvariable=ServiceCharge)
txtServiceCharge.grid(row=2, column=1)

lblPaidTax = Label(bottomLeftFrame, font=('Arial', 14, 'bold'), width=12, bd=4, text='Paid Tax', anchor='w')
lblPaidTax.grid(row=0, column=2)
txtPaidTax = Entry(bottomLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, justify='left', textvariable=PaidTax)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(bottomLeftFrame, font=('Arial', 14, 'bold'), width=12, bd=4, text='SubTotal', anchor='w')
lblSubTotal.grid(row=1, column=2)
txtSubTotal = Entry(bottomLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, justify='left', textvariable=SubTotal)
txtSubTotal.grid(row=1, column=3)

lblTotal = Label(bottomLeftFrame, font=('Arial', 14, 'bold'), width=12, bd=4, text='Total', anchor='w')
lblTotal.grid(row=2, column=2)
txtTotal = Entry(bottomLeftFrame, font=('Arial', 14, 'bold'), width=15, bd=4, justify='left', textvariable=TotalCost)
txtTotal.grid(row=2, column=3)

# ======================================================================================================================

# =============== Receipt  Display ===== Top Right Frame ===============================================================

lblReceipt = Label(topRightFrame, font=('Helvetica', 16, 'bold'), text='Receipt', fg='black', bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(topRightFrame, font=('Helvetica', 16, 'bold'), bg='white', width=40, height=14, bd=2)
txtReceipt.grid(row=1, column=0)

# ======================================================================================================================

# ============= Buttons Setup ====== Bottom Right Frame ================================================================

btnTotal = Button(bottomRightFrame, font=('Helvetica', 14, 'bold'), width=9, bd=4, text='Total', command=cost_total)
btnTotal.grid(row=0, column=0)

btnReceipt = Button(bottomRightFrame, font=('Helvetica', 14, 'bold'), width=9, bd=4, text='Receipt', command=receipt)
btnReceipt.grid(row=0, column=1)

btnReset = Button(bottomRightFrame, font=('Helvetica', 14, 'bold'), width=9, bd=4, text='Reset', command=reset)
btnReset.grid(row=0, column=2)

btnExit = Button(bottomRightFrame, font=('Helvetica', 14, 'bold'), width=9, bd=4, text='Exit', command=q_exit)
btnExit.grid(row=0, column=3)

# ======================================================================================================================

# =============== Main function ========================================================================================

space.mainloop()

