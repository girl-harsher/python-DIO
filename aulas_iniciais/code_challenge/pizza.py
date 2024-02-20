print("Thank you for choosing Python Pizza Deliveries!")
size = input() 
add_pepperoni = input() 
extra_cheese = input() 
bill = 0

if size == "S" or size == "s":
    bill += 15
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 2
    if extra_cheese == "Y" or extra_cheese == "y":
        bill += 1
    else:
        bill
else:
    bill
    
if size == "M" or size == "m":
    bill += 20
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 3
    if extra_cheese == "Y" or extra_cheese == "y":
        bill += 1
    else:
        bill
else:
    bill
    
if size == "L" or size == "l":
    bill += 25
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 3
    if extra_cheese == "Y" or extra_cheese == "y":
        bill += 1
    else:
        bill
else:
    bill
    
print(f"Your final bill is: ${bill}")

#
    
    

