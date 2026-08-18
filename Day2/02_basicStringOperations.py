#                               CONCATENATION
str1="Ishika"
str2="Chaudhary"
print(str1+" "+str2)

#                               LENGTH OF STRING
str3="Ishika Chaudhary" 
print(len(str3)) #this will print the length of the string str3

#                               STRING INDEXING
print(str3[0]) #this will print the first character of the string str3
print(str3[7]) #this will print the eighth character of the string str3

#                                STRING SLICING
#str[starting index:ending index](ending index is not included in the output)
print(str3[0:6]) #this will print the first six characters of the string str3
print(str3[7:]) #this will print the characters of the string str3 from index 7 to the end of the string
print(str3[:9]) #this will print the characters of the string str3 from the beginning of the string to index 8

#                               NEGATIVE INDEXING
str4="APPLE"
print(str4[-1]) #this will print the last character of the string str4
print(str4[-5]) #this will print the first character of the string str4
print(str4[-3:-1]) #this will print the characters of the string str4 from index -3 to index -2