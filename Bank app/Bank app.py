import math
import datetime
date = datetime.datetime.now()
trans_list =  open("Transaction_list.txt", "r")
trans_list.close()
bankbaln = open("Bank_data.txt", "r")
amnt =bankbaln.read()
bankbaln.close()

print("Welcome")
print("Would you like to make a transaction (please enter yes or no):")

trans = input(str())

if trans.lower() == "yes":
    bankbaln = open("Bank_data.txt", "r")
    print("your balance is R",bankbaln.read())
    print("For Withdrawal input W and for Deposits input D") 
    x = input(str())
    if x.lower() == "w":
            print("please enter a Withdrawal amount")
            w = input()
            z = w.isnumeric()
            while z == False:
                print('Please enter numbers only')
                w = input()
                z = w.isnumeric()
                
            withdrew = float(amnt) - float(w)
            
            if float(w) > float(amnt):
                print("Transaction failed insufficient Funds")
            else:
                print("Transaction successful amount withdrew: R", w)
                print("Current balance: R", withdrew)
                print("Goodbye")
                trans_list =  open("Transaction_list.txt", "a")
                trans_list.write("Withdrawal done: R"+ w + '\n' )
                trans_list.write("Time: " +str(date) + "\n")
                trans_list.close()
                bankbaln = open("Bank_data.txt", "w")
                bankbaln.write(str(withdrew))     
                bankbaln.close()
                           

    if x.lower() == "d":
            print("please enter a Deposit amount")
            d = input()
            z = d.isnumeric()
            while z == False:
                print('Please enter numbers only')
                d = input()
                z = d.isnumeric()
                
            dep = float(amnt) + float(d)
            
            print("Transaction succesfu, Deposited amount is: R", d)
            print("Current balance: R", dep)
            print("Goodbye")
            trans_list =  open("Transaction_list.txt", "a")
            trans_list.write("Deposit done: R"+ d + '\n' )
            trans_list.write("Time: " +str(date) + "\n")
            trans_list.close()
            
            bankbaln = open("Bank_data.txt", "w")
            bankbaln.write(str(withdrew))     
            bankbaln.close()
                         
                           
elif trans.lower() == "no":
    print("Transaction cancelled")
else:
    print("Something went south")
           
            