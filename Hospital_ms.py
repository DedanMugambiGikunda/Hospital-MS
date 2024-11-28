import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


def main():
    root = Tk()
    app = window1(root)
    root.mainloop()

class window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()


        self.LabelTitle = Label(self.frame, text = "Hospital Management System", font=("arial",40,"bold"),
                bd=10,relief= "sunken")
        self.LabelTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)


        # The 3 big frames
        self.loginframe1 = Frame(self.frame, width = 1000, height = 300, bd = 10, relief = "groove")
        self.loginframe1.grid(row=1 , column=0)

        self.loginframe2 = Frame(self.frame, width = 1000, height = 100, bd = 10, relief = "groove")
        self.loginframe2.grid(row=2 , column=0, pady = 15)

        self.loginframe3 = Frame(self.frame, width = 1000, height = 200, bd = 10, relief = "groove")
        self.loginframe3.grid(row=6 , column=0, pady = 5)


    
        # Buttons in frame3
        self.button_reg = Button(self.Loginframe3,text = "Patient Registration Window",state = DISABLED, font = ("arial",15,"bold"),command = self.Registration_window)
        self.button_reg.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.button_Hosp = Button(self.Loginframe3,text = "Hospital Management Window",state = DISABLED, font = ("arial",15,"bold"),command = self.Hospital_window)
        self.button_Hosp.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.button_Dr_appt = Button(self.Loginframe3,text = "Doctor Management Window",state = DISABLED, font = ("arial",15,"bold"),command = self.Dr_Appoint_window)
        self.button_Dr_appt.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.button_med_stock = Button(self.Loginframe3,text = "Medicine Stock Window",state = DISABLED, font = ("arial",15,"bold"),command = self.Medicine_stock)
        self.button_reg.grid(row = -1, column = 0, padx = 10, pady = 10)


        # Username and password in frame1
        self.LabelUsername = Label(self.Loginframe1, text="User Name", font=("arial", 20, "bold"),bd=3)
        self.LabelUsername.grid(row = 0,column = 0)

        self.textUsername = Entry(self.loginframe1,font = ("arial",20,"bold"), bd=3 ,textvarible=self.Username)
        self.textUsername.grid(row=0,column=1,padx=40,pady= 15)

        self.LabelPassword = Label(self.Loginframe1, text="Password", font=("arial", 20, "bold"),bd=3)
        self.LabelPassword.grid(row = 1,column = 0)

        self.textUsername = Entry(self.loginframe1,font = ("arial",20,"bold"),show="*", bd=3 ,textvarible=self.Username)
        self.textUsername.grid(row=1,column=1,padx=40,pady= 15)


        # login,reset and exit buttons in frame2
        self.button_Login = Button(self.loginframe2,Width = 20, text="Login", font=("arial", 18, "bold"),command=self.login_system)
        self.button_Login.grid(row = 0, column=0, padx=10, pady=10)

        self.button_Reset = Button(self.loginframe2, width="", text="Reset", font=("arial", 18, "bold"),command=self.reset_btn)
        self.button_Reset.grid(row = 0, column=3, padx=10, pady=10)

        self.button_Exit = Button(self.loginframe2, width="",text="Exit", font=("arial", 18, "bold"),command=self.Exit_btn)
        self.button_Exit.grid(row = 0, column=6, padx=10, pady=10)

    
    def login_system(self):
        user = self.Username.get()
        pswd = self.Password.get()

        if(user == str("admin") and (pswd == str("admin"))):
            self.button_reg.config(state = NORMAL)
            self.button_Hosp.config(state = NORMAL)
            self.button_Dr_appt.config(state = NORMAL)
            self.button_med_stock(state = NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System", "You have entered an invalid username or password")
            self.button_reg.config(state = DISABLED)
            self.button_Hosp.config(state = DISABLED)
            self.button_Dr_appt.config(state = DISABLED)
            self.button_med_stock(state = DISABLED)
        # if the username or password is incorrect then that will happen

            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()

    def reset_btn(self):
        self.button_reg.config(state = DISABLED)
        self.button_reg.config(state = DISABLED)
        self.button_reg.config(state = DISABLED)
        self.button_reg.config(state = DISABLED)
        # because when we will reset still we havent given correct user id and password
        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus

    def Exit_btn(self):
        self.Exit_btn = tkinter.messagebox.askyesno("Hospital Management System", "Are you sure you want to exit")
        if self.Exit_btn > 0:
            # We will close that master screen
            self.master.destroy()
            return
            
# Our Windows Defined
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)

    def Pharmacy(self):
        self.newWindow = Toplevel(self.master)
        self.app = Pharmacy(self.newWindow)

    def Dr_Appoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = doctor(self.newWindow)

    def Medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = window5(self.newWindow)




