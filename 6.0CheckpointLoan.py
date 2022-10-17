#First, ask for a rating from 1–10 on the following:
#How large is the loan?
#How good is your credit history?
#How high is your income?
#How large is your down payment?

from turtle import down


print("Please rate the following on a scale from 1-10.")
loan_size = float(input("The size of the loan: "))
credit_history = float(input("Your credit history: "))
income = float(input("The size of your income: "))
down_payment = float(input("The size of your down payment: "))

# First, check if the loan size is at least 5. If it is, use the following rules:
#     If the credit history and income are both at least 7, then the decision is "yes"
#     If either the credit history or income is at least 7, then check if the down payment is at least 5,
#       if it is, the decision is "yes", if not, the decision is "no"
#     Otherwise (if neither the credit history nor income is at least 7), the decision is "no"
# Otherwise (if the loan is not 5 or greater), use these rules:
#     If the credit is less than 4, then the decision is "no"
#     Otherwise, check the following:
#         If either the income or the down payment is at least 7, the decision is "yes"
#         If both the income and the down payment are at least 4, then the answer is "yes"
#         Otherwise, the decision is "no

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        decision = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >=5:
            decision = True
        else: decision = False
    else: decision = False
elif credit_history < 4: decision = False
else:
    if income >= 7 or down_payment >= 7\
        or (income >= 4 and down_payment >= 4): decision = True
    else: decision = False

if decision: print("You can get the loan!")
else: print("You cannot get the loan.")