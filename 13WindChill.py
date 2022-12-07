def windchill(tempF, mph):
    return (35.74+0.6215*tempF-35.75*(mph**.16)+0.4275*tempF*(mph**.16))
def CtoF(tempC):
    return (tempC*(9/5)+32)
temp = ""
while temp != "quit":
    temp = ""
    CorF = ""
    temp = float(input("Input a Temperature: "))
    
    while CorF != "C" and CorF != "F":
        CorF = input("'C' or 'F': ").upper()
    if CorF == "C":
        temp = CtoF(temp)
    counter = 5
    while counter < 61:
        print(f"At {temp}F with winds of {counter} MPH, the windchill is {windchill(temp, counter):.2f}F")
        counter = counter + 5
    temp = input("Type \"Quit\" to Quit, or press Enter to continue: ")