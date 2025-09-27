"""
ask the user to enter a number between 10 and 20 .
if they enter a value under 10, display the msg "too low" and 
ask them to try again.If they enter a value above 20 ,display the msg "too high"and 
ask them to try again.Keep repeating this until they enter a value that is b/w 10 and 20 and then display the msg "thank you".

"""

num = int(input("enter a number between 10 and 20 :"))

while num<=10 or num >=20:

      if num <=10:

        print("too low")
        
        num = int(input("please enter a number between 10 and 20 :"))

      elif num >=20:
        
        print("too high")

        num = int(input("please enter a number between 10 and 20 :"))

print("THANK YOU")

