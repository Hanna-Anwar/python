
'''047
Ask the user to enter a number and then enter another number.
 Add these two numbers together and then ask if they want to add another number.
 If they enter “y”, ask them to enter another number and keep adding numbers until they do not answer “y”. 
Once the loop has stopped, display the total.
'''
n1= int(input("enter n1:"))

n2 = int(input("enter n2:"))

sum = n1+n2
  
ask = input("want to add one more no y/n:")

while ask == "y":

    n = int(input("enter no:"))

    sum += n

    ask = input("want to add one more no y/n :")


print(sum)


