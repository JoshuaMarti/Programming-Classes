#Python Bank Account Activity, 221116
print("Enter the names and balances of bank accounts, type \"Quit\" when done")
newAccountName = ""
accounts = []
balances = []
total = 0
updateYN = ""
while newAccountName != "Quit":
    newAccountName = input("Account name: ").title()
    if newAccountName != "Quit":
        newBalance = float(input("Balance: $"))
        accounts.append(newAccountName)
        balances.append(newBalance)
print("\nAccount Information")
for spot in range(len(accounts)):
    print(f"{spot}. {accounts[spot]} - ${balances[spot]}")
    total = total + balances[spot]
print(f"\nTotal: ${total}\nAverage: ${total/len(accounts)}\n")

while updateYN != "No":
    updateYN = input("Would you like to update an account? (Yes/No)").title()
    while updateYN != "Yes" and updateYN != "No":
        updateYN = input("Would you like to update an account? (Yes/No)").title()
    if updateYN == "Yes":
        updateIndex = int(input("Account Index: #"))
        while updateIndex < 0 or updateIndex > (len(accounts)-1):
            updateIndex = int(input("Error: Out of Bounds\nAccount Index: #"))
        balances[updateIndex] = float(input(f"New balance for {accounts[updateIndex]} account: $"))
        print("")

        for spot in range(len(accounts)):
            print(f"{spot}. {accounts[spot]} - ${balances[spot]}")


