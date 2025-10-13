# harshad - positive integer that is divisible by the sum of its digit eg: 18  (18>>> 1+8=9 9 is div by 18)

number = int(input("enter a number:"))#18

sum=0

temp = number#18

# if number>0:

#   while number>0:#18>0

#         digits = number %10 #8

#         sum = sum+digits#8

#         number//=10#1


#   if  temp % sum == 0:

#         print("harshad")


#   else:

#         print("not")

# else:
     
#      print("number is negative")

for i in str(number):

    sum += int(i)

print("harshad" if number % sum ==0 else "not harshad")