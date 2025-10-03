#153 = 3^3 +5^3 +1^3


number = int(input("enter a number :"))

length = len(str(number))

print(length)

temp = number

sum =0

while number !=0:

    last_digit = number%10

    sum+= last_digit **length

    number//=10

if sum == temp:

    print(f"{temp} is armstrong")

else:

    print(f"{temp} is not an armstrong")