# class Pharmacy start

class Pharmacy():
    def __init__(self,root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background = "black")

        # Variable Declaration
        Date_of_Registation = StringVar()
        Date_of_Registation.set(time.strftime("%d/%n?/%y"))

        Ref = StringVar()
        cmbTabletNames = StringVar
        HospitalCode = StringVar()
        Number_of_Tablets = StringVar()
        lot = StringVar()
        IssuedDate = StringVar()
        EntryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInformation = StringVar()
        StorageAdvice = StringVar()
        Medication = StringVar()
        PatientId = StringVar()
        PatientNHnumber = StringVar()
        Patientname = StringVar()
        Dateofbirth = StringVar()
        Prescription = StringVar()
        NHSnumber = StringVar()
        Expirydate = StringVar()
        


        def Reference_numfunc():
            renumber = random.randint(10000,999999)
            randomnumber = str(ranumber)
            Ref.sat(randomnumber)


        def prescriptionfunc():
            Reference_numfunc()
            TextPrescription.insert(END, "Patient ID: \t\t" + PatientId.get()+ "\n")
            TextPrescription.insert(END, "Patient Name: \t\t" + Patientname.get()+ "\n")
            TextPrescription.insert(END, "Tablet: \t\t" + cmbTabletNames.get()+ "\n")
            TextPrescription.insert(END, "Number of tablets: \t\t" + Number_of_Tablets.get()+ "\n")
            TextPrescription.insert(END, "Daily Dose: \t\t" + DailyDose.get()+ "\n")
            TextPrescription.insert(END, "Issued Date: \t\t" + IssuedDate.get()+ "\n")
            TextPrescription.insert(END, "Expiry Date: \t\t" + ExpiryDate.get()+ "\n")
            TextPrescription.insert(END, "Storage: \t\t" + StorageAdvice.get()+ "\n")
            TextPrescription.insert(END, "More information: \t\t" + MoreInformation.get()+ "\n")




        def prescriptiondatafunc():
            Reference_numfunc()
            TextPrescriptionData.insert(END,Data_of_Registration.get()+"\t"+Ref.get()+"\t\t"
            +Patientname.get()+"\t\t"+ Dateofbirth.get()+"\t\t"+Dateofbirth.get()+"\t\t"+NHSnumber.get()+"\t\t"+cmbTabletNames.get()+"\t"
            Number_of_Tablets.get()+ "\t\t" + "IssuedDate.get()+\t\t" + ExpiryDate.get() + "\t\t" + DailyDose.get()+"\t\t"+StorageAdvice.get() + "\t\t" + PatientId.get()+ "\n")
            return

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Pharmacy", "Are you sure you want to exit ?")
            if exitbtn > 0:
                root.destroy()
                return

        
        def deletefunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            lot.set("")
            IssuedDate.set("")
            EntryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumber.set("")
            Patientname.set("")
            Dateofbirth.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0", END)
            TextPrescriptionData.delete("1.0", END)
            return
        

        def resetfunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            lot.set("")
            IssuedDate.set("")
            EntryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumber.set("")
            Patientname.set("")
            Dateofbirth.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0", END)
            return

        def Prescription():


    
     # Title
        Title = Label(self.root,text = "Pharmacy", font = ("Monotypes corvina", 42, "bold"),bd = 5, relief = GROOVE,bg = "#2eb8b8", fg = "black")
        Title.pack(side = TOP, fill = X)

     # Frames       
        Manage_Frame = Frame(self.root,width = 1518, height = 400, bd = 5, relief = RIDGE, bg = "#0099cc")
        Manage_Frame.place(x=10, y=80)

        Button_Frame = Frame(self.root, width= 1510, Height = 55, bd = 4,bd = 4, relief = RIDGE ,bg = "#328695")
        Button_Frame.place(x=10, y = 460)

        Data_Frame = LabelFrame(self.root, width= 1510, height = 270, bd = 4, relief = RIDGE , bg = "#266e73")
        Data_Frame.Place(x=10, y=510)

    
    # Inner frame
        Data_FrameLeft = LabelFrame(Manage_Frame,width = 1050, text = "General Information", font = ("arial", 20, "italic bold"), height = 399, bd = 7, relief= RIDGE, bg = "#0099cc")
        Data_FrameLeft.pack(side = LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame,width = 1050, text = "Prescription", font = ("arial", 15, "italic bold"), height = 399, bd = 7, relief= RIDGE, bg = "#0099cc")
        Data_FrameRight.Pack(side = RIGHT)

        Data_Framedata =  LabelFrame(Data_Frame, width = 1050, text = "Prescription Data", font = ("arial", 12, "italic bold"), height = 390, bd = 4, relief= RIDGE, bg = "#3eb7bb")
        Data_Framedata.pack(side = LEFT)


    # LABELS
        Date1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Date", padx = 2, bg = "#0099cc")
        Date1b1.grid(row = 0, column= 0, padx= 10, pady = 5, sticky = W)

        Datetxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = Date_of_Registation)
        Datetxt.grid(row = 0,column= 1, padx = 10, pady = 5, sticky= E)


    # Ref
        Ref1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Reference Number", padx = 2, bg = "#0099cc")
        Ref1b1.grid(row = 0, column= 0, padx= 10, pady = 5, sticky = W)
        Reftxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, state = DISABLED, textvariable = Ref)
        Reftxt.grid(row = 0,column= 1, padx = 10, pady = 5, sticky= E)

    
    # Patient ID
        PatientId1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Patient Id", padx = 2, bg = "#0099cc")
        PatientId1b1.grid(row = 2, column= 0, padx= 10, pady = 5, sticky = W)

        PatientIdtxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = Ref)
        PatientIdtxt.grid(row = 2,column= 1, padx = 10, pady = 5, sticky= E)

    # Patient ID
        PatientName1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Patient Name", padx = 2, bg = "#0099cc")
        PatientName1b1.grid(row = 3, column= 0, padx= 10, pady = 5, sticky = W)

        PatientNametxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = Ref)
        PatientNametxt.grid(row = 3,column= 1, padx = 10, pady = 5, sticky= E)

    # Date of Birth
        Dateofbirthb1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Date of Birth", padx = 2, bg = "#0099cc")
        Dateofbirthb1.grid(row = 4, column= 0, padx= 10, pady = 5, sticky = W)

        Dateofbirthtxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = Ref)
        Dateofbirthtxt.grid(row = 4,column= 1, padx = 10, pady = 5, sticky= E)

    # Address
        Address1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Address", padx = 2, bg = "#0099cc")
        Address1b1.grid(row = 5, column= 0, padx= 10, pady = 5, sticky = W)

        Addresstxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = Ref)
        Addresstxt.grid(row = 5,column= 1, padx = 10, pady = 5, sticky= E)

    # NHS number
        NHSnumber1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "NHS unique number", padx = 2, bg = "#0099cc")
        NHSnumber1b1.grid(row = 6, column= 0, padx= 10, pady = 5, sticky = W)

        NHSnumbertxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = Ref)
        NHSnumbertxt.grid(row = 6,column= 1, padx = 10, pady = 5, sticky= E)

    # Tablet name
        Tablet1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Address", padx = 2, bg = "#0099cc")
        Tablet1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Address", padx = 2, bg = "#0099cc")
        
        Tabletcmb = ttk.Combobox(Data_FrameLeft, textvariable= cmbTabletNames , width= 25, state = "readonly", font = ("arial", 12, "bold"))
        Tabletcmb['values'] = ("", "Paracetamol", "Can-p", "Dio-1 One", "Ca1pol", "Amlodipine Besylate", "Nexium", "Singulair", "Plavix", "Amoxicillian", "Azithromycin", "Limcin-900")

        Tabletcmb.current(0)
        Tabletcmb.grid(row = 7, column = 1, padx = 10, pady = 5)

    # No of tablets to take
        No_of_Tablets1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Number of Tablets", padx = 2, bg = "#0099cc")
        No_of_Tablets1b1.grid(row = 8, column= 0, padx= 10, pady = 5, sticky = W)

        No_of_Tabletstxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = Number_of_Tablets)
        No_of_Tabletstxt.grid(row = 8,column= 1, padx = 10, pady = 5, sticky= E)
    

    # Second Column of other details
        HospitalCode1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Number of Tablets", padx = 2, bg = "#0099cc")
        HospitalCode1b1.grid(row = 0, column= 2, padx= 10, pady = 5, sticky = W)

        HospitalCode1b1 = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = Number_of_Tablets)
        HospitalCode1b1.grid(row = 0,column = 3, padx = 10, pady = 5, sticky= E)


    # Storage

        StorageAdvice1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 23, text= "Storage Advice", padx = 2, bg = "#0099cc")
        StorageAdvice1b1.grid(row = 1, column= 2, padx= 10, pady = 5, sticky = W)

        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft, textvariable = StorageAdvice , width= 25, state = "readonly", font = ("arial", 12, "bold"))
        StorageAdvicecmb['values'] = ("", "Under room temp", "below 5*C", "Below 0*C", "Refrigerator")
        StorageAdvicecmb.current(0)
        StorageAdvicecmb.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = E)


    # Lot number of medication
        Lot_no1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Lot number", padx = 2, bg = "#0099cc")
        Lot_no1b1.grid(row = 2, column= 2, padx= 10, pady = 5, sticky = W)

        Lot_notxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = lot)
        Lot_notxt.grid(row = 2,column = 3, padx = 10, pady = 5, sticky= E)


    # Issued Date
        IssuedDate1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Date of Issue", padx = 2, bg = "#0099cc")
        IssuedDate1b1.grid(row = 2, column= 2, padx= 10, pady = 5, sticky = W)

        IssuedDatetxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = IssuedDate)
        IssuedDatetxt.grid(row = 2,column = 3, padx = 10, pady = 5, sticky= E)


    # Expiry Date
        ExpiryDate1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Date of Expiry", padx = 2, bg = "#0099cc")
        ExpiryDate1b1.grid(row = 4, column= 2, padx= 10, pady = 5, sticky = W)

        ExpiryDatetxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = Expirydate)
        ExpiryDatetxt.grid(row = 4,column = 3, padx = 10, pady = 5, sticky= E)
        

    # Daily Dose
        DailyDose1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Daily Dose", padx = 2, bg = "#0099cc")
        DailyDose1b1 .grid(row = 5, column= 2, padx= 10, pady = 5, sticky = W)

        DailyDose1b1  = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = DailyDose)
        DailyDose1b1.grid(row = 5,column = 3, padx = 10, pady = 5, sticky= E)


    # Side Effects
        SideEffects1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width = 20, text= "Side Effects", bg = "#0099cc")
        SideEffects1b1.grid(row = 6, column= 2, padx= 10, pady = 5, sticky = W)

        SideEffectstxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = DailyDose)
        SideEffectstxt.grid(row = 6,column = 3, padx = 10, pady = 5, sticky= E)


    # More info
        MoreInformation1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width = 20, text= "More Information", bg = "#0099cc")
        MoreInformation1b1.grid(row = 7, column= 2, padx= 10, pady = 5, sticky = W)

        MoreInformationtxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = MoreInformation)
        MoreInformationtxt.grid(row = 7,column = 3, padx = 10, pady = 5, sticky= E)

    # Medication(Yes/no)
        Medication1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width = 20, text= "Medication", bg = "#0099cc")
        Medication1b1.grid(row = 7, column= 2, padx= 10, pady = 5, sticky = W)

        Medicationtxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = Medication)
        Medicationtxt.grid(row = 7,column = 3, padx = 10, pady = 5, sticky= E)

    # Text field for Prescription
        TestPrescription = Text(Data_Framedata, font = ("arial",12,"bold"), width = 55, height = 17, padx = 3, pady =5)
        TestPrescription.grid(row = 0, column = 0)

    # Text for prescription Data
        TestPrescriptionData = Text(Data_Framedata, font = ("arial",12,"bold"), width = 203, height = 12, padx = 3, pady =5)
        TestPrescriptionData.grid(row = 1, column = 0)



    # We will add button to our middle frame
        Prescription = Button(Button_Frame = "Prescription", bg = "#ffaab0", activebackground = "#fcceb2", font = ("arial", 15, "bold"),width=22, command = prescriptionfunc)
        Prescription.grid(row = 0, column = 0, padx = 15)

        Receiptbtn = Button(Button_Frame = "Prescription Data", bg = "#ffaab0", activebackground = "#fcceb2", font = ("arial", 15, "bold"),width=22, command = prescriptiondatafunc)
        Receiptbtn.grid(row = 0, column = 1, padx = 15)

        Resetbtn = Button(Button_Frame = "Reset", bg = "#ffaab0", activebackground = "#fcceb2", font = ("arial", 15, "bold"),width=22, command= resetfunc)
        Resetbtn.grid(row = 0, column = 2, padx = 15)

        Deletebtn = Button(Button_Frame = "Delete", bg = "#ffaab0", activebackground = "#fcceb2", font = ("arial", 15, "bold"),width=22 , command = deletefunc)
        Deletebtn.grid(row = 0, column = 3, padx = 15)

        Exitbtn = Button(Button_Frame = "Exit", bg = "#ffaab0", activebackground = "#fcceb2", font = ("arial", 15, "bold"),width=22 , command = exitbtn)
        Exitbtn.grid(row = 0, column = 4, padx = 15)

        Prescriptiondatarow = Label(Data_Framedata, bg = "White", font=("arial",12, "bold"), text = "Date\tReference id\Patient Name\tDate of Birth\NHS Number\tTablet\tNo of Tablet\tIssued Date\tExpiry Date\tDaily Dose\tStorage Advice")
        Prescriptiondatarow.grid(row = 0, column = 0, sticky= W)
        
