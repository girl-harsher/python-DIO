print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
pay = 0

def enter_rollercoaster (height, pay):
    if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age? "))
        if age < 12:
            pay = 5
            print("Ticket price for child $5.")
        elif age <=18 and age >= 12:
            pay = 7
            print("Ticket price for youths $7.")
        elif age >= 45 and age <= 55:
            pay = 0
            print("Ticket price is free!") 
        else:
            pay = 12
            print("Ticket price for adults $12.")
    else:
        print("Sorry, you have to grow taller before you can ride.")
    return pay

pay = enter_rollercoaster(height, pay)

while True:
    photos = input("Do you want photos? Y or N? ").lower()
    if photos == "y":
        pay += 3
        print(f"+ $3\nThe total is ${pay}")
        break
    elif photos == "n":
        print(f"The total is ${pay}")
        break
    else:
        print("Please, insert a valid command ==> Y or N.")

