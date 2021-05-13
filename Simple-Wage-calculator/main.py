bmade = int(input("Enter the number of Bears made \n")) #Gets the user to enter how many bears made
hworked = int(input("Enter how many hours worked \n")) #gets the user to input the hour worked

wage1 = bmade *2 #Times the bears made by 2 which is how many pounds per bear
wage2 = hworked*5 #Times the hours worked by 5 which is £5

if wage1 > wage2:
  print("You have made £",wage1)
elif wage1 < wage2:
  print("You have made £", wage2)
elif wage1 == wage2:
  print(" You have made £",wage1)
else: 
  print("An error has occured. Repeat the proccess")