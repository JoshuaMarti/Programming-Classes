#Initial inputs
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
child_count = float(input("How many children are there? "))
adult_count = float(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax percentage? "))

#Calculating subtotal, sales tax, and pre-tip total
subtotal = child_meal*child_count+adult_meal*adult_count
sales_tax_cost = subtotal * (sales_tax_rate*.01)
subtotal2 = sales_tax_cost+subtotal
print(f"\nSubtotal: ${subtotal:,.2f}\nSales Tax: ${round(sales_tax_cost,2):,.2f}\nPre-Tip Total: ${round(subtotal2,2):,.2f}")
print()

#Checking if they want to tip
tip_amount = 0
tipYN = input("Would you like to tip? (y/n)")
while tipYN.lower() != "y" and tipYN.lower() != "n":
    tipYN = input("Please type y or n ")

if tipYN.lower() == "y":
    tip_amount = float(input("How much would you like to tip? "))

#Determining payment method
total = float(subtotal2+tip_amount)
print(f"Your total is ${total:,.2f}\n")
pay_method = input("Would you like to pay by cash, check, EFT, or Doge? ")
while pay_method.lower() != "cash" and pay_method.lower() != "check" and pay_method.lower() != "eft" and pay_method.lower() != "doge":
    pay_method = input("Please type cash, check, EFT, or Doge. ")

pay_method = pay_method.lower()

#Steps for each of the various payment methods
if pay_method == "cash":
    payment = float(input("What is the payment amount? "))
    #debug
    #print(type(payment),type(total))
    #end-debug
    while payment < total:
        payment = float(input(f"That amount is insufficient. Please enter at least ${total:,.2f} "))
    #print({payment},{total}) #debug
    print(f"Your change is ${payment-total:,.2f}")
    with open("paymentLog.txt", "a") as f:
	    f.write(f"{pay_method},{total},{payment},{payment-total}")

if pay_method == "check":
    print(f"Please make your check payable to Joshua Martinez for ${total:,.2f}")
    with open("paymentLog.txt", "a") as f:
	    f.write(f"{pay_method},{total}")

if pay_method == "eft":
    routing = str(input("Please enter your routing number: "))
    while len(routing) != 9:
        routing = str(input("Please enter a valid routing number: "))
    account = str(input("What is your account number? "))
    account_check = str(input("Please re-enter your account number: "))
    while account != account_check:
        print("The account numbers did not match.")
        account = str(input("What is your account number? "))
        account_check = str(input("Please re-enter your account number: "))
    print(f"Thank you! ${total} will be deducted from your account in 1-5 business days.")
    with open("paymentLog.txt", "a") as f:
	    f.write(f"{pay_method},{total},{routing},{account}")

if pay_method == "doge":
    print("Please send your payment to DGowYDpEcgCNisg76vJEh2LMVWxvndRaRN")
    with open("paymentLog.txt", "a") as f:
	    f.write(f"{pay_method}{total}")

#Tallyho
print("\nThank you for visiting!")