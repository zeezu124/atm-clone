#Defining my users in a list
registeredUsers = ["John", "Mary", "Bob", "Jane"]

#Listing out passwords for users
userPasswords = ["John123", "Mary123", "Bob123", "Jane123"]

#input field for name
name = input("What's your name?")

#Looping through the list of users
if(name in registeredUsers):
    
    #storing the index of the logged in user
    userId = registeredUsers.index(name)
    
    #input field for password
    password = input("What's your password?")

    if(password == userPasswords[userId]):

        print("Welcome to Oasis, %s !" % name)
        print("You have $100 in your account.")

        print("What would you like to do?")
        
        #Options for the user
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")

        #input field for option
        choice = int(input("Enter your choice: "))
    
    else:
        print("Wrong password!")
        
else:
    print("Name not found. Please try again.")