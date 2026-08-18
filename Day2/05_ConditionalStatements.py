# #                             if-elif-else statement
# age = int(input("Enter your age: "))
# if (age < 18):
#     print("You are a minor.")
# elif (age >=18) and (age<60):
#     print("you are an adult.")
# else:
#     print("you are a senior citizen.")

# #two elif statements
# light = "pink"

# if(light=="red"):
#     print("STOP")
# elif(light=="yellow"):
#     print("WAIT")
# elif(light=="green"):
#     print("WALK")
# else:
#     print("light khrab hai")


# #two if statements

# num = 5 
# if(num>2):
#     print("greater than 2")
# if(num>3):
#     print("greater than 3")


#nested if statements
grade = int(input("Enter your grade: "))
if(grade>=50):
    if(grade>=50 and grade<=60):
        print("You have nearly passed.")
    else:
        print("You have passed.")
else:
    print("You have failed.")