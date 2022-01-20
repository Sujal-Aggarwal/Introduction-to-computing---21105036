print('Question1')

#Taking input from user
input_str = input("Enter the string : ")

#Printing the length of the string
print("The length of the given string is : %s" % len(input_str))

#Creating reversed string
reversed_str = input_str[ : : -1 ]                                                                      
print("The string in reverse would be : %s" % reversed_str)

#Creating a new string
new_str = input_str[10:26]                                                                                           
print("The new string becomes : %s" % new_str)
new_str = "object oriented"

#Replacing the value
print("The replaced substring will be : %s" % new_str)
substr = "a"

#Finding the index value of the given substring
indx = input_str.find(substr)                                                                           
if indx == -1:
    print("The given substring was not found in the inputted string")
else:
    print("The first occurence of the given substring \"%s\" is at index no. = %d" % (substr, indx))   
no_white_spaces_str=input_str.replace(" ","")

#Removing white spaces
print("The inputted strings with no white spaces will be \"%s\"\n" % no_white_spaces_str)

print("\n")
print("####################################################################################")
print("\n")  
print("Question 2\n")

# Initializing variables.
name = "Sujal Aggarwal"
SID = "21105036"
department = "ECE"
CGPA = "10"

# Printing statements in the given format.
print(f"Hey, {name.title()} here! \nMy SID is {SID} \nI am from {department} and my CGPA is {CGPA}")
print("\n")  
print("#####################################################################################")
print("\n")  

print("Question 3")


a = 56
b = 10

print(" a&b : ", a & b)
print(" a|b : ", a | b)
print(" a^b : ", a ^ b)

# Left shift both a and b with 2 bits.
print("a<<2 : ", a << 2, "\tb<<2 :", b << 2)
# Right shift a with 2 bits and b with 4 bits.
print("a>>2 : ", a >> 2, "\tb>>2 :", b >> 2)

print("\n")  
print("##################################################################################")
print("\n")  

print("Question 4")

# taking input of 3 numbers from the user.
a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))
c = int(input("Enter 3rd no. : "))

#finding the highest no.
if a > b:
    if a > c:
        highest_number = a
    else:
        highest_number = c

if b > a:
    if b > c:
        highest_number = b
    else:
        highest_number = c


print(f"Highest no. = {highest_number}")

print("\n")  
print("##################################################################################")
print("\n")  

print("Qustion 5")

# taking input string from the user.
input_string = input("Enter input string: ")

if "name" in input_string:
    print("Yes , 'name' is present in the string")
else:
    print("No , 'name' is not present in the string")
  
print("\n")  
print("################################################################################")
print("\n")  


print("Question 6\n")

# taking input of 3 lengths from the user.
a = int(input("Enter 1st length : ")) 
b = int(input("Enter 2nd length : "))
c = int(input("Enter 3rd length : "))

# checking condition for triangle.
if a+b > c and a+c > b and b+c > a:
    print("Yes , it can form a triangle")
else:
    print("No , it can't form a traingle")


#########################################################################
