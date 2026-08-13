#arithmetic operators
a=10
b=5

print(a+b) #addition
print(a-b) #subtraction 
print(a*b) #multiplication
print(a/b) #division
print(a%b) #modulus
print(a**b) #power



#relational operators
print(a==b) #equal to   
print(a!=b) #not equal to
print(a>b) #greater than
print(a<b) #less than
print(a>=b) #greater than or equal to
print(a<=b) #less than or equal to  


#assignment operators
num=10 #assigning value to variable
print("num = ", num)
num+=5 #adding 5 to num
print("num = ", num)
num-=3 #subtracting 3 from num
print("num = ", num)
num*=2 #multiplying num by 2    
print("num = ", num)
num/=4 #dividing num by 4
print("num = ", num)
num%=3 #modulus of num by 3
print("num = ", num)
num**=2 #power of num by 2
print("num = ", num)



#logical operators
print(not True)
print(not False)

val1=True
val2=False  
print("AND operator:", val1 and val2) 
print("OR operator:", val1 or val2) 


#type conversion
a=10
b=3.14  
sum=a+b
print("Sum:", sum)

a=int("2") #type casting from string to int
b=3.14  
sum=a+b
print("Sum:", sum)