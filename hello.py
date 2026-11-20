# Greet the user
print("Hello Person")

# Ask user for their name and stores it in a variable, capitalize user name and removes white space
name = input("What is your name ").strip().title()

#Splits the string into different variables based on the argument passed
first, last = name.split(" ")

#Prints user's name
print(f"Hello {first}", end=", how u doing")

