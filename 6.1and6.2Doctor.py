should_go_to_the_doctor = False

#6.1 if should_go_to_the_doctor:
#    print("Howdy! You ought to consider visiting your local medical practitioner")
#else:
#    print("Congratulations! You seem to be in fair health.")

age = float(input("What is your age? "))
duration = float(input("How many years ago did you last see a medical practitioner?"))

if age >= 60 and duration >= 5 or duration >=20 or \
    age >= 45 and duration >= 10:
    should_go_to_the_doctor = True

if should_go_to_the_doctor:
    print("Howdy! You ought to consider visiting your local medical practitioner")
else:
    print("Congratulations! You seem to be in fair health.")