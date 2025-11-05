print("Welcome to the H&M Chatbot")

def chatbot_greeting():
    name = input("What is your name? ")
    age = input(f"Hello {name} what is your age? ")
    print(f"Great to here that even at {age} you still choose to shop at H&M")

def display_menu():
    print("1. Placeholder")
    print("2. Placeholder")
    print("3. Placeholder")
    print("4. Exit")

def user_selection():
    in_use = True
    user_input = input("\nEnter a number between 1-4: ")
    if user_input == "1":
        print("1")
    elif user_input == "2":
        print("2")
    elif user_input == "3":
        print("3")
    elif user_input == "4":
        print("Exit program")
        in_use = False
    else:
        print("Invalid option: please enter a number between 1-4")
    return in_use



chatbot_greeting()
display_menu()
user_selection()
