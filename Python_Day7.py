# Creating an empty register
#class_reg = []
#reg_count = int(input("Enter the number of students to register: "))
#for each_user in range(1, reg_count+1):
 #   user_input = input("Enter your fllname: ")
#    class_reg.append(user_input)
#print(class_reg)



## Functions
# Creating to add two number
#def addition(num1, num2):
 #   result = num1 + num2
 #   return result
#add = addition(3, 5)
#print("the sum of adding two numbers is: ", add)
#print(f"The sum of adding two numbers: {add}")


# funtion for sub
#def substraction(numb1, numb2):
  #  ans = (numb2 - numb1)
   # return ans
#substraction(19, 59)
#final_ans = substraction(19, 59)
#print(f"The final answer is {final_ans}")

# Creating an input fuction.
def inputs():
    sales_amount = float(input("Enter your sales amount for the day: "))
    commission_rate = float(input("Enter your sales commission rate: "))
    return sales_amount, commission_rate
# calling the input fuction in the addition fuction
#def addition(x,y):
  #  ans = x + y
 #   return ans
#x, y = inputs()
#ans2 = addition(x, y)
#print(ans2)

# Calling the input fuction in the Multiplecation Funtion
#def Multip(x, y):
 #   product = (x*y)
#    return product
#x, y = inputs()
#final_product = Multip(x,y)
#print(final_product)

def cal_commission(sales_amount, commission_rate):
    commission = ((commission_rate/100)*sales_amount)
    return commission
sales_amount, commission_rate = inputs()
final_commission = cal_commission(sales_amount, commission_rate)
print("Kindly note that your take home commission for the day is: ", final_commission) 


    
    