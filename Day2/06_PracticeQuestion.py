# #even or odd question
# num = int(input("Enter a number:"))
# if(num%2==0):
#     print("Your number is even.")
# else:
#     print("Your number is odd.")

# #greatest of three numbers
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# third = int(input("Enter your third number: "))

# if(first>second) and (first >third):
#     print("The greatest number is",first)
# elif(second>first) and (second>third):
#     print("The greatest number is ",second)
# else:
#     print("The greatest number is ",third)

# #multiple of 7 or not
# num = int(input("Enter your number:"))
# if(num%7==0):
#     print("Your number is a multiple of 7.")
# else:
#     print("Your number is not a multiple of 7.")

#greatest of 4
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: ")) 
num3 = int(input("Enter your third number: "))
num4 = int(input("Enter your fourth number: "))

if(num1>num2) and (num1>num3) and (num1>num4):
    print("The greatest number is",num1)    
elif(num2>num1) and (num2>num3) and (num2>num4):
    print("The greatest number is",num2)    
elif(num3>num1) and (num3>num2) and (num3>num4):
    print("The greatest number is",num3)    
else:
    print("The greatest number is",num4)
