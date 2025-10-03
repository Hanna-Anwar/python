#123=1^1+2^2+3^3=1+4=27=32

n = int(input("enter a number: "))

sum=0

temp =n

while n!=0:

    last_digit = n%10

    sum+=last_digit ** last_digit

    n//=10


print(f"sum of the exponential of {temp} is {sum} ")


