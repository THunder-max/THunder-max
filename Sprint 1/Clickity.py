from tkinter import *

x = 0

def add():
    global x, amount_Click

    x += 1
    amount_Click.pack_forget()
    amount_Click =Label(Click,text="This button was clicked " + str(x))
    amount_Click.pack()

Click=Tk()
Click.title("Click counter")
Click.geometry("200x100")

button = Button(Click,text="Click Me ", command= add, padx=10, pady=10, bg="red")
button.pack()
amount_Click =Label(Click,text= "This button was clicked " + str(x))
amount_Click.pack()


#===================================================
Click.mainloop()