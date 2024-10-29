# ## generate seq of numbs b/n 1 and 10 
# for each_number in range(1, 10):
#     print("Each Number: <= ", each_number)

# ## generate seq of even numbs b/n 1 and 10 (inclusive)
# for each_number in range(2, 11, 2):
#     print("Each Number: <= ", each_number)

# ## generate seq of numbs b/n 1 and 10 
# for each_number in range(10, 1, -1):
#     print("Each Number: <= ", each_number)

# # group_of_items = 'Moro'
# class_reg = ['Nat', 'Jul', 'Oscar', 'Tah', 'Lyd']
# for each_item in class_reg:
#     print(each_item)


# user_name = input("Enter your name: ")
# number_times = int(input("Number of times"))
# for each_name in range(1, number_times + 1):
#     print("Your name is: ", user_name )

user_name = input("Enter your name: ")
user_number = int(input("Enter the number of times: "))

if (user_number < 10):
    for each_name in range(1, user_number + 1):
        print(user_name)
else:
    for each_message in range(1, 4):
        print("Too High!!!")

