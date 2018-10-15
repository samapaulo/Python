from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
import math
import time
import datetime

space = Tk()
space.geometry("1500x650+0+0")
space.title("Product Control System")
text_insert = StringVar()
operator = ""

topframe = Frame(space, width=1400, height=40, bd=5, relief=RAISED)
topframe.pack(side=TOP)

bttmframe = Frame(space, width=1400, height=600, bd=10, relief=RAISED)
bttmframe.pack(side=BOTTOM)

leftframe = Frame(bttmframe, width=400, height=550, bd=5, relief=RIDGE)
leftframe.pack(side=LEFT)

rightframe = Frame(bttmframe, width=1000, height=550, bd=5, relief=RIDGE)
rightframe.pack(side=RIGHT)

# ===================== local time set up ==============================================================================
localtime = time.asctime(time.localtime(time.time()))
# ======================================================================================================================

# ===================== Title ==========================================================================================
lbltitle = Label(topframe, font=('verdana', 40, 'bold'), text="Product Control System", fg="dark green", width=40,
                 anchor='center')
lbltitle.grid(row=0, column=0)
lbldatetime = Label(topframe, font=('verdana', 15, 'bold'), text=localtime, fg="black", width=30, anchor='center')
lbldatetime.grid(row=1, column=0)
# ======================================================================================================================

# =======================Product Data ==================================================================================

# ----------------------- Product Data CLeft Frame Variables -----------------------------------------------------------
productid = StringVar()
productname = StringVar()
description = StringVar()
stocklvl = IntVar()
primelvl = IntVar()
out_of_stock = IntVar()
num_order = IntVar()
action = StringVar()
reorder_date = StringVar()
discount = IntVar()
unit_cost = DoubleVar()

# ---------------------Product Data Left Frame--------------------------------------------------------------------------

lblproductid = Label(leftframe, font=('helvetica', 16, 'bold'), text='Product ID', bd=10, width=20, anchor='w')
lblproductid.grid(row=0, column=0)
cmbproductid = ttk.Combobox(leftframe, font=('helvetica', 16, 'bold'), textvariable=productid, state='readonly',
                            width=21, justify="center")
cmbproductid['value'] = ('', 'PID001', 'PID002', 'PID003', 'PID004', 'PID005', 'PID006', 'PID007')
cmbproductid.current(0)
cmbproductid.grid(row=0, column=1)

lblproductname = Label(leftframe, font=('helvetica', 16, 'bold'), text='Product Name', bd=10, width=20, anchor='w')
lblproductname.grid(row=1, column=0)
txtproductname = Label(leftframe, font=('helvetica', 16, 'bold'), textvariable=productname,  bd=10, width=20,
                       justify='right', relief='sunken')
txtproductname.grid(row=1, column=1)

lbldescription = Label(leftframe, font=('helvetica', 16, 'bold'), text='Description', bd=10, width=20, anchor='w')
lbldescription.grid(row=2, column=0)
txtdescription = Label(leftframe, font=('helvetica', 16, 'bold'), textvariable=description, bd=10, width=20,
                       justify='right', relief='sunken')
txtdescription.grid(row=2, column=1)

lblstocklvl = Label(leftframe, font=('helvetica', 16, 'bold'), text='Stock Level', bd=10, width=20, anchor='w')
lblstocklvl.grid(row=3, column=0)
txtstocklvl = Entry(leftframe, font=('helvetica', 16, 'bold'), textvariable=stocklvl, bd=10, width=22, justify='center',
                    relief='sunken')
txtstocklvl.grid(row=3, column=1)

lblprimelvl = Label(leftframe, font=('helvetica', 16, 'bold'), text='Prime Stock Level', bd=10, width=20, anchor='w')
lblprimelvl.grid(row=4, column=0)
txtprimelvl = Label(leftframe, font=('helvetica', 16, 'bold'), textvariable=primelvl, bd=10,  width=20, justify='right',
                    relief='sunken')
