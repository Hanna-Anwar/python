"""create a variable called compnum and set the value to 50. ask the user to enter a number .'
while their guess is not the same as the compnum value,tell them if their guess is too low or too high and ask them to have another guess.
if they enter the same value as compnum, display the message "Well done,you took[count]attempt"."""

compnum = 50

count =0 

num = int(input("guess a number :"))

count +=1

while num != compnum:

    if num > compnum:

        print("your guess is too high")

        num = int(input("guess again :"))

        count +=1

    if num<compnum:

        print("your guess is too low")

        num = int(input("guess again :"))

        count +=1

print("well done,you took",count,"attempt")





