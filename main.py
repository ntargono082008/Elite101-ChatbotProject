import sys
print("Welcome to the H&M Chatbot")

def chatbot_greeting():
    while True:
        name = input("What is your name? ")
        if name.isdigit(): #new function learned. It checks if the string entered is a digit
            print("Invalid option. Please enter only letters")
        else:
            break
    while True:
        age = input(f"Hello {name} what is your age? ")
        if age.isdigit():
            print(f"Great to here that even at {age} you still choose to shop at H&M")
            break
        else:
            print("Invalid option. Please enter a number")      

def main_menu():
    in_use = True
    print("\nHow may I assist you?")
    print("-------------------------------------")
    print("1. Rate a Purchase")
    print("2. Write a Review")
    print("3. Customer Support")
    print("4. Exit")
    user_input = input("\nEnter a number between 1-4: ")
    if user_input == "1":
        product_review()
    elif user_input == "2":
        product_review()
    elif user_input == "3":
        customer_support()
    elif user_input == "4":
        print("Aw sorry you had to go. Goodbye!")
        in_use = False
    else:
        print("Invalid option: please enter a number between 1-4")
    return in_use

def return_main_menu():
    while True:
        user_choice = input("Would you like to return to the main menu? Yes/No: ")
        if user_choice.lower() == "yes":
            return main_menu()
        elif user_choice.lower() == "no":
            print("Aw sorry to see you go. Have a great rest of your day!")
            sys.exit()
        else:
            print("Invalid option. Please enter either Yes or No.")

def product_rating():
    rating = input("Please enter the product you have purchased: ")
    print(f"The product you have chosen is {rating}.")

    while True:
        user_rating = input(f"On a 1-5 Star rating scale how would you rate {rating}? ")
        if user_rating in ["1", "2", "3", "4", "5"]:
            rating = int(user_rating)
            
            if rating == 5:
                print("I'm glad that you enjoyed your purchase! We hope that we can continue to satisfy you at H&M!")       
            elif rating == 4:
                print("Glad to see that you enjoyed the purchase.")
            elif rating == 3:
                print("Middle of the road is decent.") 
            elif rating == 2:
                print("Aw we're sad to see your not as sastified as you can be.") 
            elif rating == 1:
                print("we are sad to see that you didn't enjoy your purchase. We hope we can do better next time.")

            return_main_menu()
            break
        else:
            print("Please enter a number between 1-5")
    
def product_review():
    review = input("Please enter the product you have purchased: ")
    print(f"The product you have chosen is {review}.")
    print("-------------------------------------")
    print("Please enter your review:")
    user_review = input("")
    print("Thank you for sharing your review.")
    return_main_menu()
    
def customer_support():
    in_use = True
    print("What appears to be your issue?")
    print("-------------------------------------")
    print("1. Return a Product")
    print("2. Shipping Issues")
    print("3. Return to the Main Menu")
    user_input = input("\nEnter a number between 1-3: ")
    if user_input == "1":
       print("Now taking you to the (Return a Product Line)")
       return_product()
    elif user_input == "2":
        print("Now taking you to the (Shipping Issues line)")
        shipping_issues()
    elif user_input == "3":
        print("Now returning to the Main Menu")
        main_menu()
    else:
        print("Invalid option: please enter a number between 1-3")
    return in_use

def return_product():
    while True:
        user_product = input("What would you like to return? ")
        user_clar = input(f"You want to return {user_product}. Is this correct? (YES/NO) ")
        if user_clar.lower() == "yes":
            print("Great! Please head to your local H&MM with your receipt ready. Thank you!")
            break
        elif user_clar.lower() == "no":
            print("Please enter the correct product you wish to return.")
        else:
            print("Invalid input. Please enter YES/NO")
    
def shipping_issues():
    user_shipping = input("What appears to be the issue involving shipping? ")
    print("We apologize to hear that. We will look into it and let you know why this is the case in a later date.")
    user_contactinfo = input("Please enter a method we can contact you. (Email/Phone Number) ")
    print(f"Thank you! We will let you know via {user_contactinfo} very soon.")
    

chatbot_greeting()
main_menu()