txtprimelvl.grid(row=4, column=1)

lblout_of_stock = Label(leftframe, font=('helvetica', 16, 'bold'), text='Out_of_Stock', bd=10, width=20, anchor='w')
lblout_of_stock.grid(row=5, column=0)
txtout_of_stock = Label(leftframe, font=('helvetica', 16, 'bold'), textvariable=out_of_stock, bd=10, width=20,
                        justify='right', relief='sunken')
txtout_of_stock.grid(row=5, column=1)

lblnum_order = Label(leftframe, font=('helvetica', 16, 'bold'), text='Numbers to Order', bd=10, width=20, anchor='w')
lblnum_order.grid(row=6, column=0)
txtnum_order = Label(leftframe, font=('helvetica', 16, 'bold'), textvariable=num_order, bd=10, width=20,
                     justify='right', relief='sunken')
txtnum_order.grid(row=6, column=1)

lblaction = Label(leftframe, font=('helvetica', 16, 'bold'), text='Action', bd=10, width=20, anchor='w')
lblaction.grid(row=7, column=0)
txtaction = Label(leftframe, font=('helvetica', 16, 'bold'), textvariable=action, bd=10, width=20, justify='right',
                  relief='sunken')
txtaction.grid(row=7, column=1)

lblreorderdate = Label(leftframe, font=('helvetica', 16, 'bold'), text='Reorder Date', bd=10, width=20, anchor='w')
lblreorderdate.grid(row=8, column=0)
txtreorderdate = Label(leftframe, font=('helvetica', 16, 'bold'), textvariable=reorder_date, bd=10, width=20,
                       justify='right', relief='sunken')
txtreorderdate.grid(row=8, column=1)

lbldiscount = Label(leftframe, font=('helvetica', 16, 'bold'), text='Discount (%)', bd=10, width=20, anchor='w')
lbldiscount.grid(row=9, column=0)
cmbdiscount = ttk.Combobox(leftframe, font=('helvetica', 16, 'bold'), textvariable=discount, state='readonly', width=21,
                           justify="center")
cmbdiscount['value'] = (0, 2, 5, 10, 15, 20)
cmbdiscount.current(0)
cmbdiscount.grid(row=9, column=1)

lblunit_cost = Label(leftframe, font=('helvetica', 16, 'bold'), text='Cost per Unit ($)', bd=10, width=20,
                     anchor='w')
lblunit_cost.grid(row=10, column=0)
txtunit_cost = Entry(leftframe, font=('helvetica', 16, 'bold'), textvariable=unit_cost, bd=10, width=22,
                     justify='center', relief='sunken')
txtunit_cost.grid(row=10, column=1)

# ----------------------------------------------------------------------------------------------------------------------

# -------------------- Product Display Right Frame Variables -----------------------------------------------------------

valid_date = StringVar()
operational_stock = DoubleVar()
order_id = IntVar()
customer_id = IntVar()
firstname = StringVar()
surname = StringVar()
expr_date = StringVar()
on_sales = IntVar()
order_date = StringVar()
item_order_num = StringVar()
item_ordered = StringVar()
payment_method = IntVar()
address = StringVar()
account_type = IntVar()
vat = StringVar()
tax = DoubleVar()
subtotal = DoubleVar()
total = DoubleVar()

# ---------------------Product Data Display Right Frame ----------------------------------------------------------------

# --------------------- Column 1 ---------------------------------------------------------------------------------------
lblvalid_date = Label(rightframe, font=('helvetica', 16, 'bold'), text='Valid From', bd=10, width=15, anchor='w')
lblvalid_date.grid(row=0, column=0)
txtvalid_date = Label(rightframe, font=('helvetica', 16, 'bold'), textvariable=valid_date, bd=10, width=15, 
                      justify='right', relief='sunken')
txtvalid_date .grid(row=0, column=1)

