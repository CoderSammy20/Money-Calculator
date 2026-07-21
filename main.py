
def main():
    print("Welcome to the Money Calculator!")
    print("Please select an option:")
    print("1. Savings Calculator")
    print("2. Budget Checker")
    print("3. EXIT")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        OptionA()   
    elif choice == "2":
        OptionB()
    elif choice == "3":
        Exit()




def OptionA():
    print("--- Welcome to Money Calculator! ---")
    print("--- How much you have to save up! ---")


    try:
        money_input = input("Enter your total money: ")
        money = int(money_input)

        cost_input = input("Enter the cost of the item: ")
        cost = int(cost_input)

        answer = cost - money
        print(f"You need to save up: {answer}")

        exit_input = input("Do you want to exit? (yes/no): ")
        if exit_input == "yes":
            Exit()
        elif exit_input == "no":
         main()
        else:
         print("Invalid input. Returning to main menu.")
        main()
    except value_error:
        print("Invalid input. Please enter numeric values.")
        OptionA()

 

    
 
  
  

def OptionB():
    print("--- Welcome to Money Calculator! ---")
    print("--- Lets see if you are within budget ---")
    
    try:
        buget_input = input("Enter your budget: ")
        budget = int(buget_input)

        expenses_input = input("Enter your expenses: ")
        expenses = int(expenses_input)

        answer = budget - expenses

        print(f"Your remaining budget is: {answer}")

        if answer < 0:
            print("YOU ARE IN THE NEAGATIVE! YOU ARE BROKE!")
        else:
            print("Everything is fine! You have money left!")

    
            exit_input = input("Do you want to exit? (yes/no): ")
            if exit_input == "yes":
                Exit()
            elif exit_input == "no":
                main()
            else:
                print("Invalid input. Returning to main menu.")
                main()
    except value_error:
        print("Invalid input. Please enter numeric values.")
        OptionB()




def Exit():
    print("Exiting the program. Goodbye!")
    quit()

if __name__ == "__main__":
    main()
