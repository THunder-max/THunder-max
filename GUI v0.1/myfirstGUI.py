from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk,Image
from tkinter import messagebox


rootGUI=Tk()
rootGUI.title("Bank App")
rootGUI.geometry("500x500")
img = Image.open("vault.png")
img = img.resize((180,180))
img = ImageTk.PhotoImage(img)
#main code /////////
myLabel = Label( rootGUI, text="Welcome To Citibank \n 'we make you a priority'", fg="black", font=("Calibri",20 , "bold"  ), bg= "white").pack(side=TOP,fill=X)
myLabel2 = Label( rootGUI, bg="black").pack()
myLabel3 = Label( rootGUI, bg="white").pack(side=BOTTOM,fill=X)
img_label = Label(image=img,).pack()
#main window
rootGUI.configure(bg="black")

#========================================================================================================================
#registration window//////
def finishreg():
    name = name1.get()
    password = password1.get()
    deposit = dep1.get()
    bank_accounts = os.listdir()

    if name == "" or password == "" or deposit == "":
        noteif.config(fg="red", text="Please fill in required fields")
        return

    for name_check in bank_accounts:
        if name == name_check:
            noteif.config(fg="red", text="Account already exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n') 
            new_file.write(password+'\n')
            new_file.write(deposit)
            new_file.close()
            messagebox.Message("Account has been registered...")
            noteif.config(fg="green", text="Account has been registered...")
            regis.destroy()
            openLog()
            
            
#========================================================================================================================
def openReg():
    #variables
    global name1, password1, dep1, noteif ,regis
    regis= Toplevel()
    regis.title("Registration")
    regis.geometry("500x500")
    regis.configure(bg="black")
    name1 = StringVar()
    password1 = StringVar()
    dep1 = StringVar()
    Label( regis, text="Welcome To Citibank \n 'we make you a priority'", fg="black", font=("Calibri",20 , "bold"  ), bg= "white").pack(side=TOP,fill=X)
    Label(regis,text="Please register, fill in all you details",bg="black", fg="white", font=("Calibri", 15 , "bold")).pack()
    Label( regis, bg="white").pack(side=BOTTOM,fill=X)
    Label( regis, text="Enter name:", fg="white", font="Calibri", bg="black").pack()
    Entry(regis,textvariable = name1).pack()
    Label( regis, text="Enter password:", fg="white", font="Calibri", bg="black").pack()
    Entry(regis,textvariable = password1,show="*").pack()
    Label( regis, text="Please make an initial deposit to keep the account open, minimum of R50", fg="white", font="Calibri", bg="black").pack()
    Label( regis, text="Initial deposit:", fg="white", font="Calibri", bg="black").pack()
    Entry(regis,textvariable = dep1).pack()
    Button( regis, text="Register", padx = 50, pady =5,font="Calibri", command = finishreg ).pack(pady = 5)
    noteif = Label( regis, fg="white", font="Calibri", bg="black")
    noteif.pack(side=BOTTOM)
#========================================================================================================================
#log in window//////
def finish_log():
    global logname
    bank_accounts = os.listdir()
    logname = name_log.get()
    logpass = pass_log.get()

    for name in bank_accounts:
        if name == logname:
            file = open(name, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            if logpass == password:
                log.destroy()
                global tLabel, submitT
                transact_window = Toplevel()  
                transact_window.title("Account Details")
                transact_window.geometry("500x500")
                transact_window.configure(bg="black")
                Label( transact_window, text="Welcome To Citibank \n 'we make you a priority'", fg="black", font=("Calibri",20 , "bold"  ), bg= "white").pack(side=TOP,fill=X)
                Label(transact_window,text="Hello "+logname ,fg="white", font=("Calibri", 15 , "bold"),bg="black").pack()
                Label(transact_window,text="Please choose a transaction",fg="white", font=("Calibri" "bold"),bg="black").pack()
                Label( transact_window, bg="white").pack(side=BOTTOM,fill=X)
                Button ( transact_window, text="Deposit", padx = 50, pady =5,font="Calibri",command=openDep).pack(pady=5)
                Button ( transact_window, text="Withdrawal", padx = 50, pady =5,font="Calibri",command=openWith ).pack(pady=5)
                Button ( transact_window, text="Personal details", padx = 50, pady =5,font="Calibri", command=personal_details).pack(pady=5)
            else:
                log_noteif.config(fg="red", text="Please Check if the password you entered is correct")
                return
    log_noteif.config(fg="red", text="No account with those details was found please use a registered account")

#========================================================================================================================
def openLog():
    global name_log, pass_log, log_noteif, log
    #vars
    name_log = StringVar()
    pass_log = StringVar()
    log = Toplevel()
    log.title("Log in")
    log.geometry("500x500")
    log.configure(bg="black")
    Label(log, text="Welcome To Citibank \n 'we make you a priority'", fg="black", font=("Calibri",20 , "bold"  ), bg= "white").pack(side=TOP,fill=X)
    Label(log,text="Please enter Log in details",fg="white", font=("Calibri", 15 , "bold"),bg="black").pack()
    Label(log, bg="white").pack(side=BOTTOM,fill=X)
    Label(log, text="Name:", fg="white", font="Calibri", bg="black").pack()
    Entry(log,textvariable = name_log).pack()
    Label(log, text="Password:", fg="white", font="Calibri", bg="black").pack()
    Entry(log,show="*",textvariable = pass_log).pack()
    Button(log, text="log in", padx = 50, pady =5,font="Calibri",command = finish_log).pack(pady=20)
    log_noteif = Label(log,fg="white", font="Calibri", bg="black")
    log_noteif.pack(side=BOTTOM)
#========================================================================================================================
#Deposits and withdrawals/////////
def openDep():
    global dnoteif, Dep_amount, current_balance, cbNoteif
    dep= Toplevel()
    dep.title("Transaction: Deposits")
    dep.geometry("500x500")
    dep.configure(bg="black")
    Dep_amount = StringVar()
    file = open(logname,"r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_balance = user_details[2]
    #widgets
    Label(dep, text="Welcome To Citibank \n 'we make you a priority'", fg="black", font=("Calibri",20 , "bold"  ), bg= "white").pack(side=TOP,fill=X)
    Label(dep,text=logname+"'s Deposit screen",bg="black", fg="white", font=("Calibri", 15 , "bold")).pack()
    Label(dep, bg="white").pack(side=BOTTOM,fill=X)
    cbNoteif = Label(dep, text=" Your current balance : R" + details_balance, fg="white", font="Calibri", bg="black")
    cbNoteif.pack()
    Label(dep, text="Amount :", fg="white", font="Calibri", bg="black").pack(pady=5)
    Entry(dep, textvariable = Dep_amount).pack()
    Button (dep, text="Proceed", padx = 50, pady =5,font="Calibri" , command=dep_done).pack(pady=5)
    dnoteif = Label(dep, fg="Green", font="Calibri", bg="black")
    dnoteif.pack()

def dep_done():
    
    if Dep_amount.get() == "":
        dnoteif.config(text="Amount required ........!!!", fg="red")
    if float(Dep_amount.get()) <=0:
        dnoteif.config(text="Negative currency not accepted", fg="red")
        return
    else:
        global new_current
        file = open(logname, "r+")
        file_data = file.read()
        user_details = file_data.split("\n")
        current_balance = user_details[2]
        new_current = current_balance
        new_current = float(new_current) + float(Dep_amount.get()) 
        file_data = file_data.replace(current_balance, str(new_current))
        file.seek(0)
        file.truncate()
        file.write(file_data)
        file.close() 
        cbNoteif.config(text="Your new current balance : R" +str(round(new_current,2)), fg="green")
        dnoteif.config(text="Deposit Successful!!!", fg="green")

 #========================================================================================================================
def openWith():
    global withDnoteif, withD_amount, current_balance, wNoteif
    withD= Toplevel()
    withD.title("Transaction: Deposits")
    withD.geometry("500x500")
    withD.configure(bg="black")
    withD_amount = StringVar()
    file = open(logname,"r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_balance = user_details[2]
    #widgets
    Label(withD, text="Welcome To Citibank \n 'we make you a priority'", fg="black", font=("Calibri",20 , "bold"  ), bg= "white").pack(side=TOP,fill=X)
    Label(withD,text=logname+"'s Deposit screen",bg="black", fg="white", font=("Calibri", 15 , "bold")).pack()
    Label(withD, bg="white").pack(side=BOTTOM,fill=X)
    wNoteif = Label(withD, text=" Your current balance : R" + details_balance, fg="white", font="Calibri", bg="black")
    wNoteif.pack()
    Label(withD, text="Amount :", fg="white", font="Calibri", bg="black").pack(pady=5)
    Entry(withD, textvariable = withD_amount).pack()
    Button (withD, text="Proceed", padx = 50, pady =5,font="Calibri" , command=fin_withdraw).pack(pady=5)
    withDnoteif = Label(withD, fg="Green", font="Calibri", bg="black")
    withDnoteif.pack()

def fin_withdraw(): 
    if withD_amount.get() == "":
        withDnoteif.config(text="Amount required ........!!!", fg="red")
        return
    if float(withD_amount.get()) <=0:
        messagebox.askretrycancel("ERROR","Negative currency not accepted")
        return
    else:
        file = open(logname, "r+")
        file_data = file.read()
        user_details = file_data.split("\n")
        current_balance = user_details[2]
        if float(withD_amount.get()) >float(current_balance):
            withDnoteif.config(text="OOOPS!!!! looks like your supply is Dry.", fg="red")
            return
            
        new_current = current_balance
        new_current = float(new_current) - float(withD_amount.get())
        #new file data 
        file_data = file_data.replace(current_balance, str(new_current))
        file.seek(0)
        file.truncate()
        file.write(file_data)
        file.close() 

        wNoteif.config(text="Your new current balance : R" + str(round(new_current,2)), fg="green")
        withDnoteif.config(text="Withdrawal Successful!!!", fg="green")

def personal_details():
    file = open(logname,"r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_name = user_details[0]
    details_balance = user_details[2]
#personal window  
    personal_details_screen = Toplevel()
    personal_details_screen.geometry("500x500")
    personal_details_screen.configure(bg="black")
    personal_details_screen.title("Personal Details")
    Label(personal_details_screen, text="Welcome To Citibank \n 'we make you a priority'", fg="black", font=("Calibri",20 , "bold"  ), bg= "white").pack(side=TOP,fill=X)
    Label(personal_details_screen,text="Personal Details ",bg="black", fg="white", font=("Calibri", 15 , "bold")).pack()
    Label(personal_details_screen, bg="white").pack(side=BOTTOM,fill=X)
    Label(personal_details_screen, text="Account holder Name : " + details_name, fg="white", font="Calibri", bg="black").pack(pady=5)
    Label(personal_details_screen, text="Current balance : R " + details_balance ,fg="white", font="Calibri", bg="black").pack(pady=5) 
#========================================================================================================================
#MAIN WINDOW WIDGETS///////
regis_btn =Button (rootGUI, text="Start your journey", padx = 50, pady =5,font="Calibri", command = openReg ).pack(pady=5)
login_btn =Button (rootGUI, text="Continue your journey" , padx = 35, pady = 5,font="Calibri", command = openLog ).pack(pady=5)
quit_btn =Button (rootGUI, text="Stop proceedings", padx = 50, pady =5,font="Calibri", command = rootGUI.quit).pack(pady=5) 
rootGUI.mainloop()

