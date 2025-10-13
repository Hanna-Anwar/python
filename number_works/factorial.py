num = int(input("enter a number:")) #4

fact =1

for i in range(1,num+1): #i=1,2,3,4
  
  fact =fact * i # 1* 1 1*2 3*2  3*2*4

print(f"factorial of {num} is {fact}")

