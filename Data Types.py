print("Welcome to the tip calculator!")
Totalbill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give?10,12,15?\n"))
num_people = int(input("How many to split the bill?\n"))
Bill_perperson = (((Totalbill*(tip*0.01)+Totalbill)/num_people) 
print("Each person should pay: $",Bill_perperson)



