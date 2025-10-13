"""048
Ask for the name of somebody the user wants to invite to a party. After this, display the message 
“[name] has now been invited” and add 1 to the count. Then ask if they want to invite somebody else. 
Keep repeating this until they no longer want to invite anyone else to the party and 
then display how many people they have coming to the party.
"""


name = input("enter the name of person you want to invite to the party ")

count = 0

print(f"{name} has now been invited")

count +=1

ask = input("want to invite somebody else (y/n): ")

while ask == "y":

     name = input("enter the name of person you want to invite to the party ")

     count+=1

     ask = input("want to invite somebody else (y/n): ")

print("no of person invited to the party are ",count)










