from tkinter import *
from tkinter import font

calculation = ""


def addto_calculation(symbol):
    global calculation
    calculation += str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0, calculation)
    
# this function (eval()) evaluates a python code
def evaluate_calculation():
    global calculation 
    try: 
        calculation = str(eval(calculation))
        result.delete(1.0, "end")
        result.insert(1.0, calculation)

    except:
        clearall()
        result.insert(1.0, "Error")




def clearall():
    global calculation
    calculation = ""
    result.delete(1.0, "end")

calroot=Tk()
calroot.title("Calculator")
calroot.geometry("250x250")
calroot.resizable(0,0)
calroot.configure(bg="black")
global result
#text field====

result = Text(calroot,height =1, width= 17, font =("calibri", 20))
result.grid(columnspan=10)
#number buttons ===========
b_1 = Button(calroot, text="1", command=lambda: addto_calculation(1), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_1.grid( row= 4, column = 1)
b_2 = Button(calroot, text ="2", command=lambda: addto_calculation(2), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_2.grid( row= 4, column = 2)
b_3 = Button(calroot, text="3", command=lambda: addto_calculation(3), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_3.grid( row= 4, column = 3)
b_4 = Button(calroot, text="4", command=lambda: addto_calculation(4), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_4.grid( row= 3, column = 1)
b_5 = Button(calroot, text="5", command=lambda: addto_calculation(5), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_5.grid( row= 3, column = 2)
b_6 = Button(calroot, text="6", command=lambda: addto_calculation(6), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_6.grid( row= 3, column = 3)
b_7 = Button(calroot, text="7", command=lambda: addto_calculation(7), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_7.grid( row= 2, column = 1)
b_8 = Button(calroot, text="8", command=lambda: addto_calculation(8), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_8.grid( row= 2, column = 2)
b_9 = Button(calroot, text="9", command=lambda: addto_calculation(9), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_9.grid( row= 2, column = 3)
b_0= Button(calroot, text="0", command=lambda: addto_calculation(0), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_0.grid( row= 5, column = 2)
# functions (+,-,*,/)
b_add= Button(calroot, text="+", command=lambda: addto_calculation("+"), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_add.grid( row= 2, column = 4 )
b_sub= Button(calroot, text="-", command=lambda: addto_calculation("-"), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_sub.grid( row= 3, column = 4 )
b_div= Button(calroot, text="/", command=lambda: addto_calculation("/"), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_div.grid( row= 4, column = 4 )
b_mult= Button(calroot, text="*", command=lambda: addto_calculation("*"), width =5, font=("calibri", 15, "bold"), fg="black", bg="white")
b_mult.grid( row= 5, column = 4 )
b_eq= Button(calroot, text="=", command=evaluate_calculation, width = 5,font=("calibri", 15, "bold"), fg="black", bg="white")
b_eq.grid(row= 6,column = 1 )
b_point= Button(calroot, text=".", command=lambda:addto_calculation("."), width = 5,font=("calibri", 15, "bold"), fg="black", bg="white")
b_point.grid(row= 6,column = 2 )
b_clear= Button(calroot, text="CA", command=clearall, width =11, font=("calibri", 15, "bold"), fg="black", bg="white")
b_clear.grid( row= 6 ,column = 3, columnspan = 2 )

#brackets ====
b_brack1= Button(calroot, text="(", command=lambda: addto_calculation("("), width =5,font=("calibri", 15, "bold"), fg="black", bg="white")
b_brack1.grid( row= 5, column = 1 )
b_brack2= Button(calroot, text=")", command=lambda: addto_calculation(")"), width =5,font=("calibri", 15, "bold"), fg="black", bg="white")
b_brack2.grid( row= 5, column = 3 )









calroot.mainloop()