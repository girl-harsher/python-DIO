menu = '''
[1] Deposit
[2] Draw
[3] Extract
[4] Exit

=> '''

balance = 500
limit = 500
extract = ""
withdrawals = 0
LIMIT_WITHDRAWALS = 3

while True:
    option = input(menu)
    
    if option == "1":
        deposit = float(input("Deposit value ==> "))
        balance += deposit
        print(f"Deposit successfully! Your balance is ${balance}")
        break
        
    elif option == "2":
        if withdrawals < LIMIT_WITHDRAWALS:
            draw = float(input("Value Draw ==> "))
            if draw <= balance:
                balance -= draw
                withdrawals += 1
                print(f"Draw {draw} successfully! ")
            else:
                print("Insufficient funds!")
        break
    
    elif option == "3":
        print("Extract")
        break
        
    elif option == "4":
        print ("Exit")
        break
    
    else:
        print("Invalid operation, please insert a valid command!")
    
    
        

