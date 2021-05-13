#Index

#For print statements go to line 15
#For variables go to line 20
#For Basic maths go to line 28
#For If statements go to line 44
#For while loops go to line 55
#For for loops go to line 63
#For Casting go to line 71
#For Text files go to line 81




#                  Print statements


print("Cheese") #This is a print statement, this is used to print statements in python It is used to display a statement. The quoation marks ("")Must be used or a syntax error will be formed

#                Variables (Strings, boolean, intregers, array, float)
print("************************Variables********************************************")
string = ("This is a string") #The first part of this code is the name of the variables. This is used to call on the variable laterr on. This variable is not able to be changed and is a defined variable. Strings are able to store any infomation
string = input("Enter a word") #This is allowing the user to add a input into the string
intreger = ("35") #This variable can be used to store WHOLE Numebers
integer = int(input("Enter A Number")) #The words int(input)) are required for a number to be entered
float1 = ("1.034")# This is a float. A float can store decimal numbers. 

#                            Basic Maths 
print("***************************Basic Maths*****************************************")

num1 = int(input("Enter a number")) #This is a Integter. It allows the user to add a input of numbers. 
num2 = int(input("Enter a second number"))

aswr = num1 + num2 #This statement is adding the 2 numbers that was added before togther. 
print(aswr) #this is printint the answer 

#The next statement is showing the features of adding maths

print(num1+num2)#This adds the 2 numbers togther
print(num1*num2)# This is multiplying the 2 numbers
print(num1/num2)# This is dividing the numbers This statement is dividing num1 by num2
print(num1-num2)#This is subtracting the 2 numbers

#                        IF statements
print("*************************If statement*******************************************")
password = int(input("Enter Password")) #This will be used for if statements

if password == 1234: #if the passworsd is equal to:
  print("Password Correct")
else: #everything else:
  print("Incorrect Password")


#                    While Loops
print("**********************While Loops**********************************************")
loop = int(input("How long do you want the program to loop for?"))

while loop > 0: #This statement is saying while the number entered in loop is bigger than 0 the code will run
  print("Cheese") #This is the statement that will be printed when the program is running
  loop = loop - 1 #This takes 1 away from the inputed number each time it is run to prevent the code from running infinatly


#              For loops
print("************************For Loops********************************************")
for counter in range (0, 100):
  print("Hello")
  print("I am repeating 100 times")



#                           Casting

#Casting is how the data type of a variable
print("**************************Casting******************************************")
age=25
age=float(age)
print(age)
age=str(age)
print (age*2)

#                      textfiles
print("********************************************************************")
#Text files is used to save infomarion or data ebwteen program uses
#
file = open("TestFile.txt", "a") #This finds the file but if its not found it creeates one

file.write("My First Words in a text file\n")
file.close()

#                      Printing the time
print("*************************Time*******************************************")

import datetime

x = datetime.datetime.now()
print(x)


#                   Lists

# A list is used to store different items within one variable. The list starts with the Variable name. then a [ to start the list, a "" must be used to store charcaters, a comma must be used to seperate the different items. Then a ] is used to finish the list
print("***********************Lists*********************************************")
#Lists are collections of data stored under a single variavble. They can then be called individually by a number
list1 = ["Bob", "Jeff", "Bojo"] # Adds strings to a list

print(list1) #Prints The list that is defined

print(list1[0])
#To create alist inside a list we can do a 2 dimension list.

list2=[["Bob","Jeff",'Bojo'],["Elim", "Jeffery"]]
print(list2[1][1])
name = input("Enter new name")
list1.append(name)
list1.sort()
print(list1)
list1.remove("Bob")
print(list1)
#lists can be sorted by listname.sort()
#To add a list listname.append(item)
#Remove an item from listname.remove(item)
#                 Selection

# Selectrion is used to control what will happen next. It compares an item next to another item.
print("***********************Selection*********************************************")
bob = (1) 
jeff = (2)

if bob == jeff: #If bob is the same as jeff then.
  print("Bob is the same as jeff")
elif bob < jeff: #if the last statement is false and bob is smaller than jeff then:
  print("Bob is smaller than jeff")
elif jeff < bob: #If the last statments is false and bob is bigger than jeff then:
  print("Bob is bigger than jeff")
else: #If all else is false then:
  print("error 303")#

b= input("Enter a word")
#                  
time1 = open("Time.txt", "a")

time1.write(b)
time1.close()


egg = "hellp"
print (egg[1:2])