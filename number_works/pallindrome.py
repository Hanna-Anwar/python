"""
121=121
"""

num = int(input("enter a number :"))#121

rev =0

temp = num#121

while num!=0:

    last_digit = num%10 #1 2 1

    rev= (rev*10) +last_digit#1 , 12 , 121

    num//=10#12  1 0

if temp==rev:

    print("pal")

else:

    print("not")
