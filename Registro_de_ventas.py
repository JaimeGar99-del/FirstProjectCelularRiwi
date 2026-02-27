print("      *************************")
print("       SALES REGISTER          ")
print("*******************************")

while True:
    try:
        customer_name = input("full customer name\n")
        
        price = float(input("unit sales price\n"))
            
        quantity = int(input("number of products to be sold\n"))

        vip = bool(
            input("customer has vip membership (yes, no)") . strip().lower() == "yes")

        subtotal = price * quantity

        # tax 19% IVA

        tax = subtotal * 0.19


        # discount 10% for being VIP Customer

        if vip == 1:
            discount = subtotal * 0.10
        else:
            discount = 0.0

        total = (subtotal + tax) - discount

        print("                              ")
        print("         INVOICE             ")
        print("                              ")

        print(f" customer name {customer_name}")
        print(f" subtotal           {subtotal}")
        print(f"  discount           {discount}")
        print(f" tax                   {tax}")
        print(f"total                 {total}")

        print(" Thank you for your purchase")
        break

    except ValueError:
        print("Error, you must enter numbers for price and quantity instead of letters, try again")
        
