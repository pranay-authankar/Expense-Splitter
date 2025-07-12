record = {}
individual = {}

def add_member(main_dict, net_individual):

    # Input for adding Member
    while True:
        member = input("\nAdd Member : ").lower().strip().capitalize()
        if member and member.isalpha():
            if member not in main_dict:                                     # Checks existance of member
                main_dict[member] = {}                                      # Creates an empty dictionary for member
                print((f"{member} added").center(20, "-")) 
            else:
                print(f"{member} already exists\nTry again with new name")
                continue

        if member == "0":
            if len(main_dict) < 2:
                print("\nYou need to pay all your Expenses\nKeep your wallet with full of fuel\nOr add member to reduce load")
                break
            break
        
        # Assiging value to every key's empty dictionary
        for member in main_dict:
            for person in main_dict:
                if person != member:                # Checking same person does not contain itself
                    main_dict[member][person] = 0   # Assigning 0 to every person's borrower's value as initial balance
                else:
                    continue
        
        # Assigning 0 to every individual's initial balance
        for individual in main_dict:
            net_individual[individual] = 0

def add_expense(main_dict, net_individual):

    error = "\nInvalid Output\nTry Again"

    # Input for 'Payer'
    while True:
        payer = input("Who Paid : ").lower().strip().capitalize()
        if payer and payer in main_dict:
            break
        else:
            print(error)
            continue
    
    # Input for 'Amount' Paid by Payer
    while True:
        amount = input("Amount : ").strip()
        if amount and amount.isdigit():
            amount = int(amount)
        else:
            print(error)
            continue

        if amount >= 0:
            break
        else:
            print(error)
            continue
    
    # Creating 'empty list' with every borrower from the payer
    borrower_list = []

    i = 0   # Increases after every borrower added to borrowers_list - To stop when every member is added to it

    # Input for 'borrower'
    while True:
        borrower = input("Paid For : ").lower().strip().capitalize()
        
        # Verifying; 
        # - that every borrower is from the members
        # - Borrower is existing or not in the list
        if borrower and borrower in main_dict:
            if borrower not in borrower_list:
                borrower_list.append(borrower)
                i += 1
                print((f"{borrower.capitalize()} added").center(20,"-"))
                if len(main_dict) == i:
                    break
                else:
                    continue
            else:
                print(f"\n{borrower} Already Exist\nTry with different name")
                continue
        elif borrower == "0":
            break
        else:
            print(error)
        
    # Splitting the amount paid by payer for borrower equally
    expense_split = amount / len(borrower_list)
    
    # Main Calculations

    if payer not in borrower_list:                          # When payer does not exists in borrow_list
        
        net_individual[payer] += amount                     # Add the 'Total receivable payment' paid by buyer to their individual balance
        for borrower in borrower_list:
            net_individual[borrower] -= expense_split       # Reduces splitted amount from borrower's individual balance
            main_dict[payer][borrower] -= expense_split     # Reduces splitted amount from payer -> borrower: balance
            main_dict[borrower][payer] += expense_split     # Adds splitted amount from borrower -> payer: balance

    else:                                                   # When payer does not exists in borrow_list
        borrower_list.remove(payer)                         # Removes payer's name from borrower's list for further calculations
        net_individual[payer] += (amount - expense_split)   # Add the 'Total payment paid by buyer - splitted' to their individual balance

        
        for borrower in borrower_list:                      # Here, borrower_list do not contain payer's name
            net_individual[borrower] -= expense_split       # Reduces splitted amount from borrower's individual balance
            main_dict[payer][borrower] -= expense_split     # Reduces splitted amount from payer -> borrower: balance
            main_dict[borrower][payer] += expense_split     # Adds splitted amount from borrower -> payer: balance


def view_balance(main_dict, net_individual):
    print(f"{"-".center(30, "-")}")
    print("\nEvery individual Person net Payement\n")
    print(f"{"-".center(30, "-")}")

    # To print Individuals net Payable / Receivable
    for person in net_individual:
        if net_individual[person] > 0:
            print(f"{person}'s Accounts")
            print(f"{person} need to receive {net_individual[person]:.2f} Rs.\n")
            print(f"{"-".center(30, "-")}")
        elif net_individual[person] < 0:
            print(f"{person}'s Accounts")
            print(f"{person} need to Pay {-net_individual[person]:.2f} Rs. - Credit Score will be affected dude. - PAY NOW !!\n")
            print(f"{"-".center(30, "-")}")
        else:
            print(f"{person}'s Accounts")
            print(f"\nWow {person}, You increased your credit score dude\n")
            print(f"{"-".center(30, "-")}")


    print(f"{"x".center(30, "-")}")

    print("\nNet Settlement Between Members\n")

    # To print Every single Transaction to be done
    for payer in main_dict:

        print(f"{"-".center(30, "-")}\nCollection of {payer}")
        for borrower in main_dict:
            if payer != borrower:
                if main_dict[payer][borrower] < 0:
                    print(f"-> {borrower} need to pay {payer} Rs. {-main_dict[payer][borrower]}")
                else:
                    continue
            else:
                continue
    print(f"{"-".center(30, "-")}")
        

def expense_tracker(main_dict, net_individual):

    error = "\nInvalid Output\nTry Again\n"
    print("\nWelcome to Expense Tracker\n")

    purpose = input("What's the purpose : ")
    print(f"\n{purpose}'s Expense Trackers")

    print("\nAdd members")
    add_member(main_dict, individual)

    print(f"\nMembers for {purpose}")
    for member in main_dict:
        print(member)
    
    # To ask what task to be performed
    while True:
        print("\nTasks: [Enter 0 to stop whenever there is need of more than one input]\n1. Add Expense\n2. View Balance\n0. Exit Program")
        choice = input("\nEnter task : ")
        if choice and choice.isdigit():
            choice = int(choice)

            # To mach choice input to desired program
            match choice:
                case 1: add_expense(main_dict, net_individual)
                case 2: view_balance(main_dict, net_individual)
                case 0: print("\nSee you soon\n"); break
        else:
            print(error)

expense_tracker(record, individual)
