import time
import datetime
import random
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title = "Registration"
        self.root.geometry = ('600x500')
        self.root.configure(background = "black")


        Date_of_Registration =  StringVar()
        Date_of_Registration.set(time.strftime("%d/%n/%y"))

        Ref = StringVar()
        Mobile_no = StringVar()
        Pincode = StringVar()
        Address = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()

        # For combo box
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()  #for numerical values


        Membership = StringVar()
        Membership.set("0") #when membership checkbox is unlocked on reset has been done it will automatically set



        member_ref1b1 = Label(Manage_frame, text = "Refer ID", font = ("arial", 15, "bold"),bg = "#001a66", fg = "white")
        member_ref1b1.grid(row = 2, column = 0 , pady = 5 , padx = 10, sticky = "w")
        
        def exitbtt():
            exitbtt = tkinter.messagebox.askyesno("Member Registration","Are you sure you want to exit ?")
            if exitbtt > 0:
                root.destroy()
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Registration(self.newWindow)
                return
        
        def resetbtt():
            Firstname.set("")
            Ref.set("")
            Mobile_no.set("")
            Pincode.set("")
            Address.set("")
            Firstname.set("")
            Lastname.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            Membership.set("0")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt(state = DISABLED)

        def reeesetbtt():
            reeesetbtt = tkinter.messagebox.askokcancel("member Registration Form", "You want to add as new Record")
            if reeesetbtt > 0:
                resetbtt()
            elif reeesetbtt <= 0:
                resetbtt()
                detail_labeltxt.delete("1.0", END)
                return

        def Reference_number():
            ranumber = random.randint(10000,999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def membership_fees():
            if(var5.got() == 1):
                member_membershiptxt.config(state = NORMAL)
                item = float(15000)   #it is a random price of membership
                Membership.set(str(item)+ "Rs")
            elif(var5.get() == 0):
                member_membership.configure(state = DISABLED)
                Membership.set("0")
        
        def Receipt():
            Reference_number()
            detail_labeltxt.insert(END,"\t" +Date_of_Registration.get()+ " \t + Ref.get() + \t\t" + 
            Firstname.get()+ '\t' + Lastname.get() + "\t" + Pincode.get() + "\t" + Mobile_no.get() + " \t" + '\t\t' + 
            Address.get() + " \t\t" + Pincode.get() + "\t" + member_gendercmb.get() + "\t\t" + 
            Membership.get() + "\n")




        # Title
        self.title = Label(self.root, text="Member Registration Form", font = ("monotype corsiva", 30, "bold"),bd = 5,
            relief = GROOVE,bg = "#E6005C", fg="#000000")
        self.title.pack(side=TOP, fill = x)

        # member frame
        Manage_frame = Frame(self.root, bd = 4, relief = RIDGE, bd = "#001a66")
        Manage_frame.place(x=20, y=100, width=450, height = 630)

        detail_frame = Frame(self.root, relief= RIDGE,bg = "#001a66")
        detail_frame.place(x=500,y=100,width=820, height = 630)


        # Manage Frame
        Cus_title = Label(Manage_frame, "Customer Details", font = ("arial",20,"bold"), bg="#001a66",fg = "white")
        Cus_title.grid(row = 0, columnspan = 2, pady = 5)


        member_date1b1 = Label(Manage_frame,text = "Date",font = ("arial",15,"bold"),bg = "#001a66", fg="white")
        member_date1b1.grid(row = 1, column = 0, pady = 5, padx = 10, sticky = "w")

        member_datetext = Entry(Manage_frame, font = ("arial", 15, "bold"), textvariable = Date_of_Registration)
        member_datetext.grid(row = 1, column = 1, pady = 5, pady = 10 , sticky = "w")


        member_ref1b1 = Label(Manage_frame, text = "Reference ID", font = ("arial", 15, "bold"), bg = "#001Aa66", fg = "white")
        member_ref1b1.grid(row = 2, column = 0, pady = 5, padx = 10, sticky = "w")

        member_reftxt = Label(Manage_frame,font = ("arial",15,"bold"),textvariable = Ref)
        member_reftxt.grid(row = 2, column = 1, pady = 5, padx = 10, sticky = "w")


        member_frame1b1 = Label(Manage_frame,text = "First Name",font = ("arial",15,"bold"),bg = "#001a66", fg="white")
        member_frame1b1.grid(row = 3, column = 0, pady = 5, padx = 10, sticky = "w")

        member_fnametxt = Entry(Manage_frame, font = ("arial", 15, "bold"), textvariable = Firstname)
        member_fnametxt.grid(row = 3, column = 1, pady = 5, padx = 10 , sticky = "w")


        member_lname1b1 = Label(Manage_frame,text = "Last Name",font = ("arial",15,"bold"),bg = "#001a66", fg="white")
        member_lname1b1.grid(row = 4, column = 0, pady = 5, padx = 10, sticky = "w")

        member_lnametxt = Entry(Manage_frame, font = ("arial", 15, "bold"), textvariable = Lastname)
        member_lnametxt.grid(row = 4, column = 1, pady = 5, padx = 10 , sticky = "w")


        member_mobile1b1 = Label(Manage_frame,text = "Mobile No",font = ("arial",15,"bold"),bg = "#001a66", fg="white")
        member_mobile1b1.grid(row = 5, column = 0, pady = 5, padx = 10, sticky = "w")

        member_mobiletxt = Entry(Manage_frame, font = ("arial", 15, "bold"), textvariable = Mobile_no)
        member_mobiletxt.grid(row = 5, column = 1, pady = 5, padx = 10 , sticky = "w")


        member_address1b1 = Label(Manage_frame,text = "Address",font = ("arial",15,"bold"),bg = "#001a66", fg="white")
        member_address1b1.grid(row = 6, column = 0, pady = 5, padx = 10, sticky = "w")

        member_addresstxt = Entry(Manage_frame, font = ("arial", 15, "bold"), textvariable = Address)
        member_addresstxt.grid(row = 6, column = 1, pady = 5, padx = 10 , sticky = "w")

        
        member_pincode1b1 = Label(Manage_frame,text = "Pin Code",font = ("arial",15,"bold"),bg = "#001a66", fg="white")
        member_pincode1b1.grid(row = 7, column = 0, pady = 5, padx = 10, sticky = "w")

        member_pincodetxt = Entry(Manage_frame, font = ("arial", 15, "bold"), textvariable = Pincode)
        member_pincodetxt.grid(row = 7, column = 1, pady = 5, padx = 10 , sticky = "w")


        member_gender1b1 = Label(Manage_frame,text = "Pin Code",font = ("arial",15,"bold"),bg = "#001a66", fg="white")
        member_gender1b1.grid(row = 7, column = 0, pady = 5, padx = 10, sticky = "w")

        member_pincodetxt = Entry(Manage_frame, font = ("arial", 15, "bold"), textvariable = Pincode)
        member_pincodetxt.grid(row = 7, column = 1, pady = 5, padx = 10 , sticky = "w")

# 
        member_gendercmb = ttk.Combobox(Manage_frame, text = var4, state = "readonly", font = ("arial",15,"bold"),width = 19)
        member_gendercmb['values'] = ("", "Male", "Female", "Other")
        member_gendercmb.current(0)
        member_gendercmb.grid(row = 8, column = 1, pady = 5, padx = 10, sticky = "w")


        member_id_proof1b1 = Entry(Manage_frame, text = "ID Proof", font = ("arial", 15, "bold"), textvariable = Pincode)
        member_id_proof1b1.grid(row = 9, column = 1, pady = 5, padx = 10 , sticky = "w")


        member_id_proofcmb = ttk.Combobox(Manage_frame, text = var3, state = "readonly", font = ("arial",15,"bold"),width = 19)
        member_id_proofcmb['values'] = ("", "Medical Card", "Passport", "Driving License", "Pan Card", "Student ID")
        member_id_proofcmb.current(0)
        member_id_proofcmb.grid(row = 9, column = 1, pady = 5, padx = 10, sticky = "w")


        member_memtype1b1 = Entry(Manage_frame, text = "Member Type", font = ("arial", 15, "bold"), textvariable = Pincode)
        member_memtype1b1.grid(row = 10, column = 1, pady = 5, padx = 10 , sticky = "w")


        member_memtypecmb = ttk.Combobox(Manage_frame, text = var2, state = "readonly", font = ("arial",15,"bold"),width = 19)
        member_memtypecmb['values'] = ("", "Medical Card", "Insurance", "Pay immediately", "Pay when leaving")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row = 10, column = 1, pady = 5, padx = 10, sticky = "w")

        member_paymentwith1b1 = Entry(Manage_frame, text = "Member Type", font = ("arial", 15, "bold"), textvariable = Pincode)
        member_paymentwith1b1.grid(row = 11, column = 1, pady = 5, padx = 10 , sticky = "w")


        member_paymentwithcmb = ttk.Combobox(Manage_frame, text = var1, state = "readonly", font = ("arial",15,"bold"),width = 19)
        member_paymentwithcmb['values'] = ("", "Cash", "Debit Card - RuPay", "Debit Card - visa", "Debit Card - Mastercard", "Credit Card", "Googlepay")
        member_paymentwithcmb.current(0)
        member_paymentwithcmb.grid(row = 11, column = 1, pady = 5, padx = 10, sticky = "w")


        member_membership = Checkbutton(Manage_frame, text = "Membership Fees", variable = var5, onvalue = 1, offvalue = 0, font = ("arial", 15, "bold"),bg = "#001a66", fg = "white", command = membership_fees)
        member_membership.grid(row = 12,column = 0, sticky = "w")
        member_membershiptxt = Entry(Manage_frame, font = ("arial", 15, "bold"), state = DISABLED, justify = RIGHT, textvariable = Membership)
        member_membershiptxt.grid(row = 12, column = 1, pady = 5, padx = 10 , sticky = "w")

        detail_frame = Frame(self.root, relief = RIDGE, bg = "#001a66")
        detail_frame.place(x=500, y=100, width = 820, height = 630)

        detail_label = Label(detail_frame, font = ("arial", 11, "bold"),pady = 10,padx = 2, width = 95, text = "Date\t REf id\t Firstname Lastname Mobile No Address Pincode Gender Membership")
        detail_label.grid(row = 0, column = 0, columnspan = 4, sticky = "w")
        detail_labeltxt = Text(detail_frame, width = 123, height = 34, font = ("arial", 10))
        detail_labeltxt.grid(row = 1, column=0, columnspan=4)

        # we will add button
        receiptbtn = Button(detail_frame, padx = 15, bd = 5, font = ("arial",12,"bold"), bg = "#ff9966", width = 20, text = "Receipt", command = Receipt)
        receiptbtn.grid(row = 2, column = 0)

        resetbtn = Button(detail_frame, padx = 15, bd = 5, font = ("arial",12,"bold"), bg = "#ff9966", width = 20, text = "Reset", command = reeesetbtt)
        resetbtn.grid(row = 2, column = 1)

        exittbtn = Button(detail_frame, padx = 15, bd = 5, font = ("arial",12,"bold"), bg = "#ff9966", width = 20, text = "Exit", command = exitbtt)
        exittbtn.grid(row = 2, column = 2)




if __name__ == "__main__":
    root = Tk()
    app = Registration()
    root.mainloop()