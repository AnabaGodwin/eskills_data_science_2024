User = {}
while len(User) < 10:
    User_input = ("Enter the your fav stop: ")
    if User_input in User:
        print("User alreday exists. Please enter a different user. Thank You: ")
        continue
    
    Team_name = input(" What is the name of your Team: ")
    
    User[User_input] = {"Team_name": Team_name}
print(f"User {User_input}) added successfully!")