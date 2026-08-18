#                       ESCAPE SEQUENCE CHARACTERS
# \n - new line
# \t - tab
# \\ - backslash
# \' - single quote
# \" - double quote

str1="This is a string."
str2='This is also a string.'
str3="""This is a string that 
spans multiple lines."""
str4='''This is also a string that 
spans multiple lines.'''
str5='This is ishika\'s python learning journey.'#this is an example of escaping a single quote in a string
str6="user's input" #this is an example of using a single quote in a string without escaping it by using double quotes to define the string
str7="This is a string with a \"double quote\" inside it."#this is an example of escaping a double quote in a string
str8="This is a string that adds new line\nin between the string."
str9="\tThis is a string that adds a tab"
str10="This is a string that adds a backslash \" \\ \" in between the string."

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)
print(str8)
print(str9)
print(str10)