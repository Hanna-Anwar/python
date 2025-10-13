n1= int(input("enter n1 :"))

n2= int(input("enter n2 :"))

limit = min(n1,n2)

print(limit)

for num in range(2,limit+1):

    if n1%num==0 and n2%num==0:

        gcd=num

print("gcd is :",num)