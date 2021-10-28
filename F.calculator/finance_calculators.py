import math

print("Good day... Welcome... ")
print('''Choose either Investment or Bond from the list below:
      Investment - to calculate the amount of interest you'll earn on interest. (input I) 
      Bond - to calculate the amount you'll have to pay on a home loan.(input B)''')
#investment =======>
x = input()
if x.lower() == "i":
    print("Please input a deposit/Investment amount:")
    inv = input()
    print("Please input amount of years you'd like to invest for:")
    yr = input()
    print("Please input a interest rate you will prefer:")
    i = float(input())
    n_inter =i/100
    #Simple Or compound calculations =======>
    print("Please choose Simple(Input S) or Compound interest(Input C):")
    a = input()    
    if a.lower() =="s":
        s_int = int(inv)*(1+n_inter*int(yr))
        print("Simple interest result:",s_int)
        act_profit1 =int(s_int)-int(inv)
        print(act_profit1)
    elif a.lower() == "c":
        c_int = int(inv)*math.pow((1+n_inter),int(yr))
        print("Compound interest results: ",c_int)
        act_profit2 =int(c_int)-int(inv)
        print(act_profit2)

#Bond choice and calculations ======>   
elif x.lower() == "b":
    print("Please enter the houses value:")
    h = float(input())
    print("please enter the interest rate:") 
    i_2 = float(input()) 
    bond_inter = (float(i_2)/100)/12
    print("Please enter tyhe amount of months you would like on your Bond payment:")
    b_month = float(input())
    repay = (bond_inter*h)/(1-math.pow((1+bond_inter),(- b_month)))
    print("Your Bond has been calculated repayment is: "+ str(round(repay,2))+" p/month")
else:
    print("ERROR!!! invalid input ")