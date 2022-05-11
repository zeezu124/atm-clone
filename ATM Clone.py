while(1):

    #Defining my users in a list
    registeredUsers = ["John", "Mary", "Bob", "Jane"]

    #Listing out passwords for users
    userPasswords = ["John123", "Mary123", "Bob123", "Jane123"]

    #input field for name
    name = input("What's your name?\n")

    #Looping through the list of users
    if(name in registeredUsers):
        
        #storing the index of the logged in user
        userId = registeredUsers.index(name)
        
        #input field for password
        password = input("What's your password?\n")

        if(password == userPasswords[userId]):

            print("Welcome to Oasis, %s!" % name)
            print("You have $100 in your account.")

            print("What would you like to do?\n")
            
            #Options for the user
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Exit")

            #input field for option
            choice = int(input("Enter your choice: "))
        
            if(choice == 1):
                print("You have chosen to withdraw.")
            elif(choice == 2):
                print("You have chosen to deposit.")
            elif(choice == 3):
                print("You have chosen to check your balance.")

        else:
            print("Wrong password! Please try again.")
            
    else:
        print("Name not found. Please try again.")