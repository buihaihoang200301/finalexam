from tkinter import *
from tkinter import ttk
import random
import time;
import datetime
from tkinter import filedialog
from tkinter.filedialog import askopenfiles, asksaveasfile
import tkinter.messagebox
import login

class water:
    def __init__(self, root1):
        self.root1 = root1
        self.root1.title("Water information management system")
        self.root1.geometry("1350x700+0+0")
        self.root1.configure(background='powder blue')

        # nameTable=StringVar()
        name = StringVar()
        id = StringVar()
        address = StringVar()
        mail = StringVar()
        phone = StringVar()
        amount = StringVar()
        f = StringVar()
        to = StringVar()
        price = StringVar()
        cost = StringVar()

        bill = StringVar()

        # ==============================Function==========================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Water information management system", "Are you sure?")
            if iExit > 0:
                root1.destroy()
                return

        def iReset():
            name.set("")
            id.set("")
            address.set("")
            mail.set("")
            phone.set("")
            amount.set("")
            f.set("")
            to.set("")
            price.set("")
            cost.set("")
            self.txtFrameDetail.delete("1.0", END)
            self.txtbill.delete("1.0", END)
            return

        def iDelete():
            name.set("")
            id.set("")
            address.set("")
            mail.set("")
            phone.set("")
            amount.set("")
            f.set("")
            to.set("")
            price.set("")
            cost.set("")

            self.txtbill.delete("1.0", END)
            # self.txtFrameDetail.delete("1.0",END)
            return

        def iBill():
            self.txtbill.insert(END, 'ID: \t\t' + id.get() + "\n")
            self.txtbill.insert(END, 'Name: \t\t' + name.get() + "\n")
            self.txtbill.insert(END, 'Address: \t\t' + address.get() + "\n")
            self.txtbill.insert(END, 'Mail: \t\t' + mail.get() + "\n")
            self.txtbill.insert(END, 'Phone: \t\t' + phone.get() + "\n")
            self.txtbill.insert(END, 'Amount: \t\t' + amount.get() + "\n")
            self.txtbill.insert(END, 'From: \t\t' + f.get() + "\n")
            self.txtbill.insert(END, 'To: \t\t' + to.get() + "\n")
            self.txtbill.insert(END, 'Price: \t\t' + price.get() + "\n")
            self.txtbill.insert(END, 'Cost: \t\t' + cost.get() + "\n")
	    
            return

        def iData():
            self.txtFrameDetail.insert(END, "      " +
                                       name.get() + "         " + id.get() + "	                 " + address.get() + "		                  " + mail.get() + "          	" + phone.get() + "                          " + amount.get() + "	                      " + f.get() + "		         " + to.get() + "		               " + price.get() + "		               " + cost.get() + "\n")
            return

        def iCalculate():
            a = float(amount.get())
            p = float(price.get())
            c = a * p
            cost.set(c)
            return

        def iSave():
            # text = Text(root)
            file=filedialog.asksaveasfile(defaultextension='.txt',
                                          filetypes=[
                                              ("Text file",".txt"),
                                              ("Html file", ".html"),
                                              ("All file", ".*"),

                                          ])
            filetext = self.txtbill.get("1.0",END)
            file.write(filetext)
            file.close()
            return


        # =======================FRAMEEEEEEEEE==========================================================

        mainFrame = Frame(self.root1)
        mainFrame.config(bg = "#DFDFDE")
        mainFrame.grid()

        titleFrame = Frame(mainFrame, width=1350, padx=30, relief=RIDGE)
        titleFrame.pack(side=TOP)

        self.lbtitle = Label(titleFrame, font=('arial', 40, 'bold'), text="Water Information Management System", padx=2)
        self.lbtitle.grid()

        ButtonFrame = Frame(mainFrame, bd=8, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(mainFrame, bd=8, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)


        DataFrame = Frame(mainFrame, bd=8, width=1350, height=200, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        DataFrame.config(bg = "#DFDFDE")

        InputFrame = LabelFrame(DataFrame, bd=3, width=800, height=400, padx=20, relief=RIDGE, font=('arial',12,'bold'), text= "Customer Information:")
        InputFrame.pack(side=LEFT)
        InputFrame.config(bg = "#DFDFDE")


        BillFrame = LabelFrame(DataFrame, bd=3, width=450, height=400, padx=20, relief=RIDGE, font=('arial',12,'bold'), text= "Bill:")
        BillFrame.pack(side=RIGHT)
        BillFrame.config(bg = "#DFDFDE")



        # ==================================INPUT===================================
        # ==================================INPUT===================================
        # ==================================INPUT===================================
        # ==================================INPUT===================================

        self.lbname = Label(InputFrame, font=('arial', 12, 'bold'), text="Name:", padx=2, pady=2)
        self.lbname.grid(row=0, column=0, stick=W)
        self.lbname.config(bg ="#DFDFDE")
        self.txtname = Entry(InputFrame, font=('arial', 12, 'bold'), textvariable=name)
        self.txtname.grid(row=0, column=1)

        self.lbid = Label(InputFrame, font=('arial', 12, 'bold'), text="ID:", padx=2, pady=2)
        self.lbid.grid(row=1, column=0, stick=W)
        self.lbid.config(bg ="#DFDFDE")
        self.txtid = Entry(InputFrame, font=('arial', 12, 'bold'), textvariable=id)
        self.txtid.grid(row=1, column=1)

        self.lbaddress = Label(InputFrame, font=('arial', 12, 'bold'), text="Address:", padx=2, pady=2)
        self.lbaddress.grid(row=2, column=0, stick=W)
        self.lbaddress.config(bg ="#DFDFDE")
        self.txtaddress = Entry(InputFrame, font=('arial', 12, 'bold'), textvariable=address)
        self.txtaddress.grid(row=2, column=1)

        self.lbmail = Label(InputFrame, font=('arial', 12, 'bold'), text="Mail:", padx=2, pady=2)
        self.lbmail.grid(row=3, column=0, stick=W)
        self.lbmail.config(bg ="#DFDFDE")
        self.txtmail = Entry(InputFrame, font=('arial', 12, 'bold'), textvariable=mail)
        self.txtmail.grid(row=3, column=1)

        self.lbphone = Label(InputFrame, font=('arial', 12, 'bold'), text="Phone:", padx=2, pady=2)
        self.lbphone.grid(row=4, column=0, stick=W)
        self.lbphone.config(bg ="#DFDFDE")
        self.txtphone = Entry(InputFrame, font=('arial', 12, 'bold'), textvariable=phone)
        self.txtphone.grid(row=4, column=1)

        self.lbamount = Label(InputFrame, font=('arial', 12, 'bold'), text="Amount(m3):", padx=2, pady=2)
        self.lbamount.grid(row=5, column=0, stick=W)
        self.lbamount.config(bg ="#DFDFDE")
        self.txtamount = Entry(InputFrame, font=('arial', 12, 'bold'), textvariable=amount)
        self.txtamount.grid(row=5, column=1)

        self.lbfrom = Label(InputFrame, font=('arial', 12, 'bold'), text="From:", padx=2, pady=2)
        self.lbfrom.grid(row=6, column=0, stick=W)
        self.lbfrom.config(bg ="#DFDFDE")
        self.txtfrom = Entry(InputFrame, font=('arial', 12, 'bold'), textvariable=f)
        self.txtfrom.grid(row=6, column=1)

        self.lbto = Label(InputFrame, font=('arial', 12, 'bold'), text="To:", padx=2, pady=2)
        self.lbto.grid(row=7, column=0, stick=W)
        self.lbto.config(bg ="#DFDFDE")
        self.txtto = Entry(InputFrame, font=('arial', 12, 'bold'), textvariable=to)
        self.txtto.grid(row=7, column=1)

        self.lbprice = Label(InputFrame, font=('arial', 12, 'bold'), text="Price(VND/m3):", padx=2, pady=2)
        self.lbprice.grid(row=8, column=0, stick=W)
        self.lbprice.config(bg ="#DFDFDE")
        self.txtprice = Entry(InputFrame, font=('arial', 12, 'bold'), textvariable=price)
        self.txtprice.grid(row=8, column=1)

        self.lbcost = Label(InputFrame, font=('arial', 12, 'bold'), text="Cost(VND):", padx=2, pady=2)
        self.lbcost.grid(row=9, column=0, stick=W)
        self.lbcost.config(bg ="#DFDFDE")
        self.txtcost = Entry(InputFrame, font=('arial', 12, 'bold'), textvariable=cost)
        self.txtcost.grid(row=9, column=1)

        # ==================================Bill===================================
        # ==================================Bill===================================
        # ==================================Bill===================================

        self.txtbill = Text(BillFrame, font=('arial', 12, 'bold'), width=50, height=20, padx=2, pady=6)
        self.txtbill.grid(row=0, column=0, stick=W)
        self.txtbill.config(bg ="#DFDFDE")

        # ==================================ButtonFrame===================================
        # ==================================ButtonFrame===================================
        # ==================================ButtonFrame===================================

        self.btncal = Button(ButtonFrame, text='Calculate', font=('arial', 12, 'bold'), width=17, bd=4,
                             command=iCalculate)
        self.btncal.grid(row=0, column=0)

        self.btnBill = Button(ButtonFrame, text='Print bill', font=('arial', 12, 'bold'), width=17, bd=4, command=iBill)
        self.btnBill.grid(row=0, column=1)

        self.btnData = Button(ButtonFrame, text='Add data', font=('arial', 12, 'bold'), width=17, bd=4, command=iData)
        self.btnData.grid(row=0, column=2)

        self.btnDelete = Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'), width=17, bd=4, command=iDelete)
        self.btnDelete.grid(row=0, column=3)

        self.btnReset = Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'), width=17, bd=4, command=iReset)
        self.btnReset.grid(row=0, column=4)

        self.btnExit = Button(ButtonFrame, text='Exit', fg='red', font=('arial', 12, 'bold'), width=17, bd=4,
                              command=iExit)
        self.btnExit.grid(row=0, column=5)

        self.btnSave = Button(ButtonFrame, text='Save', fg='red', font=('arial', 12, 'bold'), width=17, bd=4,
                              command=iSave)
        self.btnSave.grid(row=0, column=6)

        # ==================================Dataaaaaaaaaaa===================================
        # ==================================Dataaaaaaaaaaa===================================
        # ================================ ==Dataaaaaaaaaaa===================================

        self.lbLabel = Label(FrameDetail, font=('arial', 9, 'bold'), pady=8,
                             text="Name \t\t ID \t\t Address \t\t Mail \t\t\t Phone \t\t\t Amount(m3) \t\t From \t\t To \t\t Price(VND/m3) \t\t Cost(VND)")
        self.lbLabel.grid(row=0, column=0)

        self.txtFrameDetail = Text(FrameDetail, font=('arial', 12, 'bold'), width=145, height=4, padx=2, pady=4)
        self.txtFrameDetail.grid(row=1, column=0)


if __name__ == '__main__':
    root1 = Tk()
    root1.resizable(0,0)
    application = water(root1)
    root1.mainloop()