lblopstock = Label(rightframe, font=('helvetica', 16, 'bold'), text='Operational Stock', bd=10, width=15, anchor='w')
lblopstock.grid(row=1, column=0)
txtopstock = Label(rightframe, font=('helvetica', 16, 'bold'), textvariable=operational_stock, bd=10, width=15, 
                   justify='right', relief='sunken')
txtopstock.grid(row=1, column=1)

lblorder_id = Label(rightframe, font=('helvetica', 16, 'bold'), text='Order ID', bd=10, width=15, anchor='w')
lblorder_id.grid(row=2, column=0)
cmborder_id = ttk.Combobox(rightframe, font=('helvetica', 16, 'bold'), textvariable=order_id, state='readonly', 
                           width=16, justify="center")
cmborder_id['value'] = ('', 'ORD091', 'ORD092', 'ORD093', 'ORD094', 'ORD095', 'ORD096', 'ORD097')
cmborder_id.current(0)
cmborder_id.grid(row=2, column=1)

lblcustomer_id = Label(rightframe, font=('helvetica', 16, 'bold'), text='Customer ID', bd=10, width=15, anchor='w')
lblcustomer_id.grid(row=3, column=0)
cmbcustomer_id = ttk.Combobox(rightframe, font=('helvetica', 16, 'bold'), textvariable=customer_id, state='readonly', 
                              width=16, justify="center")
cmbcustomer_id['value'] = ('', 'CID091', 'CID092', 'CID093', 'CID094', 'CID095', 'CID096', 'CID097')
cmbcustomer_id.current(0)
cmbcustomer_id.grid(row=3, column=1)

lblfirstname = Label(rightframe, font=('helvetica', 16, 'bold'), text='First Name', bd=10, width=15, anchor='w')
lblfirstname.grid(row=4, column=0)
txtfirstname = Entry(rightframe, font=('helvetica', 16, 'bold'), textvariable=firstname, bd=10, width=16,
                     justify='left', relief='sunken')
txtfirstname .grid(row=4, column=1)

lblsurname = Label(rightframe, font=('helvetica', 16, 'bold'), text='Surname', bd=10, width=15, anchor='w')
lblsurname.grid(row=5, column=0)
txtsurname = Entry(rightframe, font=('helvetica', 16, 'bold'), textvariable=surname, bd=10, width=16,
                   justify='left', relief='sunken')
txtsurname.grid(row=5, column=1)

lbladdress = Label(rightframe, font=('helvetica', 16, 'bold'), text='Address', bd=10, width=15, anchor='w')
lbladdress.grid(row=6, column=0)
txtaddress = Entry(rightframe, font=('helvetica', 16, 'bold'), textvariable=address, bd=10, width=53,
                   justify='left', relief='sunken')
txtaddress.grid(row=6, column=1, columnspan=4)

lblaccount_type = Label(rightframe, font=('helvetica', 16, 'bold'), text='Account Type', bd=10, width=15, anchor='w')
lblaccount_type.grid(row=7, column=0)
cmbaccount_type = ttk.Combobox(rightframe, font=('helvetica', 16, 'bold'), textvariable=account_type, state='readonly',
                               width=16, justify="center")
cmbaccount_type['value'] = ('', 'Debit Acct', 'Credit Acct', 'Checking Acct', 'Savings Acct')
cmbaccount_type.current(0)
cmbaccount_type.grid(row=7, column=1)

lbltax = Label(rightframe, font=('helvetica', 16, 'bold'), text='Tax', bd=10, width=15, anchor='w')
lbltax.grid(row=8, column=0)
txttax = Label(rightframe, font=('helvetica', 16, 'bold'), textvariable=tax, bd=10, width=15,
               justify='right', relief='sunken')
txttax.grid(row=8, column=1)

lbltotal = Label(rightframe, font=('helvetica', 16, 'bold'), text='Total', bd=10, width=15, anchor='w')
lbltotal.grid(row=9, column=0)
txttotal = Label(rightframe, font=('helvetica', 16, 'bold'), textvariable=total, bd=10, width=15,
                 justify='right', relief='sunken')
