#221012 Joshua Martinez

#Seek Entry
percentage = float(input("What is your grade percentage in the class? "))

#If within a + or - range, declare that
sign = ""
if percentage <= 95 and percentage >= 60:
    if (percentage % 10) >= 7:
        sign = "+"
    elif (percentage % 10) < 3:
        sign = "-"
    else:
        sign = ""

#Determine passing or not
if percentage >= 70:
    passString = "Congratulations! You're passing!"
else:
    passString = "Unfortunately, you're not passing right now. Keep trying though!"

grade_and_sign = "Error 500"
#Determining grade and sign
if percentage >= 90:
    grade_and_sign = (f"A{sign}")
elif  percentage >= 80:
    grade_and_sign = (f"B{sign}")
elif percentage >= 70:
    grade_and_sign = (f"C{sign}")
elif percentage >= 60:
    grade_and_sign = (f"D{sign}")
elif percentage < 60:
    grade_and_sign = "F"
else: #In theory, this should /never/ run.
    print("Error 417. I have no clue how you did this. Please check your entry and try again.")

#Printing grade and sign if applicable
print(f"Your grade is: {grade_and_sign}")

#Printing whether or not they passed
print(f"{passString}")