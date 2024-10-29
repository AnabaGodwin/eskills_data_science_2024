# 012
# Ask for two numbers. If the first one is larger than the second,
# display the second number
# first and then the first number, 
# otherwise show the first number first and then the second.

# ## asking for two inputs and converting them to integer
# first_number = int(input("Enter your first number: "))

# second_number = int(input("Enter the second number: "))

# ## test for the condition and make a decision
# if (first_number > second_number):
#     print(second_number, first_number)
# else:
#     print(first_number, second_number)

# 013
# Ask the user to enter a number that is under 20. 
# If they enter a number that is 20 or more,
# display the message “Too high”, otherwise display “Thank you”.

# ## take an input from a user 
# user_input = int(input("Enter a number that is less than 20: "))

# ## check if the number is equal to or greater than 20
# if (user_input >= 20):
#     print("Too High")
# else:
#     print("Thank you")

# 014
# Ask the user to enter a number between 10 and 20 (inclusive).
# If they enter a number within
# this range, display the message “Thank you”, 
# otherwise display the message “Incorrect Answer”.

# user_input = int(input("Enter a number b/n 10 and 20: "))

# if ((user_input >= 10) and (user_input <= 20) ):
#     print("Thank you")
# else:
#     print("Incorrect Answer")


# user_input = input("Enter a color: ")

# if ((user_input == "Red") or (user_input == "RED") or (user_input == "red")):
#     print("I like red too")
# else:
#     print("I dont like the color")

# ## take a users weight in kg
# user_weight_kg = int(input("Enter your weight in kilogram: "))

# ## we convert the weight to pounds 
# new_weight_pd = user_weight_kg * 2204 

# ## display the new weight of the user in pounds 
# print("Users Weight in Pounds is: ", new_weight_pd)



# Ask the user if it is raining . 
# If they answer “yes”, ask if it is windy. 
# If they answer “yes” to this second question, 
# display the answer “It is too windy for an umbrella”, 
# otherwise display the message “Take an umbrella”. 
# If they did not answer yes to the first question, display the
# answer “Enjoy your day

# print("Enter [yes] or [no] to the following questions")
# user_input_1 = input("Is it raining?: ")

# if (user_input_1 == "yes"):
#     user_input_2 = input("Is it also windy?: ")
#     if (user_input_2 == "yes"):
#         print("It is too windy for an umbrella")
#     else:
#         print("Take an umbrella")
# else:
#     print("Enjoy your day.")

# 019
# Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they
# enter a 2, display “Well done”, if they enter a 3, display “Correct”. If they enter anything else,
# display “Error message”

print("Enter 1 or 2 or 3")
user_input = int(input("Enter a number of your choice: "))

if (user_input == 1): 
    print("Thank you")
elif (user_input == 2):
    print("Well done")
elif (user_input == 3):
    print("Correct")
else:
    print("Error message")