numbers = [1,3,2,4]

# print(len(numbers))

target = int(input("enter a target "))

for i in range(0,len(numbers)-1):#(0,4) 0.1.2.3 0

     for j in range(1,len(numbers)):#(1,4)1.2.3.4 1
          
         sum = numbers[i]+numbers[j]  #1+3=4

         if sum == target:
          
          n=numbers[i],numbers[j]

          print(list(n))


          

     


         

