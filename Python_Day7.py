# Creating an empty register
class_reg = []
reg_count = int(input("Enter the number of students to register: "))
for each_user in range(1, reg_count+1):
    user_input = input("Enter your fllname: ")
    class_reg.append(user_input)
print(class_reg)