# class Pharmacy Ends


# Class Doctor Starts
class doctor():
    def __init__(self,root):
        self.root = root
        self.root.title("Doctor Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background = "black")
        

        # Declarationof all functions
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%n/%y"))
        DrId = StringVar()
        Drname = StringVar
        DateofBirth = StringVar()
        Spes = StringVar()
        GovtPri = StringVar()
        Surgeries = StringVar()
        Experieces = StringVar()
        Nurseries = StringVar()
        DrMobile = StringVar()
        PtName = StringVar()
        Appline = StringVar()
        PtAge = StringVar()
        PatientAddress = StringVar()
        PtMobile = StringVar()
        Disease = StringVar()
        caseBenefitCard = StringVar()
        Apptime = StringVar()
        case = StringVar()
        Benefitcard = StringVar()


        # commands for buttons
        def exitbtn():
            tkinter.messagebox.askyesno("Doctor Management System","Are you sure you want to exit?")
            if exitbtn > 0:
                root.destroy()
            return

        def resetfunc():
            DrId.set("")
            Drname.set("")
            DateofBirth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experieces.set("")
            Nurseries.set("")
            DrMobile.set("")
            PtName.set("")
            Appline.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            caseBenefitCard.set("")
            Apptime.set("")
            case.set("")
            Benefitcard.set("")
            return

        def deletefunc():
            DrId.set("")
            Drname.set("")
            DateofBirth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experieces.set("")
            Nurseries.set("")
            DrMobile.set("")
            PtName.set("")
            Appline.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            caseBenefitCard.set("")
            Apptime.set("")
            case.set("")
            Benefitcard.set("")
            TextPrescription.delete("1.0",END)
            return
        
        def Patient_idFunc():
            ranumber = random.randint(10000,999999)
            randomnumber = str(ranumber)
            DrId.set(randomnumber)

        def prescriptiondatafunc():
            Patient_idFunc()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+DrId.get()+"\t"+Drname.get()+"\t\t"+DateofBirth.get()+"\t\t"+
            Spes.get()+ "\t\t"+GovtPri.get()+"\t\t"+PtName.get()+"\t\t"+case.get()+"\t"+PtAge.get()+"\n")
            return

        def prescriptionfunc():
            Patient_idFunc()
            TextPrescription.insert(END, "Date: \t\t"+Date_of_Registration.get()+"\n")
            TextPrescription.insert(END, "Patient Name: \t\t"+Date_of_Registration.get()+"\n")
            TextPrescription.insert(END, "Appintment Time"+Apptime.get()+"\n")
            TextPrescription.insert(END, "Age"+PtAge.get()+ "\n")
            TextPrescription.insert(END, "Address"+ PatientAddress.get()+"\n")
            TextPrescription.insert(END, "Disease"+Disease.get()+"\n")
            TextPrescription.insert(END, "Case"+case.get()+"\n")
            TextPrescription.insert(END, "Benefit Card"+Benefitcard.get()+"\n")
            TextPrescription.insert(END, "To meet Dr"+Drname.get()+"\n")
            TextPrescription.insert(END, "Dr. Mobile No"+DrMobile.get()+"\n")
            return


        # Title
        title = Label(self.root, text = "Doctor Management System", font=("monotype corsiva", 42,"bold"),bd = 5, relief=GROOVE, bd = "#b7d8d5", fg = "black")
        title.pack(side = TOP, fill = X, expand= True)

        # Frames
        Manage_Frame = Frame(self.root, width = 1510, height = 400, bd = 5, relief = RIDGE, bg = "#789e9e")
        Manage_Frame.place(x=10, y=80)

        Button_Frame = Frame(self.root, width = 1510, height = 55, bd = 4, relief= RIDGE , bg = "#eef3db")
        Button_Frame.place(x=10, y= 460)
        
        Data_Frame = Frame(self.root, width = 1510, height = 270, bd = 4, relief = RIDGE, bg = "#eef3db")
        Data_Frame.place(x=10,y=510)

        Data_FrameLeft = LabelFrame(Manage_Frame, width = 1050, text = "General Information", font=("arial", 20,"italic bold"), height = 390, bd = 7, pady = 1, relief = RIDGE, bg = "#789e9e")
        Data_FrameLeft.pack(side = LEFT)

        Data_Framedata = LabelFrame(Manage_Frame, width = 1050, text = "Doctor's Details", font=("arial", 20,"italic bold"), height = 390, bd = 7, relief = RIDGE, bg = "#789e9e")
        Data_Framedata.pack(side = LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame, width = 1050, text = "Patient's Information", font=("arial", 20,"italic bold"), height = 390, bd = 7, relief = RIDGE, bg = "#789e9e")
        Data_FrameRight.pack(side = LEFT)

        # Doctor's ID
        Dr1b1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Doctor ID", bg = "#789e9e")
        Dr1b1b1.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)
        DrIdtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27, state = DISABLED, textvariable = DrId)
        DrIdtxt.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)


        DrName1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Doctor ID", bg = "#789e9e")
        DrName1b1.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)
        DrNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27, state = DISABLED, textvariable = Drname)
        DrNametxt.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = E)


        Dateofbirth1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Date of birth", bg = "#789e9e")
        Dateofbirth1b1.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)
        Dateofbirth1b1 = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27, state = DISABLED, textvariable = DateofBirth)
        Dateofbirth1b1.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)


        Spes1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Specialisation", bg = "#789e9e")
        Spes1b1.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)
        Spestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27, state = DISABLED, textvariable = DrId)
        Spestxt.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

        
        GovtPri1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Govt/Private", bg = "#789e9e")
        GovtPri1b1.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = W)
        GovtPricmb = ttk.Combobox(Data_FrameLeft, textvariable= GovtPri , width= 25, state = "readonly", font=("arial", 12,"bold"))
        GovtPricmb['values'] = ("", "Govrtnment", "Private")
        GovtPricmb.current(0)
        GovtPricmb.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = E)
        

        Surgeries1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Surgeries", bg = "#789e9e")
        Surgeries1b1.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = W)
        Surgeriestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27,textvariable = Surgeries)
        Surgeriestxt.grid(row = 5, column = 1, padx = 10, pady = 5, sticky = E)


        Experience1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Surgeries", bg = "#789e9e")
        Experience1b1.grid(row = 6, column = 0, padx = 10, pady = 5, sticky = W)
        Experiencetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27,textvariable = Experieces)
        Experiencetxt.grid(row = 6, column = 1, padx = 10, pady = 5, sticky = E)
        

        Nurses1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Surgeries", bg = "#789e9e")
        Nurses1b1.grid(row = 7, column = 0, padx = 10, pady = 5, sticky = W)
        Nursestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27,textvariable = Experieces)
        Nursestxt.grid(row = 7, column = 1, padx = 10, pady = 5, sticky = E)
        

        DrMobile1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Doctor MObile No", bg = "#789e9e")
        DrMobile1b1.grid(row = 7, column = 0, padx = 10, pady = 5, sticky = W)
        DrMobiletxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27,textvariable = DrMobile)
        DrMobiletxt.grid(row = 7, column = 1, padx = 10, pady = 5, sticky = E)

        
        Date1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Doctor MObile No", bg = "#789e9e")
        Date1b1.grid(row = 7, column = 0, padx = 10, pady = 5, sticky = W)
        Datetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27,textvariable = Date_of_Registration)
        Datetxt.grid(row = 7, column = 1, padx = 10, pady = 5, sticky = E)


        PtName1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Doctor MObile No", bg = "#789e9e")
        PtName1b1.grid(row = 7, column = 0, padx = 10, pady = 5, sticky = W)
        PtNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27,textvariable = PtName)
        PtNametxt.grid(row = 7, column = 1, padx = 10, pady = 5, sticky = E)


        Apptime1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Appointment Time", bg = "#789e9e")
        Apptime1b1.grid(row = 7, column = 0, padx = 10, pady = 5, sticky = W)
        Apptimetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27,textvariable = Apptime)
        Apptimetxt.grid(row = 7, column = 1, padx = 10, pady = 5, sticky = E)


        PtAge1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Patient Age", bg = "#789e9e")
        PtAge1b1.grid(row = 7, column = 0, padx = 10, pady = 5, sticky = W)
        PtAge1b1txt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27,textvariable = PtAge)
        PtAge1b1txt.grid(row = 7, column = 1, padx = 10, pady = 5, sticky = E)


        PtAddress1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Patient Address", bg = "#789e9e")
        PtAddress1b1.grid(row = 5, column = 3, padx = 10, pady = 5, sticky = W)
        PtAddresstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27,textvariable = PatientAddress)
        PtAddresstxt.grid(row = 6, column = 3, padx = 10, pady = 5, sticky = E)


        PtMobile1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Patient Mobile No", bg = "#789e9e")
        PtMobile1b1.grid(row = 5, column = 2, padx = 10, pady = 5, sticky = W)
        PtMobiletxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27,textvariable = PtMobile)
        PtMobiletxt.grid(row = 5, column = 3, padx = 10, pady = 5, sticky = E)


        Disease1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Patient Disease", bg = "#789e9e")
        Disease1b1.grid(row = 6, column = 2, padx = 10, pady = 5, sticky = W)
        Diseasetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width = 27,textvariable = Disease)
        Diseasetxt.grid(row = 6, column = 3, padx = 10, pady = 5, sticky = E)


        Case1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Case", padx = 2)
        Case1b1.grid(row = 7, column = 2, padx = 10, pady = 5, sticky = W)
        casecmb = ttk.Combobox(Data_FrameLeft, textvariable = case , width = 25 ,state = "readonly", font = ("arial", 12, "bold"))
        casecmb['values'] = ("", "New Case", "Old Case")
        casecmb.current(0)
        casecmb.grid(row = 7, column = 3, padx = 10, pady = 5, sticky = E)


        BenefitCard1b1 = Label(Data_Frame, font=("arial", 12, "bold"), width = 20, text = "Patient Disease", bg = "#789e9e")
        BenefitCard1b1.grid(row = 8, column = 2, padx = 10, pady = 5, sticky = W)
        BenefitCardcmb = ttk.Combobox(Data_FrameLeft, textvariable = Benefitcard , width = 25 ,state = "readonly", font = ("arial", 12, "bold"))
        BenefitCardcmb['values'] = ("", "Ayushman Card", "Health", "Senior Citizen", "Army Card")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row = 8, column = 3, padx = 10, sticky = E)


        # TextPresctriprion
        TextPrescription = Text(Data_FrameRight, font=("arial",12,"bold"),width = 55,height=17,padx =3, pady = 5)
        TextPrescription.grid(row= 0, column = 0)
        TextPrescription = Text(Data_Framedata, font =("arial",12,"bold"),width = 203, height=12, padx =3, pady = 5)
        TextPrescription.grid(row = 1, column = 0)

        
        # Buttons
        Prescriptionbtn = Button(Button_Frame, text = "Patient information", bg = "#fe615a", activebackground = "#cc6686", font = ("arial", 15, "bold"), Width = 22, command = prescriptionfunc)
        Prescriptionbtn.grid(row = 0, column = 0, padx = 15)

        DoctorDetailbtn = Button(Button_Frame, text = "Doctor's Details", bg = "#fe615a", activebackground = "#cc6686", font = ("arial", 15, "bold"), Width = 22, command = prescriptiondatafunc)
        DoctorDetailbtn.grid(row = 0, column = 1, padx = 15)

        Resetbtn = Button(Button_Frame, text = "Reset", bg = "#fe615a", activebackground = "#cc6686", font = ("arial", 15, "bold"), Width = 22, command = resetfunc)
        Resetbtn.grid(row = 0, column = 2, padx = 15)

        Deletebtn = Button(Button_Frame, text = "Delete", bg = "#fe615a", activebackground = "#cc6686", font = ("arial", 15, "bold"), Width = 22 , command = deletefunc)
        Deletebtn.grid(row = 0, column = 3, padx = 15)

        Exitbtn = Button(Button_Frame, text = "Exit", bg = "#fe615a", activebackground = "#cc6686", font = ("arial", 15, "bold"), Width = 22 ,command = exitbtn)
        Exitbtn.grid(row = 0, column = 4, padx = 15)

        Prescriptiondatarow = Label(Data_Framedata, bg = "white", font = ("arial", 12, "bold"), text = "Date\tDoctor Name\tDate of Birth\tSpecialisation\tGovt/Private\tSurgeries\tExperience\tNurses\tDr Mobile No\tPateintName\tCase\tPt.Age")

# Class Doctor Ends

        
if __name__ == "__main__":
    root = Tk()
    app = doctor(root)
    root.mainloop()

class window5:
    def __init__(self,master):
        self.master = master
        self.master.title("Medicine System")
        self.master.geomotry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == "__main__":
    main()