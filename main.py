
print("Hello welcome to the food delivery chatbot\n")

name = input("What is your name? ")

resturant = input("\nWhat restruant are you having issues with? ")

print("\n1. My delivery was never completed \n2. I want to add to my order \n3. I didn't get the right food \n4. I cannot find what food I want from "+resturant+ "\n5. I can't get into contact with my deliverer \n6. Cancel")

problem = input("\nI'm sorry " + name + " what seems to be the issue (use number)\n")


def cashback(type):
    if type == "1":
        print("you're total is being converted into in app credit and should be added to your account shortly.")
    elif type == "2":
        print("Sending money to the card which made the purchase.")

def noDelivery():
    compensation = input("1. Do you want cash back on your delivery?\n2. Cancel\n")
    if compensation == "1":
        type = input("\n1. In app credit\n2. Credit/Debit card\n")
        cashback(type)
            
        
    elif compensation == "2":
        quit()
    else:
        print("That is not a valid option, try again")
        noDelivery()

def SecondChoice():
    print("\n1. My delivery was never completed \n2. I want to add to my order \n3. I didn't get the right food \n4. I cannot find what food I want from "+resturant+ "\n5. I can't get into contact with my deliverer \n6. Cancel")

    problem = input("\nI'm sorry " + name + " what seems to be the issue (use number)\n")

    if problem == "1" or problem == "3":
        noDelivery()
    elif problem == "2":
        print("We've already sent your order we cannot add more, you can order again!")
    elif problem == "4":
        print("We are actively updating our menus, please be paitent")
    elif problem == "5":
        print("We'll try contacting them ourselves, please wait.")
    elif problem == "6":
        print("Canceling request!")
    else:
        print("This is not one of the options try 1-6!")
        SecondChoice()

if problem == "1" or problem == "3":
    noDelivery()
elif problem == "2":
    print("We've already sent your order we cannot add more, you can order again!")
elif problem == "4":
    print("We are actively updating our menus, please be paitent")
elif problem == "5":
    print("We'll try contacting them ourselves, please wait.")
elif problem == "6":
    print("Canceling request!")
else:
    print("This is not one of the options try 1-6!")
    SecondChoice()