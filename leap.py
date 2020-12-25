#Goal:Check whether the given year is leap year or not

#Step1:Take user_input in integer value
a = input("Enter the Year: ")

#Step2:Use conditional statement
if (a %4)== 0: #check give input is divisible by 4
  print ("This is a Leap Year")
elif (a %100)== 0: #check give input is divisible by 100
  print ("This is a Leap Year") 
elif (a %400)== 0: #check give input is divisible by 400
  print ("This is a Leap Year")
else : 
  print ("This is not a Leap Year")
