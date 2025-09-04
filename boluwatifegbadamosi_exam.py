# question 1

# def add(num1, num2):
#     return num1 + num2
# def subtract(num1, num2):
#     return num1 - num2
# def multiply(num1, num2):
#     return num1 * num2

# def divide(num1,num2):
#     if num2 != 0:
#         return num1/num2
#     else:
#         raise "zero division error"




# print("===Welcome to Basic Calculator app===")
# while True:
#     print("Basic Operation: ")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. exit")

#     try:
#         choice = int(input("Enter an Operation you would like to perform: "))
#         if choice == 5:
#             print("Exciting the program!")
#             break
#         num1 = float(input("Enter first number: "))
#         num2 =float(input("Enter second number: "))
#     except ValueError as e:
#         print(e)
#         print("Invalid input.")
#     except Exception:
#         print("Invalid input")

        
#         if choice ==1:
#             print("Result:", add(num1,num2))
#         elif choice ==2:
#             print("Result:", subtract(num1,num2))
#         elif choice==3:
#             print("Result:", multiply(num1,num2))
#         elif choice==4:
#             print("Result:", divide(num1,num2))
    
#         else:
#             print("Invalid Input, choose a number between 1-5")








# # Question 2
# while True:
#     user_input = input("Enter a number (or type 'exit' to quit): ")
#     if user_input == "exit":
#         print("Goodbye!")
#         break      # break out of loop
    
#     num = int(user_input)   # convert to integer
    
#     if num % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")


# Question 3

while True:
    try:
        age = int(input("Enter your age (or type exit to quit): "))
        if age >= 18 :
            print("You can vote")
            break
        elif age == "exit":
                print("You can vote")
        else:
            print("You cannot vote")
    

    except Exception as e:
        print("Invalid input")
        
    
    

   
    