txttotal.grid(row=9, column=1)

# --------------------- Column 2 ---------------------------------------------------------------------------------------

lblexprdate = Label(rightframe, font=('helvetica', 16, 'bold'), text='Date Expires', bd=10, width=15, anchor='w')
lblexprdate.grid(row=0, column=2)
txtexprdate = Label(rightframe, font=('helvetica', 16, 'bold'), textvariable=expr_date, bd=10, width=15,
                    justify='right', relief='sunken')
txtexprdate.grid(row=0, column=3)

lblon_sales = Label(rightframe, font=('helvetica', 16, 'bold'), text='On Sales', bd=10, width=15, anchor='w')
lblon_sales.grid(row=1, column=2)
cmbon_sales = ttk.Combobox(rightframe, font=('helvetica', 16, 'bold'), textvariable=on_sales, state='readonly',
                           width=16, justify="center")
cmbon_sales['value'] = ('', 'Yes', 'No')
cmbon_sales.current(0)
cmbon_sales.grid(row=1, column=3)

lblorder_date = Label(rightframe, font=('helvetica', 16, 'bold'), text='Order Date', bd=10, width=15, anchor='w')
lblorder_date.grid(row=2, column=2)
txtorder_date = Label(rightframe, font=('helvetica', 16, 'bold'), textvariable=order_date, bd=10, width=15,
                      justify='right', relief='sunken')
txtorder_date.grid(row=2, column=3)

lblitem_order_num = Label(rightframe, font=('helvetica', 16, 'bold'), text='No. of Item Ordered', bd=10, width=15,
                          anchor='w')
lblitem_order_num.grid(row=3, column=2)
txtitem_order_num = Label(rightframe, font=('helvetica', 16, 'bold'), textvariable=item_order_num, bd=10, width=15,
                          justify='right', relief='sunken')
txtitem_order_num.grid(row=3, column=3)

lblitem_ordered = Label(rightframe, font=('helvetica', 16, 'bold'), text='Item Ordered', bd=10, width=15, anchor='w')
lblitem_ordered.grid(row=4, column=2)
txtitem_ordered = Label(rightframe, font=('helvetica', 16, 'bold'), textvariable=item_ordered, bd=10, width=15,
                        justify='right', relief='sunken')
txtitem_ordered.grid(row=4, column=3)

lblpay_method = Label(rightframe, font=('helvetica', 16, 'bold'), text='Payment Method', bd=10, width=15, anchor='w')
lblpay_method.grid(row=5, column=2)
cmbpay_method = ttk.Combobox(rightframe, font=('helvetica', 16, 'bold'), textvariable=payment_method, state='readonly',
                             width=16, justify="center")
cmbpay_method['value'] = ('', 'VISA', 'MasterCard', 'Discover', 'American Express', 'Paypal', 'Venmo', 'Stripe')
cmbpay_method.current(0)
cmbpay_method.grid(row=5, column=3)

lblvat = Label(rightframe, font=('helvetica', 16, 'bold'), text='VAT', bd=10, width=15, anchor='w')
lblvat.grid(row=7, column=2)
cmbvat = ttk.Combobox(rightframe, font=('helvetica', 16, 'bold'), textvariable=vat, state='readonly',  width=16,
                      justify="center")
cmbvat['value'] = ('', 'Yes', 'No')
cmbvat.grid(row=7, column=3)

lblsubtotal = Label(rightframe, font=('helvetica', 16, 'bold'), text='Sub Total', bd=10, width=15, anchor='w')
lblsubtotal.grid(row=8, column=2)
txtsubtotal = Label(rightframe, font=('helvetica', 16, 'bold'), textvariable=subtotal, bd=10, width=15, justify='right',
                    relief='sunken')
txtsubtotal.grid(row=8, column=3)

# ---------------- Product Select Population ---------------------------------------------------------------------------


