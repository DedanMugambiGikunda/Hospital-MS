import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Hospital():
    def __init__(self,root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background = "black")

        # Variable Declaration
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%n?/%y"))

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
        PatientAddress = StringVar()
        Dateofbirth = StringVar()
        Prescription = StringVar()
        NHSnumber = StringVar()
        ExpiryDate = StringVar()
        TextPrescription = StringVar()
        TextPrescriptionData = StringVar()
        


        def Reference_numfunc():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)


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
            TextPrescriptionData.insert(END, Date_of_Registration.get()+"\t"+Ref.get()+"\t\t")
            +Patientname.get()+"\t\t"+ Dateofbirth.get()+"\t\t"+Dateofbirth.get()+"\t\t"+NHSnumber.get()+"\t\t"+cmbTabletNames.get()+"\t"
            Number_of_Tablets.get()+ "\t\t" + "IssuedDate.get()+\t\t" + ExpiryDate.get() + "\t\t" + DailyDose.get()+"\t\t"+StorageAdvice.get() + "\t\t" + PatientId.get()+ "\n")
            return

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Pharmacy Management System", "Are you sure you want to exit ?")
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
            TextPrescription.set("1.0", END)
            return

        def Prescription():

  
    
     # Title
        Title = Label(self.root,text = "Pharmacy Management System", font = ("Monotypes corvina", 42, "bold"),bd = 5, relief = GROOVE,bg = "#2eb8b8", fg = "black")
        Title.pack(side = TOP, fill = X)

     # Frames       
        Manage_Frame = Frame(self.root,width = 1518, height = 400, bd = 5, relief = RIDGE, bg = "#0099cc")
        Manage_Frame.place(x=10, y=80)

        Button_Frame = Frame(self.root, width= 1510, Height = 55, bd = 4,bd = 4, relief = RIDGE ,bg = "#328695")
        Button_Frame.place(x=10, y = 460)

        Data_Frame = LabelFrame(self.root, width= 1510, height = 270, bd = 4, relief = RIDGE , bg = "#266e73")
        Data_Frame.place(x=10, y=510)

    
    # Inner frame
        Data_FrameLeft = LabelFrame(Manage_Frame,width = 1050, text = "General Information", font = ("arial", 20, "italic bold"), height = 399, bd = 7, relief= RIDGE, bg = "#0099cc")
        Data_FrameLeft.pack(side = LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame,width = 1050, text = "Prescription", font = ("arial", 15, "italic bold"), height = 399, bd = 7, relief= RIDGE, bg = "#0099cc")
        Data_FrameRight.pack(side = RIGHT)

        Data_Framedata =  LabelFrame(Data_Frame, width = 1050, text = "Prescription Data", font = ("arial", 12, "italic bold"), height = 390, bd = 4, relief= RIDGE, bg = "#3eb7bb")
        Data_Framedata.pack(side = LEFT)


    # LABELS
    # Date
        Date1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Date", padx = 2, bg = "#0099cc")
        Date1b1.grid(row = 0, column= 0, padx= 10, pady = 5, sticky = W)

        Datetxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = Date_of_Registration)
        Datetxt.grid(row = 0,column= 1, padx = 10, pady = 5, sticky= E)


    # Ref
        Ref1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Reference Number", padx = 2, bg = "#0099cc")
        Ref1b1.grid(row = 1, column= 0, padx= 10, pady = 5, sticky = W)

        Reftxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, state = DISABLED, textvariable = Ref)
        Reftxt.grid(row = 1,column= 1, padx = 10, pady = 5, sticky= E)

    
    # Patient ID
        PatientId1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Patient Id", padx = 2, bg = "#0099cc")
        PatientId1b1.grid(row = 2, column= 0, padx= 10, pady = 5, sticky = W)

        PatientIdtxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = PatientId)
        PatientIdtxt.grid(row = 2,column= 1, padx = 10, pady = 5, sticky= E)

    # Patient ID
        PatientName1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Patient Name", padx = 2, bg = "#0099cc")
        PatientName1b1.grid(row = 3, column= 0, padx= 10, pady = 5, sticky = W)

        PatientNametxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = Patientname)
        PatientNametxt.grid(row = 3,column= 1, padx = 10, pady = 5, sticky= E)

    # Date of Birth
        Dateofbirthb1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Date of Birth", padx = 2, bg = "#0099cc")
        Dateofbirthb1.grid(row = 4, column= 0, padx= 10, pady = 5, sticky = W)

        Dateofbirthtxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = Dateofbirth)
        Dateofbirthtxt.grid(row = 4,column= 1, padx = 10, pady = 5, sticky= E)

    # Address
        Address1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Address", padx = 2, bg = "#0099cc")
        Address1b1.grid(row = 5, column= 0, padx= 10, pady = 5, sticky = W)

        Addresstxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = PatientAddress)
        Addresstxt.grid(row = 5,column= 1, padx = 10, pady = 5, sticky= E)

    # NHS number
        NHSnumber1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "NHS unique number", padx = 2, bg = "#0099cc")
        NHSnumber1b1.grid(row = 6, column= 0, padx= 10, pady = 5, sticky = W)

        NHSnumbertxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = NHSnumber)
        NHSnumbertxt.grid(row = 6,column= 1, padx = 10, pady = 5, sticky= E)

    # Tablet name
        Tablet1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Tablet", padx = 2, bg = "#0099cc")
        Tablet1b1.grid(row = 7, column =0 , padx = 10, pady = 5)
        
        Tabletcmb = ttk.Combobox(Data_FrameLeft, textvariable= cmbTabletNames , width= 25, state = "readonly", font = ("arial", 12, "bold"))
        Tabletcmb['values'] = ("", "Paracetamol", "Can-p", "Dio-1 One", "Ca1pol", "Amlodipine Besylate", "Nexium", "Singulair", "Plavix", "Amoxicillian", "Azithromycin", "Limcin-900")
        Tabletcmb.current(0)
        Tabletcmb.grid(row = 7, column = 1, padx = 10, pady = 5)

    # No of tablets to take
        No_of_Tablets1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Number of Tablets", padx = 2, bg = "#0099cc")
        No_of_Tablets1b1.grid(row = 8, column= 0, padx= 10, pady = 5, sticky = W)

        No_of_Tabletstxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 27, textvariable = Number_of_Tablets)
        No_of_Tabletstxt.grid(row = 8,column= 1, padx = 10, pady = 5, sticky= E)
    


    # Second table of other details
        HospitalCode1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Hospital Code", padx = 2, bg = "#0099cc")
        HospitalCode1b1.grid(row = 0, column= 2, padx= 10, pady = 5, sticky = W)

        HospitalCode1b1 = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = HospitalCode)
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

        ExpiryDatetxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = ExpiryDate)
        ExpiryDatetxt.grid(row = 4,column = 3, padx = 10, pady = 5, sticky= E)
        

    # Daily Dose
        DailyDose1b1 = Label(Data_FrameLeft , font=("arial", 12, "bold"), width = 20, text= "Dose", padx = 2, bg = "#0099cc")
        DailyDose1b1 .grid(row = 5, column= 2, padx= 10, pady = 5, sticky = W)

        DailyDose1b1  = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = DailyDose)
        DailyDose1b1.grid(row = 5,column = 3, padx = 10, pady = 5, sticky= E)


    # Side Effects
        SideEffects1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width = 20, text= "Side Effects", bg = "#0099cc")
        SideEffects1b1.grid(row = 6, column= 2, padx= 10, pady = 5, sticky = W)

        SideEffectstxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = SideEffects)
        SideEffectstxt.grid(row = 6,column = 3, padx = 10, pady = 5, sticky= E)


    # More info
        MoreInformation1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width = 20, text= "More Information", bg = "#0099cc")
        MoreInformation1b1.grid(row = 7, column= 2, padx= 10, pady = 5, sticky = W)

        MoreInformationtxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = MoreInformation)
        MoreInformationtxt.grid(row = 7,column = 3, padx = 10, pady = 5, sticky= E)

    # Medication(Yes/no)
        Medication1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width = 20, text= "Medication", bg = "#0099cc")
        Medication1b1.grid(row = 8, column= 2, padx= 10, pady = 5, sticky = W)

        Medicationtxt = Entry(Data_FrameLeft, font = ("arial", 12 , "bold"), width = 25, textvariable = Medication)
        Medicationtxt.grid(row = 8,column = 3, padx = 10, pady = 5, sticky= E)

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

        # Prescription label 
        Prescriptiondatarow = Label(Data_Framedata, bg = "White", font=("arial",12, "bold"), text = "Date\tReference id\Patient Name\tDate of Birth\NHS Number\tTablet\tNo of Tablet\tIssued Date\tExpiry Date\tDaily Dose\tStorage Advice")
        Prescriptiondatarow.grid(row = 0, column = 0, sticky= W)
        










if __name__ == " __main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()