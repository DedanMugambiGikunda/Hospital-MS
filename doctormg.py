import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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



        
if __name__ == "__main__":
    root = Tk()
    app = doctor(root)
    root.mainloop()