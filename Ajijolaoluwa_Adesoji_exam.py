# Question 1

# Calculator 


# This function adds two numbers
def add(num1, num2):
    return(num1 + num2)

# This function subtracts two numbers
def subtract(num1, num2):
    return num1 - num2

# This function multiplies two numbers and returns the result.
def multiply(num1, num2):
    return num1 * num2

#This function divides a number by another and returns the result. 
# Try and except is also used here to catch ZeroDivision error.
def divide(num1, num2):
    try: 
        if num2 != 0:
            return num1 / num2
        else:
            print("Zero division error! Enter a number that is not zero for num2")
    except ZeroDivisionError:
        print("Cannot divide by zero!!!")

options = """
Enter the following numbers to perform the coressponding operations.

1. Add
2. Subtract
3. Multiply
4. Divide
0. Exit
"""
while True: # This keeps the action going until the user specifies otherwise or an error occurs
    try:
        print(options) # This here is to display the available options to the user
        action = int(input("Choose a number from the available options to proceed: "))
        if action == 0:
            print("You are now exiting the calculator program!!!")
            break
        elif action == 1 or action == 2 or action == 3 or action == 4:   
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        else:
            print("Enter a valid option!")
        
        if action == 1:
            print(f"The addition of {num1} and {num2} is {add(num1, num2)}")
        elif action == 2:
            print(f"{num1} - {num2} is {subtract(num1, num2)}")
        elif action == 3:
            print(f"{num1} * {num2} is {multiply(num1, num2)}")
        elif action == 4:
            if num2 != 0:
                print(f"{num1} / {num2} is {divide(num1, num2)}")
            else:
                print("Cannot divide by Zero!!!")
                continue
        else:
            print("Invalid operation. Please choose from the options available.")
    except ValueError:
        print("Enter a valid number!")
        




# Question 2: Code completion

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ") # Accept input from user
    if user_input == "exit":
        print("Goodbye!") 
        break       # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0: # This checks if the number is even.
        print("The number is even")
    else:
        print("The number is odd")






# Question 3: Debugging

while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break
    
    try:
        if int(age) >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")