def value_op():

    stock_val = int(stocklvl.get())
    stocklvl.set(stock_val)
    outstock_val = int(out_of_stock.get())

    if stock_val <= outstock_val:
        num_order.set(primelvl.get() - stock_val)
        action.set("Low Stock: Reordering")
        operational_stock.set("Reserves " + "%.1f" % stock_val)
        purchase = num_order.get() * unit_cost.get()
        if discount.get() > 0:
            if vat.get() == 'Yes':
                discount_purchase = (purchase - (purchase * (discount.get() / 100)))
                subttl_val = discount_purchase + (discount_purchase * (4.5 / 100))
                subtotal.set("$" + "%.2f" % subttl_val)
            else:
                subttl_val = purchase - (purchase * (discount.get() / 100))
                subtotal.set("$" + "%.2f" % subttl_val)
        elif discount.get() == 0:
            if vat.get() == 'Yes':
                subttl_val = purchase + (purchase * (4.5/100))
                subtotal.set("$" + "%.2f" % subttl_val)
            else:
                subttl_val = purchase
                subtotal.set("$" + "%.2f" % subttl_val)

        tax_val = subttl_val * 0.0895
        tax.set("$" + "%.2f" % tax_val)
        total_val = tax_val + subttl_val
        total.set("$" + "%.2f" % total_val)

        item_order_num.set(num_order.get())
        item_ordered.set(productname.get())

        #-- Order and Reorder Dates entry--#

        reorder_date.set(time.strftime("%a, %b %d, %Y"))
        order_date.set(time.strftime("%a, %b %d, %Y"))

        #---Valid Date Entry -------------#

        #--If order occurs on a weekend, then the valid date will be the following Monday --#

        if datetime.date.today().weekday() == 5 :
            valid_date.set((datetime.date.today() + datetime.timedelta(days=2)).strftime("%a, %b %d, %Y"))
        elif datetime.date.today().weekday() == 6 :
            valid_date.set((datetime.date.today() + datetime.timedelta(days=1)).strftime("%a, %b %d, %Y"))
        else: valid_date.set(time.strftime("%b %d, %Y"))

        #-----------------------------------#

    elif stock_val > primelvl.get():
        num_order.set(0)
        overstock = stock_val - primelvl.get()
        action.set("Overstock of " + "%.0f" % overstock)
        operational_stock.set("%.0f" % (primelvl.get() - outstock_val) + ": Surplus " + "%.0f" % overstock)

    else: num_order.set(0),\
          action.set("Stock Numbers OK"),\
          operational_stock.set(stock_val - outstock_val)


