menu ={

    "Rice": 60,
    "Wheat": 55,
    "Milk": 50,
    "Sugar": 45,
    "Oil": 120,
    "Egg": 70,
    "Bread": 40,
    "Fruits": 150,
    "Vegetables": 100

}

# customer details

name = input("enter name :")

phone_no = int(input("enter phone number :"))

print(f"hello dear {name},Welcome to the grocery shopping")

cart = []

while True:

    print("Available items are")

    for item,price in menu.items():

        print(f"{item} :rs {price}")


    choice = input("enter the name of the item :")

    if  choice in menu:

        kilo = int(input("enter the kilo :"))

        cart.append([choice,menu.get(choice),kilo])

        print(cart)

    else:

        print("invalid choice")

    more = input(f"add more? (Y/N)")

    if more!= "y":

        break

    # bill calculate


sum =0 

for item,price,kilo in cart:

    sum += price * kilo

print(f"Total amount to be paid is rs {sum}")

code = input("Enter coupon (SAVE10/SAVE20): ")

if code == "SAVE10":

    discount = sum * (10/100)

elif code == "SAVE20":

    discount = sum * (20/100)


total_amount = sum - discount

print(f"Discount: rs {discount}")

print(f"Final Amount: rs {total_amount}")


file_path = "C:\\Users\\hanna\\OneDrive\\Desktop\\PYTHON_WORKS\\bill_qn\\bill.txt"

fw = open(file_path,"w")

fw.write("\n---- Grocery Shop Bill ----\n")

fw.write(f"customer name :{name} \nphone number : {phone_no}\n")

for item,price,kilo in cart:

    fw.write(f"{item} x {kilo} : rs {price} * {kilo}\n")

fw.write(f"total : rs {sum}\n")

fw.write(f"discount : rs {discount}\n")

fw.write(f"finaml amount : rs {total_amount}\n")

fw.write(f"......THANK YOU FOR SHOPPING PLZ VISIT AGAIN .......")

print("\nBill saved successfully!")

