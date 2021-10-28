import random

#random password generator===============

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789123456789123456789"
special = ";:/.,\\*+-_()[]@#!%?"


upper, lower, nums, spec =True, True, True, True

password = ""

if upper:
    password += upper_case
if lower:
    password += lower_case
if nums:
    password += numbers
if spec:
    password += special

lenght = 12
amount = 1

#print("Password that has been generated.....:")
print("!==========================================================!")
print("Your password is:")
for x in range(amount):
    password = "".join(random.sample(password, lenght))
    print(password)
print("!==========================================================!")