def product():
    if productid.get() == "PID001":
        productname.set("Rice")
        description.set("White Seed")
        primelvl.set(200)
        out_of_stock.set(50)
        if unit_cost.get() == 0:
            unit_cost.set("%.2f" % 0.50)
        value_op()
        if num_order.get() != 0:
            expr_date.set((datetime.date.today() + datetime.timedelta(weeks=52)).strftime("%a, %b %d, %Y"))
        else: expr_date.set("")

    elif productid.get() == "PID002":
        productname.set("Beans")
        description.set("Red Beans")
        primelvl.set(250)
        out_of_stock.set(75)
        if unit_cost.get() == 0:
            unit_cost.set("%.2f" % 0.50)
        value_op()
        if num_order.get() != 0:
            expr_date.set((datetime.date.today() + datetime.timedelta(weeks=52)).strftime("%a, %b %d, %Y"))
        else:
            expr_date.set("")

    elif productid.get() == "PID003":
        productname.set("Peanuts")
        description.set("Salted Peanuts")
        primelvl.set(240)
        out_of_stock.set(70)
        if unit_cost.get() == 0:
            unit_cost.set("%.2f" % 1.40)
        value_op()
        if num_order.get() != 0:
            expr_date.set((datetime.date.today() + datetime.timedelta(weeks=36)).strftime("%a, %b %d, %Y"))
        else:
            expr_date.set("")

    elif productid.get() == "PID004":
        productname.set("Corn")
        description.set("Short Kernel Corn")
        primelvl.set(180)
        out_of_stock.set(20)
        if unit_cost.get() == 0:
            unit_cost.set("%.2f" % 0.75)
        value_op()
        if num_order.get() != 0:
            expr_date.set((datetime.date.today() + datetime.timedelta(weeks=36)).strftime("%a, %b %d, %Y"))
        else:
            expr_date.set("")

    elif productid.get() == "PID005":
        productname.set("Flour")
        description.set("Whole Grain flour")
        primelvl.set(200)
        out_of_stock.set(50)
        if unit_cost.get() == 0:
            unit_cost.set("%.2f" % 2.50)
        value_op()
        if num_order.get() != 0:
            expr_date.set((datetime.date.today() + datetime.timedelta(weeks=52)).strftime("%a, %b %d, %Y"))
        else:
            expr_date.set("")

    elif productid.get() == "PID006":
        productname.set("Cooking Oil")
        description.set("Olive Oil")
        primelvl.set(150)
        out_of_stock.set(15)
        if unit_cost.get() == 0:
            unit_cost.set("%.2f" % 4.50)
        value_op()
        if num_order.get() != 0:
            expr_date.set((datetime.date.today() + datetime.timedelta(weeks=104)).strftime("%a, %b %d, %Y"))
        else:
            expr_date.set("")

    elif productid.get() == "PID007":
        productname.set("Bread")
        description.set("Rye Bread")
        primelvl.set(150)
        out_of_stock.set(25)
        if unit_cost.get() == 0:
            unit_cost.set("%.2f" % 5.50)
        value_op()
        if num_order.get() != 0:
            expr_date.set((datetime.date.today() + datetime.timedelta(weeks=2)).strftime("%a, %b %d, %Y"))
        else:
            expr_date.set("")


def submit():
    submit_msg = messagebox.askyesno("You are about to submit your order", "If indeed click 'YES' otherwise click 'NO'")
    if submit_msg > 0:
        messagebox.showinfo("Order Submitted", "Your Purchase Order has been submitted")
        space.destroy()
        return


def qexit():
    exit_msg = messagebox.askyesno("Your are Exiting the system", "If indeed click 'YES' otherwise click 'NO' ")
    if exit_msg > 0:
        space.destroy()
        return


def reset():
    productid.set("")
    productname.set("")
    description.set("")
    stocklvl.set(0)
    primelvl.set(0)
    out_of_stock.set(0)
    num_order.set(0)
    action.set("")
    discount.set(0)
    unit_cost.set(0.0)
    reorder_date.set("")
    valid_date.set("")
    expr_date.set("")
    order_date.set("")
    operational_stock.set(0)
    order_id.set("")
    customer_id.set("")
    firstname.set("")
    surname.set("")
    expr_date.set("")
    on_sales.set("")
    item_order_num.set("")
    item_ordered.set("")
    payment_method.set("")
    address.set("")
    account_type.set("")
    vat.set("")
    tax.set(0.0)
    subtotal.set(0.0)
    total.set(0.0)

# ------------------ Buttons -------------------------------------------------------------------------------------------

btntotal = Button(rightframe, font=('helvetica', 16, 'bold'), text='Total', bd=5, width='15', command=product)
btntotal.grid(row=10, column=0)

btnreset = Button(rightframe, font=('helvetica', 16, 'bold'), text='Reset', bd=5, width='15', command=reset)
btnreset.grid(row=10, column=1)

btnsubmit = Button(rightframe, font=('helvetica', 16, 'bold'), text='Submit', bd=5, width='15', command=submit)
btnsubmit.grid(row=10, column=2)

btnexit = Button(rightframe, font=('helvetica', 16, 'bold'), text='Exit', bd=5, width='15', command=qexit)
btnexit.grid(row=10, column=3)

# ----------------------------------------------------------------------------------------------------------------------

space.mainloop()
